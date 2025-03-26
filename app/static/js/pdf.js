pdfjsLib.GlobalWorkerOptions.workerSrc = 'pdf.worker.js';
const pdfUrl = document.getElementById('pdf').innerHTML;
console.log(pdfUrl);


pdfjsLib.getDocument(pdfUrl).promise.then(function(pdf) {
    const container = document.getElementById('pdf-container');

    for (let pageNumber = 1; pageNumber <= pdf.numPages; pageNumber++) {
        const pageDiv = document.createElement('div');
        pageDiv.id = 'page-' + pageNumber; 
        container.appendChild(pageDiv);
    }
    
    for (let pageNumber = 1; pageNumber <= pdf.numPages; pageNumber++) {
        pdf.getPage(pageNumber).then(function(page) {
            const scale = 1.5;
            const viewport = page.getViewport({ scale: scale });
            const canvas = document.createElement('canvas');
            const context = canvas.getContext('2d');

            canvas.width = viewport.width;
            canvas.height = viewport.height;

            const renderContext = {
                canvasContext: context,
                viewport: viewport
            };

            page.render(renderContext).promise.then(function() {
                const pageDiv = document.getElementById('page-' + pageNumber);
                pageDiv.appendChild(canvas);
            });
        });
    }
}).catch(function(error) {
    console.error('Ошибка при загрузке/отрисовке PDF: ', error);
});