document.addEventListener('DOMContentLoaded', function() {
    const toggle = document.getElementById('toggle');

    const elementsToColor = document.querySelectorAll('.color-changing-element');

    const dark_mode_bg_color = "#010119";
    const dark_mode_div_bg = "#030326";
    const blue_color = "#1919DD"; //what is its use???
    const slight_grey_color = "#EFF0ED";
    const white_color = "#fff";

    toggle.addEventListener('change', () => {
        if (toggle.checked) {
            elementsToColor.forEach(element => {
                element.style.color = slight_grey_color;
                element.style.backgroundColor = dark_mode_div_bg; // Change background color for example
            });

        } else {
            elementsToColor.forEach(element => {
                element.style.color = dark_mode_bg_color;
                element.style.backgroundColor = white_color; // Change background color for example
            });
        }
    });
});