const burgerBtn = document.querySelector('.burger');
const sidebar = document.querySelector('.sidebar_item')

burgerBtn.addEventListener('click', function(event){
    event.preventDefault();

    sidebar.classList.toggle('active');
    burgerBtn.classList.toggle('active');

})