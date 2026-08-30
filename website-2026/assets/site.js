/* Kulé kulé Zanskar — small progressive enhancements. No dependencies. */
(function () {
  "use strict";

  /* ---- mobile navigation ------------------------------------------- */
  var toggle = document.querySelector(".nav-toggle");
  var menu = document.getElementById("menu");
  if (toggle && menu) {
    toggle.addEventListener("click", function () {
      var open = menu.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      toggle.textContent = open ? "Close" : "Menu";
    });
  }

  /* ---- journey filters --------------------------------------------- */
  var bar = document.querySelector("[data-filters]");
  var list = document.querySelector("[data-journeys]");
  var counter = document.querySelector("[data-count]");

  if (bar && list) {
    var state = { style: "all", level: "all", len: "all" };
    var cards = Array.prototype.slice.call(list.children);

    function apply() {
      var shown = 0;
      cards.forEach(function (card) {
        var ok =
          (state.style === "all" || card.dataset.style === state.style) &&
          (state.level === "all" || card.dataset.level === state.level) &&
          (state.len === "all" || card.dataset.len === state.len);
        card.hidden = !ok;
        if (ok) shown++;
      });
      if (counter) {
        counter.textContent =
          shown === cards.length
            ? "Showing all " + cards.length + " journeys"
            : "Showing " + shown + " of " + cards.length + " journeys";
      }
    }

    bar.addEventListener("click", function (e) {
      var chip = e.target.closest(".chip");
      if (!chip) return;
      var group = chip.dataset.filter;
      state[group] = chip.dataset.value;
      bar.querySelectorAll('.chip[data-filter="' + group + '"]').forEach(function (c) {
        c.classList.toggle("is-on", c === chip);
        c.setAttribute("aria-pressed", c === chip ? "true" : "false");
      });
      apply();
    });

    bar.querySelectorAll(".chip").forEach(function (c) {
      c.setAttribute("aria-pressed", c.classList.contains("is-on") ? "true" : "false");
    });
    apply();
  }

  /* ---- prefill the enquiry form from ?journey= ---------------------- */
  var select = document.getElementById("journey");
  if (select) {
    var wanted = new URLSearchParams(window.location.search).get("journey");
    if (wanted) {
      var match = Array.prototype.slice.call(select.options).some(function (o) {
        if (o.value === wanted) { select.value = wanted; return true; }
        return false;
      });
      if (match) { select.setAttribute("data-prefilled", "true"); }
    }
  }
})();
