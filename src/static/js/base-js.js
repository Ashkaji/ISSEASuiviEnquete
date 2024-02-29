document.addEventListener('DOMContentLoaded', function() {
    const dark_mode_bg_color = "#010119";
    const slight_grey_color = "#EFF0ED";

    const toggle = document.getElementById('toggle');
    const tagElementsToColor = document.querySelectorAll('.tag-color-changing');

    toggle.addEventListener('change', () => {
        if (toggle.checked) {
            document.body.style.backgroundColor = dark_mode_bg_color;
            document.body.style.color = slight_grey_color;

            tagElementsToColor.forEach(element => {
                element.style.color = slight_grey_color;
                element.style.backgroundColor = dark_mode_bg_color; // Change background color for example
            });
        } else {
            document.body.style.backgroundColor = slight_grey_color;
            document.body.style.color = dark_mode_bg_color;

            tagElementsToColor.forEach(element => {
                element.style.color = dark_mode_bg_color;
                element.style.backgroundColor = slight_grey_color; // Change background color for example
            });
        }
    });

    function toggleMenu() {
        const navLinks = document.getElementById("navLinks");
        navLinks.classList.toggle("active");
    }
});
