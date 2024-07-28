document.addEventListener('DOMContentLoaded', function () {
    const generalBtn = document.querySelector('button[data-content="general"]');
    generalBtn.classList.add('active');

    showContent('general');
});

function showContent(contentId) {
    // Hide all content
    const contents = document.querySelectorAll('.content');
    contents.forEach(content => {
        content.style.display = 'none';
    });

    // Show the selected content
    const selectedContent = document.getElementById(contentId);
    selectedContent.style.display = 'block';

    const buttons = document.querySelectorAll('.btn');
    buttons.forEach(button => {
        button.classList.remove('active');
    });
    const selectedButton = document.querySelector(`button[data-content="${contentId}"]`);
    selectedButton.classList.add('active');
}
