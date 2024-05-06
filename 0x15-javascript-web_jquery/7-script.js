$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (resp) {
  $('DIV#character').text(resp.name);
});
