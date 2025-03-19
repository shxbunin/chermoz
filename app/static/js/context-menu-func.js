async function changeCover(btn) {
  const photoId = btn.dataset.photoId;

  try {
    const res = await fetch('/change_cover', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ id: photoId })
    });

    const { status, result } = await res.json();
    console.log('Ответ сервера:', status, result);
  } catch (err) {
    console.error('Ошибка отправки:', err);
  }
}

async function deletePhoto(btn) {
  const photoId = btn.dataset.photoId;

  try {
    const res = await fetch('/delete_photo', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ id: photoId })
    });

    const { status, result } = await res.json();
    console.log('Ответ сервера:', status, result);

    if (status === 'ok') {
      location.reload();
    }
  } catch (err) {
    console.error('Ошибка отправки:', err);
  }
}