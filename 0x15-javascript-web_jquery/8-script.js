const movieList = $('UL#list_movies');
$.get('https://swapi-api.alx-tools.com/api/films/?format=json',
  ({ results }) => {
    results.forEach(({ title }) => {
      movieList.append(`<li>${title}</li>`);
    });
  });
