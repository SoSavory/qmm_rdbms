function grabFormData(formElement, callback){
  $values = {};
  $(formElement).on('submit', function( event ){
    event.preventDefault();
    $.each($(formElement).serializeArray(), function(i, field){
      $values[field.name] = field.value;
    });
    callback($values);
  })
}
