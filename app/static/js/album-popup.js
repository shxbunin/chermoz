const path = window.location.pathname;
const segments = path.split('/');
const id = segments[segments.length - 1];
const firstItems = document.querySelectorAll('.gallery-item.first');
const popup = document.getElementById('popup');
const albumInput = document.querySelector('input[name="album_id"]');
const sectionInput1 = document.querySelector('input[name="section_id1"]');
const add = document.querySelector('.add-button');
const sectionInput2 = document.querySelector('input[name="section_id2"]');
const popup2 = document.getElementById('popup2');
const nav = document.querySelector('.nav');

firstItems.forEach((firstItem) => {
    firstItem.addEventListener('click', () => {
        const scrollbarWidth = getScrollbarWidth();
        console.log(scrollbarWidth)
        albumInput.value = firstItem.getAttribute('data-album-id');
        sectionInput1.value = id;
        popup.classList.add('open');
        document.body.classList.add('no-scroll');
        document.body.style.paddingRight = `${scrollbarWidth}px`;
        nav.style.paddingRight = `${scrollbarWidth}px`;
    });
});

document.getElementById('popup-form1').addEventListener('submit', router);

add.addEventListener('click', () => {
    const scrollbarWidth = getScrollbarWidth();
    sectionInput2.value = id;
    popup2.classList.add('open');
    document.body.classList.add('no-scroll');
    document.body.style.paddingRight = `${scrollbarWidth}px`;
    nav.style.paddingRight = `${scrollbarWidth}px`;
});

document.getElementById('popup-form2').addEventListener('submit', router);

popup.addEventListener('click', (event) => {
    if (!event.target.closest('.popup-content')) {
        popup.classList.remove('open');
        document.body.classList.remove('no-scroll');
        document.body.style.paddingRight = "";
        nav.style.paddingRight = "";
    }
});

popup2.addEventListener('click', (event) => {
    if (!event.target.closest('.popup-content')) {
        popup2.classList.remove('open');
        document.body.classList.remove('no-scroll');
        document.body.style.paddingRight = "";
        nav.style.paddingRight = "";
    }
});

