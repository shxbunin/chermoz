// WeakMap теперь хранит объект с двумя таймерами
const hideTimers = new WeakMap();

function scheduleHide(btn, menu) {
  clearHide(menu);

  const menuTimer = setTimeout(() => {
    menu.classList.remove('show');
  }, 1000);

  const btnTimer = setTimeout(() => {
    btn.classList.remove('show');
  }, 1150);

  hideTimers.set(menu, { menuTimer, btnTimer });
}

function clearHide(menu) {
  const timers = hideTimers.get(menu);
  if (timers) {
    clearTimeout(timers.menuTimer);
    clearTimeout(timers.btnTimer);
    hideTimers.delete(menu);
  }
}


document.addEventListener('click', e => {
  const moreBtn = e.target.closest('.more-btn');
  const actionBtn = e.target.closest('.context-menu button');

  if (moreBtn) {
    e.preventDefault();
    e.stopPropagation();

    const menu = moreBtn.nextElementSibling;
    const isOpen = menu.classList.toggle('show');
    moreBtn.classList.toggle('show', isOpen);

    if (isOpen) scheduleHide(moreBtn, menu);
    else clearHide(menu);
    return;
  }

  if (actionBtn) {
    e.preventDefault();
    e.stopPropagation();

    const menu = actionBtn.closest('.context-menu');
    const btn = menu.previousElementSibling;
    btn.classList.remove('show');
    menu.classList.remove('show');
    clearHide(menu);
    return;
  }

  // Клик вне меню — закрываем все открытые
  document.querySelectorAll('.context-menu.show').forEach(menu => {
    const btn = menu.previousElementSibling;
    btn.classList.remove('show');
    menu.classList.remove('show');
    clearHide(menu);
  });
});

document.addEventListener('mouseover', e => {
  const menu = e.target.closest('.context-menu.show');
  if (menu) clearHide(menu);
});

document.addEventListener('mouseout', e => {
  const menu = e.target.closest('.context-menu.show');
  if (menu && !e.relatedTarget?.closest('.context-menu')) {
    const btn = menu.previousElementSibling;
    scheduleHide(btn, menu);
  }
});
