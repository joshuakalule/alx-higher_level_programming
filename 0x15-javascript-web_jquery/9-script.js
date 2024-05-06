$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (resp) {
  let data = resp.hello;
  $('DIV#hello').text(data);
});
