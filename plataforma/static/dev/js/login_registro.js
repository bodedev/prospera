// Form por AJAX
$('.formAccessAjax').on('submit', function(e){
  e.preventDefault();
  console.log('HERE!');
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
          var parent = form.find('[name='+key+']').parent();
          parent.addClass('has-error');
          parent.find('p.help-block').text(input.message);
        });
      });
    }
  })
});