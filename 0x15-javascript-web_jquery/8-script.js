// $ function == jQuery == $.(documenr).ready(function () {})
$(function () {
  // MAking ajax get requesr to get the data from this url
  $.get(
    "https://swapi-api.alx-tools.com/api/films/?format=json",
    function (data) {
      // Loop through the results array and append each title to the UL element with id list_movies
      // data = the response from the API , data.results = the results array , data.results.title = the title of each film
      data.results.forEach(function (film) {
        $("#list_movies").append("<li>" + film.title + "</li>");
      });
    }
  );
});

