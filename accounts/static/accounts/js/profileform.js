$(document).ready(function(){

        var crew=$('.crew .selected')
        
        crew.siblings().each( function(){
                
                if ($(this).val()==crew.val()){
                    $(this).css('display','none')
                    crew.css('color','coral')

                }
        } )  
})


$(document).ready(function(){

    var camera_type=$('#camera_type .selected')
    
    camera_type.siblings().each( function(){
            
            if ($(this).val()==camera_type.val()){
                $(this).css('display','none')
                camera_type.css('color','coral')

            }
    } )  
})


$(document).ready(function(){

    var category=$('#category .selected')
    
    category.siblings().each( function(){
            
            if ($(this).val()==category.val()){
                $(this).css('display','none')
                category.css('color','coral')

            }

    } )  

})