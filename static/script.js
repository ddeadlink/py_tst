$(function() {

  // delete
    $('.delete').map(function(key, element){
      $(element).click(function(){

        $.ajax({
          url: "/ajaxDelete",
          type: 'POST',
          data: {id:element.id, key: $(element).attr('data-trigger')},
          success: function(result){
            $(element).parents()[0].remove();
          }
        });

      })
    });


    // full info
    $('.view').map(function(key, element){
      $(element).click(function(){
        $($('.info-block')[key]).toggleClass('show');
      })
    });



});
