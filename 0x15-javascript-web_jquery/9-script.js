let tag = $('html').attr('lang');
$.get('https://hellosalut.stefanbohacek.dev/?lang=fr' + tag, function (resp) {
  let data = resp.hello;
  $('DIV#hello').text(data);
});
