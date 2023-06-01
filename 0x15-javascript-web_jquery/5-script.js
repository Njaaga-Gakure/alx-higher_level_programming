const div = $('DIV#add_item');
const list = $('.my_list');
div.on('click', () => {
  list.append('<li>Item</li>');
});
