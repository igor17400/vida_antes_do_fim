const observer = new MutationObserver((mutations, obs) => {
    const heroContainer = document.querySelector(".hero-container");
    const navbar = document.querySelector(".navbar-custom");
    var currentPath = window.location.pathname;

    if (heroContainer && navbar) {
        window.addEventListener("scroll", function () {
            const heroBottom = heroContainer.getBoundingClientRect().bottom;
            console.log(heroBottom); // Debugging the value of heroBottom
            if (heroBottom < window.innerHeight * 0.1) { // Adjusting the threshold
                navbar.classList.add("navbar-active");
            } else {
                navbar.classList.remove("navbar-active");
            }
        });

        obs.disconnect(); // Stop observing once the elements are found
    } else if (navbar && currentPath !== '/') {
        navbar.classList.add("navbar-active");
    }
});

observer.observe(document, {
    childList: true,
    subtree: true
});
