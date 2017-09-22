function grabArticle(){
  $.ajax({
    method: "GET",
    url: "http://localhost:8000/search/arxiv_xml/",

  }).done(function(xml){
    $("#id").html(xml.id);
    $("#title").html(xml.title);
    $("#authors").html(xml.authors);
    $("#arxiv_id").html('<a target="_blank" href="https://arxiv.org/abs/' + xml.arxiv_id.replace("oai:arXiv.org:", "") + '">' + xml.arxiv_id + '</a>');
    $("#abstract").html(xml.abstract);
    $("#skip_id").attr("value", xml.id);

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
