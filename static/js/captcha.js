!(function(t) {
  "use strict";
  t.fn.captcha = function(a) {
    var e = t.extend(
        {
          idCaptchaText: "captchaText",
          idCaptchaInput: "captchaInput",
          class: ""
        },
        a
      ),
      i = t(this).find("input[type=submit]");
    i.attr("disabled", "disabled"),
      t('<label id="' + e.idCaptchaText + '"></label>').insertBefore(i),
      t(
        '<input id="' +
          e.idCaptchaInput +
          '" aria-label="Captcha Input" type="text" required>'
      ).insertBefore(i);
    var d = this.find("#" + e.idCaptchaText),
      s = this.find("#" + e.idCaptchaInput),
      n = Math.floor(10 * Math.random()),
      r = Math.floor(10 * Math.random()),
      c = n + r;
    return (
      t(d).text(n + " + " + r + " ="),
      t(s).keyup(function() {
        t(this).val() == c
          ? i.removeAttr("disabled").addClass(e.class)
          : i.attr("disabled", "disabled").removeClass(e.class);
      }),
      this
    );
  };
})(jQuery);
