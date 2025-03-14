const firstItem = document.querySelector('.first');
const popup = document.getElementById('popup');
const nav = document.querySelector('.nav');
        
const getScrollbarWidth = () => {
    const scrollDiv = document.createElement('div');
    scrollDiv.style.width = '100px';
    scrollDiv.style.height = '100px';
    scrollDiv.style.overflowY = 'scroll';
    scrollDiv.style.position = 'absolute';
    scrollDiv.style.top = '-9999px';
    document.body.appendChild(scrollDiv);
    const scrollbarWidth = scrollDiv.offsetWidth - scrollDiv.clientWidth;
    document.body.removeChild(scrollDiv);
    return scrollbarWidth;
};

document.getElementById('popup-form').addEventListener('submit', router);

firstItem.addEventListener('click', () => {
    const scrollbarWidth = getScrollbarWidth();
    popup.classList.add('open');
    document.body.classList.add('no-scroll');
    document.body.style.paddingRight = `${scrollbarWidth}px`;
    nav.style.paddingRight = `${scrollbarWidth}px`;
});
      
popup.addEventListener('click', (event) => {
    if (!event.target.closest('.popup-content')) {
        popup.classList.remove('open');
        document.body.classList.remove('no-scroll');
        document.body.style.paddingRight = "";
        nav.style.paddingRight = "";
    }
});