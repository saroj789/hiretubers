

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



// let tr=$('.dashboard tr')
// for (let index = 0; index < tr.length; index++) {
//     const element = tr[index].children[2];
//     element.innerHTML=''
// }


// let tr2=$('.dashboard tbody tr a ')

// console.log(tr2)
// for (let index = 0; index < tr2.length; index++) {
//     const element = tr2[index]
//     console.log(element.innerText='page')
// }



