import "./main.scss"

import "./boostrap/boostrap"
import {stickyMainNav} from "./core/main_nav/main_nav"

// import 'nouislider'


$(document).ready(function() {
    // console.log("document ready function")

    // Init test noUiSlider
    // const squareSlider = document.getElementById('square-slider');
    // noUiSlider.create(squareSlider, {
    //     start: [20, 80],
    //     connect: true,
    //     range: {
    //         'min': 0,
    //         'max': 100
    //     }
    // });
})


$(window).scroll(function() {
    stickyMainNav()
})
