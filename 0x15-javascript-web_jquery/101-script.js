$(document).ready(() => {
  const list = $('UL.my_list');
  const addItem = $('DIV#add_item');
  const removeItem = $('DIV#remove_item');
  const clearList = $('DIV#clear_list');
  addItem.on('click', () => {
    list.append('<li>Item</li>');
  });
  removeItem.on('click', () => {
    list.children().last().remove();
  });
  clearList.on('click', () => {
    list.empty();
  });
});
