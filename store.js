// Valhalla store front on top of the Tebex Headless API: Steam login, basket and checkout are handled by Tebex.
(function () {
  var cfg = window.VALHALLA_STORE || {};
  var API = "https://headless.tebex.io/api";
  var grid = document.getElementById("packages");
  var notice = document.getElementById("store-notice");
  var here = location.href.split("?")[0];
  var login = el("button", "btn", "Sign in through Steam");
  login.type = "button";
  notice.parentNode.insertBefore(login, notice);
  login.addEventListener("click", function () { buy(null); });
  var SYMBOL = {USD: "$", EUR: "€", GBP: "£"};

  // Shown while no Tebex token is configured; mirrors the packages created in the Tebex panel (store-config.js).
  var FALLBACK = cfg.catalogue || [];

  function el(tag, cls, text) { var e = document.createElement(tag); if (cls) e.className = cls; if (text) e.textContent = text; return e; }

  function heading(text, note) {
    var h = el("h3", null, text);
    h.style.gridColumn = "1 / -1";
    h.style.margin = "8px 0 0";
    grid.appendChild(h);
    if (note) {
      var p = el("p", "desc", note);
      p.style.gridColumn = "1 / -1";
      p.style.margin = "0";
      grid.appendChild(p);
    }
  }

  function card(pkg, onBuy) {
    var c = el("article", "pkg");
    c.appendChild(el("h4", null, pkg.name));
    c.appendChild(el("div", "price", (pkg.from ? "from " : "") + (SYMBOL[cfg.currency] || "") + pkg.price + (SYMBOL[cfg.currency] ? "" : " " + (cfg.currency || ""))));
    var ul = el("ul");
    (pkg.perks || []).forEach(function (p) { ul.appendChild(el("li", null, p)); });
    if (pkg.description) { var d = el("div", "desc"); d.innerHTML = pkg.description; c.appendChild(d); }
    c.appendChild(ul);
    if (pkg.note) c.appendChild(el("div", "desc", pkg.note));
    var b = el("button", "btn block", onBuy ? "Buy now" : "Opening soon");
    if (onBuy) b.addEventListener("click", function () { onBuy(pkg); }); else b.disabled = true;
    c.appendChild(b);
    return c;
  }

  function showCatalogue() {
    FALLBACK.forEach(function (cat) {
      heading(cat.category, cat.note);
      (cat.packages || []).forEach(function (p) { grid.appendChild(card(p, null)); });
    });
  }

  function api(method, path, body) {
    return fetch(API + path, {method: method, headers: {"Content-Type": "application/json"}, body: body ? JSON.stringify(body) : undefined})
      .then(function (r) { if (!r.ok) throw new Error("Tebex " + r.status); return r.json(); });
  }

  function configure(pkg) {
    notice.textContent = "Loading package options...";
    api("GET", "/accounts/" + cfg.token + "/packages/" + pkg.id)
      .then(function (res) {
        var variables = res.data.variables || [];
        if (!variables.length) { buy(pkg, {}); return; }
        var dialog = el("dialog", "store-options");
        var form = el("form");
        var values = {};
        form.appendChild(el("h3", null, pkg.name));
        variables.forEach(function (v) {
          var label = el("label", null, v.description || v.identifier);
          var input = el(v.type === "dropdown" ? "select" : "input");
          input.name = v.identifier;
          input.required = true;
          if (v.type === "dropdown") {
            var blank = el("option", null, "Choose an option"); blank.value = ""; input.appendChild(blank);
            (v.options || []).forEach(function (o) { var option = el("option", null, o.name); option.value = o.id; input.appendChild(option); });
          } else { input.type = "text"; if (v.max_length) input.maxLength = v.max_length; }
          label.appendChild(input); form.appendChild(label);
          values[v.identifier] = input;
        });
        var proceed = el("button", "btn", "Continue to checkout"); proceed.type = "submit";
        var cancel = el("button", "btn ghost", "Cancel"); cancel.type = "button";
        cancel.addEventListener("click", function () { dialog.close(); });
        form.appendChild(proceed); form.appendChild(cancel);
        form.addEventListener("submit", function (event) {
          event.preventDefault();
          var data = {}; Object.keys(values).forEach(function (key) { data[key] = values[key].value; });
          dialog.close(); buy(pkg, data);
        });
        dialog.addEventListener("close", function () { dialog.remove(); });
        dialog.appendChild(form); document.body.appendChild(dialog); dialog.showModal();
        notice.textContent = "Choose the agreed package option. Tebex confirms the final price before payment.";
      }).catch(function () { notice.textContent = "Could not load package options. Please try again."; });
  }

  function buy(pkg, variableData) {
    notice.textContent = "Preparing your basket...";
    api("POST", "/accounts/" + cfg.token + "/baskets", {complete_url: here + "?done=1", cancel_url: here, complete_auto_redirect: true})
      .then(function (res) {
        var ident = res.data.ident;
        localStorage.setItem("vBasket", JSON.stringify({ident: ident, pkg: pkg ? pkg.id : null, variables: variableData || {}}));
        return api("GET", "/accounts/" + cfg.token + "/baskets/" + ident + "/auth?returnUrl=" + encodeURIComponent(here + "?basket=" + ident));
      })
      .then(function (links) {
        var provider = links.find(function (p) { return /steam/i.test(p.name); }) || links[0];
        if (!provider || !provider.url) throw new Error("Steam sign-in is unavailable");
        var target = new URL(provider.url);
        if (target.protocol !== "https:" || !(target.hostname === "steamcommunity.com" || target.hostname.endsWith(".tebex.io"))) throw new Error("Invalid sign-in address");
        location.href = target.href;
      })
      .catch(function (e) { notice.textContent = "The store is unavailable right now (" + e.message + "). Please try again later."; });
  }

  function resume(ident) {
    var saved = {};
    try { saved = JSON.parse(localStorage.getItem("vBasket") || "{}"); } catch (e) {}
    if (saved.ident !== ident) return;
    notice.textContent = "Checking Steam sign-in...";
    api("GET", "/accounts/" + cfg.token + "/baskets/" + encodeURIComponent(ident))
      .then(function (res) {
        if (!res.data.username_id) throw new Error("Steam sign-in was not completed");
        login.textContent = "Steam: " + (res.data.username || res.data.username_id);
        notice.textContent = "Signed in through Steam.";
        history.replaceState(null, "", here);
        if (!saved.pkg) return null;
        notice.textContent = "Signed in through Steam. Opening checkout...";
        return api("POST", "/baskets/" + ident + "/packages", {package_id: saved.pkg, quantity: 1, variable_data: saved.variables || {}});
      })
      .then(function (res) { if (res) { localStorage.removeItem("vBasket"); location.href = res.data.links.checkout; } })
      .catch(function (e) { notice.textContent = "Could not add the package (" + e.message + ")."; });
  }

  var params = new URLSearchParams(location.search);
  if (params.get("done")) notice.textContent = "Check your Tebex receipt for payment confirmation. Delivered perks appear in /perks; custom packages are handled by staff.";

  if (!cfg.token) {
    login.disabled = true;
    showCatalogue();
    if (!params.get("done")) notice.textContent = "The store opens soon. Ask on our Discord if you want to support us earlier.";
    return;
  }

  if (params.get("basket")) resume(params.get("basket"));
  else {
    try { var prior = JSON.parse(localStorage.getItem("vBasket") || "{}"); if (prior.ident && !prior.pkg) resume(prior.ident); } catch (e) {}
  }
  api("GET", "/accounts/" + cfg.token + "/categories?includePackages=1")
    .then(function (res) {
      (res.data || []).forEach(function (cat) {
        if (!(cat.packages || []).length) return;
        heading(cat.name);
        (cat.packages || []).forEach(function (p) {
          grid.appendChild(card({id: p.id, name: p.name, price: Number(p.total_price ?? p.base_price).toFixed(2), from: p.name === "Custom Character", description: p.description}, configure));
        });
      });
    })
    .catch(function () { showCatalogue(); });
})();
