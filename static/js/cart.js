var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function () {
        var productId = this.dataset.productId
        var action = this.dataset.action
        console.log('productId:', productId, 'Action:', action)
        console.log('USER:', user)

        if (user == 'AnonymousUser') {
            console.log('User is not authenticated')
        } else {
            updateUserOrder(productId, action)
        }
    })
}

function updateUserOrder(productId, action){
    console.log('User is authenticated, sending data...')
        var url = '/update_item/'
        console.log('URL:', url)

        fetch(url, {
            method:'POST',
            headers:{
                'Content-Type':'application/json'
                'X-CSRFToken': csrftoken,
            },
            body:JSON.stringfy({'productId':productId, 'action':action})
        })
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            console.log('data:', data)
            location.reload()
        });
}
// < >