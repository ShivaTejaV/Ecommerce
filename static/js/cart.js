var updateButtons=document.getElementsByClassName("update-cart");

for(var i=0;i<updateButtons.length;i++){
    updateButtons[i].addEventListener("click",function(){
        var productId=this.dataset.product;
        var action=this.dataset.action;
        console.log('Product Id:',productId,'Action:',action);

        console.log('USER : ',user);
        if(user==='AnonymousUser'){
            console.log('Not logged in');
        }else{
            updateUserOrder(productId,action);
        }
    })
}

function   updateUserOrder(productId,action){
    console.log('User is Logged in Sending Data..');

    var url = 'update_item/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({'productId':productId,'action':action})
    })
    .then((response) => {
        return response.json()
    })
    .then(data => {
        console.log('Data:', data);
        location.reload()
    })

}