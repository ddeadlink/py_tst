$(function() {


    $('.delete').map(function(key, element){
      $(element).click(function(){

        $.ajax({
          url: "/ajax",
          type: 'POST',
          data: {id:element.id, key: $(element).attr('data-trigger')},
          success: function(result){
            $(element).parents()[0].remove();
          }
        });

      })
    });


    $('.view').map(function(key, element){
      $(element).click(function(){
        $($('.info')[key]).toggleClass('show');
      })
    })

});