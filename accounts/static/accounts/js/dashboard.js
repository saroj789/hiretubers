

 function cancel(hire_id,event){
            var ajaxreq=new XMLHttpRequest()
            alert(hire_id)
            row =   event.target.parentElement.parentElement
                   
                     
            ajaxreq.onreadystatechange=function(){
                if (this.readyState==4) {
                    alert(this.responseText)
                    console.log(hire_id,row)
                    row.remove()
                }

            }
            
            ajaxreq.open('GET','../hiretubers/reqcancel/'+String(hire_id),true)
            ajaxreq.send(hire_id,row)
               
}


function accept(hire_id,event){
    var ajaxreq=new XMLHttpRequest()
    alert(hire_id)
    row =   event.target.parentElement.parentElement
           
             
    ajaxreq.onreadystatechange=function(){
        if (this.readyState==4){
            alert(this.responseText)
            console.log(hire_id,row)
            //row.remove()
        }

    }
    
    ajaxreq.open('GET','../hiretubers/reqaccept/'+String(hire_id),true)
    ajaxreq.send(hire_id,row)

    // var link=location.origin + '/hiretubers/req'+  event.target.id  +'/' +hire_id
    // console.log(link,'../hiretubers/reqaccept/')

    // ajaxreq.open('GET',link,true)
    // ajaxreq.send(hire_id,row)
       
}



function reject(hire_id,event){
    var ajaxreq=new XMLHttpRequest()
    alert(hire_id)
    row =   event.target.parentElement.parentElement
           
             
    ajaxreq.onreadystatechange=function(){
        if (this.readyState==4){
            alert(this.responseText)
            
            //row.remove()
        }
    }

    ajaxreq.open('GET','../hiretubers/reqreject/'+String(hire_id),true)
    ajaxreq.send(hire_id,row)

}
