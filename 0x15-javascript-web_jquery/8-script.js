$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (resp) {
  let data = resp.results;
  data.forEach(function (elem) {
    $('UL#list_movies').append('<li>' + elem.title + '</li>');
  });
});
