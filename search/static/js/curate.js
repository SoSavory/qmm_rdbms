function grabArticle(){
  $.ajax({
    method: "GET",
    url: "http://localhost:8000/search/arxiv_xml/",

  }).done(function(xml){
    $("#id").html(xml.id);
    $("#title").html(xml.title);
    $("#authors").html(xml.authors);
    $("#arxiv_id").html('<a href="https://arxiv.org/abs/' + xml.arxiv_id.replace("oai:arXiv.org:", "") + '">' + xml.arxiv_id + '</a>');
    $("#abstract").html(xml.abstract);

    $("#hidden_title").attr("value", xml.title);
    $("#hidden_authors").attr("value", xml.authors);
    $("#hidden_link").attr("value", "https://arxiv.org/abs/" + xml.arxiv_id.replace("oai:arXiv.org:", ""));

    $("#current_user").html("Current User: " + xml.user_name)
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
  // submitCuration($form);
});
