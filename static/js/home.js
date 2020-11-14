
var updatebtns=document.getElementsByClassName('update-cart')

for (var i=0;i<updatebtns.length;i++)
{

    updatebtns[i].addEventListener('click',function(){

var productid=this.dataset.product
var action=this.dataset.action
console.log('productid:',productid, 'action:',action)
console.log(user)
if (user =='AnonymousUser'){
   guestuser(productid,action)
}
else{
    updateuser(productid,action)
}

    })
}
function guestuser(productid,action){
    console.log("hey bitch")
    if (action=='add'){
        if(cart[productid]==undefined){
            cart[productid]={'quantity':1}
        }
        else{
         cart[productid]['quantity']+=1
    }
    }
    if (action=='remove'){
        cart[productid]['quantity']-=1
        if(cart[productid]['quantity']<=0){
            console.log('remove item')
            delete cart[productid]
        }
    }

console.log("cart:",cart)
document.cookie='cart='+JSON.stringify(cart)+";domain=;path=/"
location.reload()
}

function updateuser(productid,action){
    console.log('fuck u')
    var url='/update'
    fetch (url,{

  method:'POST',
  headers:{'Content-Type':'application/json',

           'X-CSRFToken':csrftoken,

},
  body:JSON.stringify({'productid':productid,'action':action})

    }
        )

.then((response)=>{return response.json})

.then((data)=>{
    console.log('data:',data);
    location.reload();


})


    }

