

// setTimeout(() => {
//     const messages = document.getElementsByClassName('messages')
//     messages.style.display = 'none'
// }, 2000)


// let times = document.getElementById('times')
// let messages = document.getElementById('messages')

// times.addEventListener('click', () => {
//     messages.style.display = 'none'
// })


function removeAlert() {
    var alertElement = document.getElementById("messages");
    if (alertElement) {
        alertElement.parentNode.removeChild(alertElement);
    }
}


document.addEventListener("DOMContentLoaded", function () {
    setTimeout(removeAlert, 2000);
});


let searchForm = document.getElementById('searchForm')
let pageLink = document.getElementsByClassName('page-link')

if(searchForm){
    for(let i=0; pageLink.length > i; i++){
        pageLink[i].addEventListener('click',function(e){
            e.preventDefault()
            
            let page = this.dataset.page
            
            searchForm.innerHTML += `<input value=${page} name="page" hidden />`
            
            searchForm.submit()
        })
    }
}
