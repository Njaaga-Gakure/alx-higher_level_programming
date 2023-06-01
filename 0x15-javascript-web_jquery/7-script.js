const character = $('DIV#character');
$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json',
  ({ name }) => {
    character.text(name);
  });
