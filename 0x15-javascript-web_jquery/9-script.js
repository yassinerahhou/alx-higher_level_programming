$(function () {
  $.ajax({
    url: "https://hellosalut.stefanbohacek.dev/?lang=fr",
    success: function (sata) {
      //Within the success callback function, you use $("#hello") to select an HTML element with the ID hello. This is the element where you want to display the "hello" translation.

      $("#hello").text(sata.hello);
    },
  });
});
