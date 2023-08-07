document.addEventListener("DOMContentLoaded", function() {
    var footer = document.querySelector("footer");
    var scrollThreshold = 100; // Adjust this value as needed

    window.addEventListener("scroll", function() {
        var scrollPosition = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop;
        var windowHeight = window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight;
        var bodyHeight = Math.max(document.body.scrollHeight, document.documentElement.scrollHeight);

        if (scrollPosition + windowHeight >= bodyHeight - scrollThreshold) {
            footer.classList.add("show-footer");
        } else {
            footer.classList.remove("show-footer");
        }
    });
});