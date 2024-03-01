document.addEventListener('DOMContentLoaded', function() {
    const toggle = document.getElementById('toggle');

    const elementsToColor = document.querySelectorAll('.color-changing-element');
    const tagElementsToColor = document.querySelectorAll('.tag-color-changing');

    const dark_mode_bg_color = "#010119";
    const dark_mode_div_bg = "#030326";
    const blue_color = "#1919DD";
    const slight_grey_color = "#EFF0ED";
    const white_color = "#fff";

    toggle.addEventListener('change', () => {
        if (toggle.checked) {

            document.body.style.backgroundColor = dark_mode_bg_color;
            document.body.style.color = slight_grey_color;

            tagElementsToColor.forEach(element => {
                element.style.color = slight_grey_color;
                element.style.backgroundColor = dark_mode_bg_color; // Change background color for example
            });

            elementsToColor.forEach(element => {
                element.style.color = slight_grey_color;
                element.style.backgroundColor = dark_mode_div_bg; // Change background color for example
            });

        } else {
            document.body.style.backgroundColor = slight_grey_color;
            document.body.style.color = dark_mode_bg_color;

            tagElementsToColor.forEach(element => {
                element.style.color = dark_mode_bg_color;
                element.style.backgroundColor = slight_grey_color; // Change background color for example
            });

            elementsToColor.forEach(element => {
                element.style.color = dark_mode_bg_color;
                element.style.backgroundColor = white_color; // Change background color for example
            });
        }
    });

    function toggleMenu() {
        const navLinks = document.getElementById("navLinks");
        navLinks.classList.toggle("active");
    }
});
