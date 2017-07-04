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

})