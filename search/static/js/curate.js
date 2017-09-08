function grabArticle(){
  $.ajax({
    method: "GET",
    url: "http://localhost:8000/search/arxiv_xml/",

  }).done(function(xml){
    $("#id").html(xml.id);
    $("#title").html(xml.title);
    $("#authors").html(xml.authors);
    $("#arxiv_id").html(xml.arxiv_id);
    $("#abstract").html(xml.abstract);
  });
}

function submitCuration(element){
  console.log(element);

  grabFormData(element, function(values){
    console.log(values);

    $.ajax({
      type: 'POST',
      url: 'http://localhost:8000/search/curate_arxiv_article/',
      contentType: 'application/json',
      dataType: 'json',
      data: JSON.stringify(values),
    }).done(function(response){
      grabArticle();
      console.log(response);
    })
  })
}

$(document).ready(function(){
  $form = $('form')[0]
  grabArticle();
  submitCuration($form);
});
