const updateHeader = $('DIV#update_header');
const header = $('header');
updateHeader.on('click', () => {
  header.text('New Header!!!');
});
