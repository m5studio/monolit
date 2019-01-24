import "./main.scss"

import "./boostrap/boostrap"
import {stickyMainNav} from "./core/main_nav/main_nav"

import 'nouislider'


$(document).ready(function() {
    // console.log("document ready function")

    // Init test noUiSlider
    const realtySquareSlider = document.getElementById('realty-filter__square-slider');
    noUiSlider.create(realtySquareSlider, {
        start: [35, 245],
        connect: true,
        range: {
            'min': 35,
            'max': 245
        }
    });
})


$(window).scroll(function() {
    stickyMainNav()
})
