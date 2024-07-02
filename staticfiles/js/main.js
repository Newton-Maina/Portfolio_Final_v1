window.addEventListener("scroll", function() {
    const navbar = document.getElementById("main-navbar");
    const scrollPosition = window.scrollY || document.documentElement.scrollTop;

    if (scrollPosition > 100 && !navbar.classList.contains("sticky-top")) {
        navbar.classList.add("sticky-top");
    } else if (scrollPosition <= 100 && navbar.classList.contains("sticky-top")) {
        navbar.classList.remove("sticky-top");
    }
});

document.addEventListener("DOMContentLoaded", function() {
    var button = document.querySelector('.button.back-to-top'); // Adjusted selector to match CSS class

    window.addEventListener('scroll', function() {
        if (window.scrollY > 200) {
            button.classList.add('show');
        } else {
            button.classList.remove('show');
        }
    });

    button.addEventListener('click', function(e) {
        e.preventDefault(); // Prevent default anchor behavior
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
});

