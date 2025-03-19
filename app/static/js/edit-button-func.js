function toggleEditing() {
    const desc = document.getElementById('desc');
    const descEdit = document.getElementById('desc-edit');
    const editButton = document.getElementById('editButton');
    const textarea = document.getElementById('desc-textarea');

    if (desc.style.display === 'block') {
        desc.style.display = 'none';
        descEdit.style.display = 'block';
        editButton.innerText = 'Сохранить';

    autoResize(textarea);

    } else {
        const newText = textarea.value
        editDesc(editButton, newText)
        desc.innerText = newText;
        desc.style.display = 'block';
        descEdit.style.display = 'none';
        editButton.innerText = 'Редактировать';
    }
}

function autoResize(el) {
    el.style.height = 'auto';
    el.style.height = el.scrollHeight + 10 + 'px';
}

const textarea = document.getElementById('desc-textarea');

textarea.addEventListener('input', () => { autoResize(textarea); });

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

document.getElementById('editButton').onclick = toggleEditing;