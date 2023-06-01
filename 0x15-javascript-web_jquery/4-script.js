const header = $('header');
const div = $('DIV#toggle_header');
div.on('click', () => {
  header.toggleClass('green red');
});
