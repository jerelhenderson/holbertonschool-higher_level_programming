$.get('https://swapi.co/api/films/?format=json', function (data) {
  let films = data.results
  for (let i in films) {
    $('UL#list_movies').append('<li>' + films[i].title + '</li>');
  }
});
