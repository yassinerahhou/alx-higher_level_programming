$(function () {
  $("#btn_translate").click(function () {
    var language_code = $("#language_code").val();
    $.get(
      "https://hellosalut.stefanbohacek.dev/?lang=" + language_code,
      function (data) {
        $("#hello").text(data.hello);
      }
    );
  });
});
