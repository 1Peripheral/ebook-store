var updateBtns = document.getElementsByClassName('update-cart')


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

for (i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function () {
        var productId = this.dataset.product
        var action = this.dataset.action

        if (user == 'AnonymousUser') {
            alert('User is not authenticated')
        } else {
            updateUserOrder(productId, action)
        }
    })
}

function updateUserOrder(productId, action){
        var url = '/update_item/'

        fetch(url, {
            method:'POST',
            headers:{
                'Content-Type':'application/json',
                'X-CSRFToken': csrftoken,
            },
            body:JSON.stringify({'productId':productId, 'action':action})
        })
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            location.reload()
        });
}