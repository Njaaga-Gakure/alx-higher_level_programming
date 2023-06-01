const div = $('DIV#hello');
$.get('https://www.fourtonfish.com/hellosalut/hello/',
  ({ hello }) => {
    div.text(hello);
  });
