// Valhalla store front on top of the Tebex Headless API: Steam login, basket and checkout are handled by Tebex.
(function () {
  var cfg = window.VALHALLA_STORE || {};
  var API = "https://headless.tebex.io/api";
  var grid = document.getElementById("packages");
  var notice = document.getElementById("store-notice");
  var here = location.href.split("?")[0];

  // Shown while no Tebex token is configured; mirrors the packages created in the Tebex panel.
  var FALLBACK = [
    {name: "VIP - 30 days", price: "4.99", perks: ["Premium vehicles at the car dealer", "+25 % pay every paycheck", "VIP tag in OOC chat", "Discord VIP role"]},
    {name: "VIP - 90 days", price: "12.99", perks: ["Everything in VIP", "Save 13 % against monthly", "Stacks with running VIP time"]},
    {name: "Premium vehicles", price: "9.99", perks: ["Permanent access to premium vehicles", "Lassiter Hollywood, Mercedes G4 W31", "Every future premium car included"]},
    {name: "Supporter", price: "2.99", perks: ["Supporter tag in OOC chat", "Discord supporter role", "Our thanks - it keeps the server online"]}
  ];

  function el(tag, cls, text) { var e = document.createElement(tag); if (cls) e.className = cls; if (text) e.textContent = text; return e; }

  function card(pkg, onBuy) {
    var c = el("article", "pkg");
    c.appendChild(el("h4", null, pkg.name));
    c.appendChild(el("div", "price", (cfg.currency === "EUR" ? "€" : "") + pkg.price));
    var ul = el("ul");
    (pkg.perks || []).forEach(function (p) { ul.appendChild(el("li", null, p)); });
    if (pkg.description) { var d = el("div", "desc"); d.innerHTML = pkg.description; c.appendChild(d); }
    c.appendChild(ul);
    var b = el("button", "btn block", onBuy ? "Buy now" : "Opening soon");
    if (onBuy) b.addEventListener("click", function () { onBuy(pkg); }); else b.disabled = true;
    c.appendChild(b);
    return c;
  }

  function api(method, path, body) {
    return fetch(API + path, {method: method, headers: {"Content-Type": "application/json"}, body: body ? JSON.stringify(body) : undefined})
      .then(function (r) { if (!r.ok) throw new Error("Tebex " + r.status); return r.json(); });
  }

  function buy(pkg) {
    notice.textContent = "Preparing your basket...";
    api("POST", "/accounts/" + cfg.token + "/baskets", {complete_url: here + "?done=1", cancel_url: here, complete_auto_redirect: true})
      .then(function (res) {
        var ident = res.data.ident;
        localStorage.setItem("vBasket", JSON.stringify({ident: ident, pkg: pkg.id}));
        return api("GET", "/accounts/" + cfg.token + "/baskets/" + ident + "/auth?returnUrl=" + encodeURIComponent(here + "?basket=" + ident));
      })
      .then(function (links) { location.href = links[0].url; })   // Steam login at Tebex
      .catch(function (e) { notice.textContent = "The store is unavailable right now (" + e.message + "). Please try again later."; });
  }

  function resume(ident) {
    var saved = {};
    try { saved = JSON.parse(localStorage.getItem("vBasket") || "{}"); } catch (e) {}
    if (saved.ident !== ident) return;
    notice.textContent = "Signed in with Steam. Opening checkout...";
    api("POST", "/baskets/" + ident + "/packages", {package_id: saved.pkg, quantity: 1})
      .then(function (res) { localStorage.removeItem("vBasket"); location.href = res.data.links.checkout; })
      .catch(function (e) { notice.textContent = "Could not add the package (" + e.message + ")."; });
  }

  var params = new URLSearchParams(location.search);
  if (params.get("done")) notice.textContent = "Thank you! Your perks arrive in game within a minute (type /perks).";

  if (!cfg.token) {
    FALLBACK.forEach(function (p) { grid.appendChild(card(p, null)); });
    if (!params.get("done")) notice.textContent = "The store opens soon. Ask on our Discord if you want to support us earlier.";
    return;
  }

  if (params.get("basket")) resume(params.get("basket"));
  api("GET", "/accounts/" + cfg.token + "/categories?includePackages=1")
    .then(function (res) {
      (res.data || []).forEach(function (cat) {
        (cat.packages || []).forEach(function (p) {
          grid.appendChild(card({id: p.id, name: p.name, price: Number(p.total_price || p.base_price).toFixed(2), description: p.description}, buy));
        });
      });
    })
    .catch(function () { FALLBACK.forEach(function (p) { grid.appendChild(card(p, null)); }); });
})();
