const header = $('header');
const div = $('DIV#red_header');
div.on('click', () => {
  header.addClass('red');
});
