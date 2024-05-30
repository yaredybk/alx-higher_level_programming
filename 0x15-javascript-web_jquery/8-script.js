// fetches and lists the title for all movies by using this URL:
// https://swapi-api.alx-tools.com/api/films/?format=json
// 
// All movie titles must be list in the HTML tag UL#list_movies

$(document).ready(function() {
    $.ajax({
        url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
        method: 'GET',
        success: function(data) {
            const films = data.results;
            films.forEach(film => {
                $('UL#list_movies').append('<li>' + film.title + '</li>');
            });
        }
    });
});
