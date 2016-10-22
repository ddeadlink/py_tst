$(function() {

  // delete
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

    // full info
    $('.view').map(function(key, element){
      $(element).click(function(){
        $($('.info-block')[key]).toggleClass('show');
      })
    })

/*
    if ( $('#position option:selected').text() == '' ){
       $('#position').attr('disabled','disabled');
       $('.form-group button').attr('disabled','disabled');
       $('#position').append('<option>create position first</option>')

    }

    if ( $('#department option:selected').text() == '' ){
       $('#department').attr('disabled','disabled');
       $('.form-group button').attr('disabled','disabled');
       $('#department').append('<option>create department first</option>');
    }
*/
});
