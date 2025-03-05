// File upload preview
document.addEventListener('DOMContentLoaded', function() {
    const fileInput = document.getElementById('file');
    if (fileInput) {
        fileInput.addEventListener('change', function(e) {
            const fileName = e.target.files[0]?.name;
            if (fileName) {
                // You could add preview functionality here
                console.log('File selected:', fileName);
            }
        });
    }
});
