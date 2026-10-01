// Drifting star field behind the header, like the particle sky of the old community boards.
(function () {
  var canvas = document.getElementById("stars");
  if (!canvas || !canvas.getContext) return;
  var ctx = canvas.getContext("2d");
  var stars = [], w = 0, h = 0, ratio = window.devicePixelRatio || 1;
  var still = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function resize() {
    w = canvas.offsetWidth; h = canvas.offsetHeight;
    canvas.width = w * ratio; canvas.height = h * ratio;
    ctx.setTransform(ratio, 0, 0, ratio, 0, 0);
    var count = Math.round(w * h / 2600);
    stars = [];
    for (var i = 0; i < count; i++) {
      stars.push({
        x: Math.random() * w, y: Math.random() * h, r: Math.random() * 1.4 + 0.3,
        vx: (Math.random() - 0.5) * 0.12, vy: (Math.random() - 0.5) * 0.12,
        a: Math.random() * 0.6 + 0.2, t: Math.random() * Math.PI * 2, purple: Math.random() < 0.25
      });
    }
  }

  function frame() {
    ctx.clearRect(0, 0, w, h);
    for (var i = 0; i < stars.length; i++) {
      var s = stars[i];
      if (!still) {
        s.x = (s.x + s.vx + w) % w; s.y = (s.y + s.vy + h) % h; s.t += 0.02;
      }
      var alpha = s.a * (0.65 + 0.35 * Math.sin(s.t));
      ctx.beginPath();
      ctx.arc(s.x, s.y, s.r, 0, Math.PI * 2);
      ctx.fillStyle = s.purple ? "rgba(150,100,240," + alpha + ")" : "rgba(220,215,255," + alpha + ")";
      ctx.fill();
    }
    if (!still) requestAnimationFrame(frame);
  }

  window.addEventListener("resize", function () { resize(); if (still) frame(); });
  resize();
  frame();
})();
