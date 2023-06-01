const div = $('DIV#red_header');
console.log(div);
div.on('click', () => {
  div.css('color', '#FF0000');
});
