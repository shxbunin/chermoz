const photos = document.querySelectorAll('.photo img');
const overlay = document.getElementById('overlay');
const fullImage = document.getElementById('fullImage');
const desc = document.getElementById('imageDescription')
const nav = document.querySelector('.nav');

photos.forEach(photo => {
    photo.addEventListener('click', function() {
        const scrollbarWidth = getScrollbarWidth();

        fullImage.src = this.src;
        desc.textContent = this.getAttribute('data-description');
        overlay.classList.add('active');
        document.body.classList.add('no-scroll');
        document.body.style.overflow = 'hidden';

        nav.style.paddingRight = `${scrollbarWidth}px`;
        document.body.style.paddingRight = `${scrollbarWidth}px`;
    });
});

overlay.addEventListener('click', function() {
    overlay.classList.remove('active');
    document.body.classList.remove('no-scroll');

    nav.style.paddingRight = '';
    document.body.style.overflow = '';
    document.body.style.paddingRight = '';

    setTimeout(() => fullImage.src = '', 150); 
});