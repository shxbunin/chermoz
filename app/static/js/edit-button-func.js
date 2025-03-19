function toggleEditing() {
  const desc = document.getElementById('desc');
  const descEdit = document.getElementById('desc-edit');
  const textarea = descEdit.querySelector('textarea');
  const editButton = document.getElementById('editButton');

  if (editButton.innerText === 'Редактировать') {
    descEdit.value = desc.innerText.trim();
    desc.style.display = 'none';
    descEdit.style.display = 'block';
    editButton.innerText = 'Сохранить';
  } else {
    const newText = textarea.value
    console.log(newText +  " aboba")
    editDesc(editButton, newText)
    desc.innerText = newText;
    desc.style.display = 'block';
    descEdit.style.display = 'none';
    editButton.innerText = 'Редактировать';
  }
}
document.getElementById('editButton').onclick = toggleEditing;


async function editDesc(btn, desc) {
  const photoId = btn.dataset.photoId;

  try {
    const res = await fetch('/edit_desc', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ id: photoId, desc: desc})
    });

    const { status, result } = await res.json();
    console.log('Ответ сервера:', status, result);
  } catch (err) {
    console.error('Ошибка отправки:', err);
  }
}