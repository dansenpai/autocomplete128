jQuery(document).ready(function($) {
  $('.ui.search')
    .search({
      apiSettings: {
        url: '/autocomplete/?term={query}'
      },
      minCharacters: 3,
      maxResults: 15,
      fields: {
        results: 'results',
        title: 'name',
        description: 'rank_position'
      },
      errors:{
         noResults: "Nenhum resultado"
      },
      onSelect: function(result, response){
        window.location.href = '/player/'+ response[0].id;
      },
    })
  ;
});