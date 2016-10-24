$(function() {

  // delete
    $('.delete').map(function(key, element){

      $(element).click(function(){

        //check if user is master and give an option to select new master
        if ( $(element).attr('data-master') != '0' && $(element).attr('data-master') ){
          $.ajax({
            url: "/ajaxGetMaster",
            type: 'POST',
            data: {id:element.id},
            success: function(result){
              var master = $(element).attr('data-master');
              $(element).attr('data-master','0');
              $(result).insertAfter($(element))

              $('#masterChange').on('change',function(){

                $.ajax({
                  url: "/ajaxDeleteUpdate",
                  type: 'POST',
                  data: {id:element.id, key: $(element).attr('data-trigger'),change:this.value,master:master},
                  success: function(result){
                    $(element).parents()[0].remove();
                  }
                });

              });

            }
          });


        } else if ( $(element).attr('data-position') == 'position' ){
          $.ajax({
            url: "/ajaxGetPosition",
            type: 'POST',
            data: {id:element.id},
            success: function(result){
              $(result).insertAfter($(element))
              $(element).attr('data-master','0')
              $('#positionChange').on('change',function(){
                $.ajax({
                  url: "/ajaxDelete",
                  type: 'POST',
                  data: {id:element.id, key: $(element).attr('data-trigger'),change:this.value,position:$(element).attr('data-name')},
                  success: function(result){
                    $(element).parents()[0].remove();
                  }
                });
              });
            }
          });

        } else if ( $(element).attr('data-department') != '' && $(element).attr('data-department')){
          $.ajax({
            url: "/ajaxDelete",
            type: 'POST',
            data: {id:element.id,key: $(element).attr('data-trigger'),parent:$(element).attr('data-department'),
                  current:document.getElementsByClassName('dep-name')[key].innerHTML},
            success: function(result){
              $(element).parents()[0].remove();
            }
          });
        } else {
          $.ajax({
            url: "/ajaxDelete",
            type: 'POST',
            data: {id:element.id, key: $(element).attr('data-trigger')},
            success: function(result){
              $(element).parents()[0].remove();
            }
          });

        }

      })
    });


    // full info
    $('.view').map(function(key, element){
      $(element).click(function(){
        $($('.info-block')[key]).toggleClass('show');
      })
    });


});
