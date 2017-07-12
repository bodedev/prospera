// Form por AJAX
$('.formAccessAjax').on('submit', function(e){
  e.preventDefault();
  var form = $(this);
  var url = form.attr('action');
  var data = form.serialize();
  $('.formAccessAjax').find('.form-group').removeClass('has-error');
  $('.formAccessAjax').find('p.help-block').text('');

  $.ajax({
    method: 'POST',
    data: data,
    url: url,
    success: function(data) {
      // Quando é a resposta de sucesso de registro, tem a mensagem, se é login, não tem
      if (data.hasOwnProperty("message")) {
        // Mostra a mensagem de sucesso de registro
        $('#message-registro').css("display", "block");
        $('#message-registro').html(data.message);
      }
      else {
        // Recarrega a página pra mostrar que está logado
        location.reload();
      }
    },
    error: function(data) {
      var json = JSON.parse(data.responseJSON);
      Object.keys(json).map((key, index) => {
        json[key].map((input) => {
          if(key == "__all__"){
            form.find("p#__all__").text(input.message);
          }else{
            var parent = form.find('[name='+key+']').parent();
            parent.addClass('has-error');
            parent.find('p.help-block').text(input.message);
          }
        });
      });
    }
  })
});

$('[data-toggle="changeLogin"]').on('click', function(e){
  e.preventDefault()
  var btn = $(this),
      target = btn.data('target'),
      active = btn.closest('form').attr('id');

  $('#'+target).css("display", "block");
  $('#'+active).css("display", "none");
})
