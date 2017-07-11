$(document).ready(function() {

  // Preview image
  $('#id_imagem').change(function(){
    var imageInput = $(this)
    var file = imageInput[0].files[0]
    var reader = new FileReader()
    reader.readAsDataURL(file)
    reader.onload = function (index) {
        $('img.upload-image').attr('src', this.result);
    }.bind(reader);
  });

  // Alert auto dismiss
  $(".alert").fadeTo(2000, 500).slideUp(500, function(){
    $(".alert").slideUp(500);
  });

  // Spinners
  $(".loading-spinner").each(function(index) {
    var element = $(this);
    var url = $(this).data('url');
    if(url != ""){
      console.log("TEM url "+url);
      $.ajax({
          url: url,
          type: 'GET',
          success: function(data) {
            $(element).css("display", "none");
            $(element).after(data);
          },
          error: function(err) {
            console.log("erro");
          }
      });
    }else{
      console.log("Elemento não possui url");
    }
  });

})
