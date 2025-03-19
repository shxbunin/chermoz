const path = window.location.pathname;
const segments = path.split('/');
const id = segments[segments.length - 1];

const addPhotoButtons = document.querySelectorAll('.gallery-item.first');
const addPhotoPopup = document.getElementById('add-photo-popup');
const albumInput = document.querySelector('input[name="album_id"]');
const addPhotoSectionInput = document.querySelector('input[name="section_id1"]');

const addAlbumButton = document.querySelector('.add-button');
const addAlbumSectionInput = document.querySelector('input[name="section_id2"]');
const addAlbumPopup = document.getElementById('add-album-popup');

addPhotoButtons.forEach((firstItem) => {
    firstItem.addEventListener('click', () => {
        const scrollbarWidth = getScrollbarWidth();
        console.log(scrollbarWidth)
        albumInput.value = firstItem.getAttribute('data-album-id');
        addPhotoSectionInput.value = id;
        addPhotoPopup.classList.add('open');
        document.body.classList.add('no-scroll');

        document.body.style.paddingRight = `${scrollbarWidth}px`;
        nav.style.paddingRight = `${scrollbarWidth}px`;
    });
});

document.getElementById('popup-form1').addEventListener('submit', router);

addAlbumButton.addEventListener('click', () => {
    const scrollbarWidth = getScrollbarWidth();
    addAlbumSectionInput.value = id;
    addAlbumPopup.classList.add('open');
    document.body.classList.add('no-scroll');

    document.body.style.paddingRight = `${scrollbarWidth}px`;
    nav.style.paddingRight = `${scrollbarWidth}px`;
});

document.getElementById('popup-form2').addEventListener('submit', router);

addPhotoPopup.addEventListener('click', (event) => {
    if (!event.target.closest('.popup-content')) {
        addPhotoPopup.classList.remove('open');
        document.body.classList.remove('no-scroll');

        document.body.style.paddingRight = "";
        nav.style.paddingRight = "";
    }
});

addAlbumPopup.addEventListener('click', (event) => {
    if (!event.target.closest('.popup-content')) {
        addAlbumPopup.classList.remove('open');
        document.body.classList.remove('no-scroll');

        document.body.style.paddingRight = "";
        nav.style.paddingRight = "";
    }
});