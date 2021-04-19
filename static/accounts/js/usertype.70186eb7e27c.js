
      // for usertype buttons
        
      $(document).ready(function(){      
          $(".usertype > input").val('0');
        }); 
    
      $(".usertype > .btn").click(function(event){

            console.log($('.usertype  > input').val())
            $(".usertype > .btn").removeClass("active").css('background-color','gray')
            $(this).addClass("active");
            $(this).css('background-color','rgb(25, 0, 255)')
            event.preventDefault()
     
            $('.usertype  > input').val($(this).val())

      });
      
