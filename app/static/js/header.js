const navMenuLoader = document.getElementById('nav-handler');
const body = document.querySelector('body');
const menuIcon = document.getElementById('menu-icon');
const menu = document.getElementById('more');

navMenuLoader.addEventListener('click', function() {
    if (menuIcon.src.endsWith('menu.svg')) {
        menu.classList.add('show');
        setTimeout(() => { menuIcon.src = "../static/images/x.svg"; }, 100); 
    } else {
        menu.classList.remove('show');
        menuIcon.src = "../static/images/menu.svg"; 
    }
});

body.addEventListener('click', function() {
    if (menuIcon.src.endsWith('x.svg')) {
        menu.classList.remove('show');
        menuIcon.src = "../static/images/menu.svg"; 
    } 
});




