import "./main.scss"

import "./boostrap/boostrap"
import {realtySquareSlider} from "./nouislider/nouislider"
import {stickyMainNav} from "./core/main_nav/main_nav"


$(document).ready(function() {
    realtySquareSlider();
})


$(window).scroll(function() {
    stickyMainNav()
})
