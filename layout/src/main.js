import "./main.scss"

import "./boostrap/boostrap"
import {stickyMainNav} from "./core/main_nav/main_nav"


$(document).ready(function() {
    // console.log("document ready function")
})


$(window).scroll(function() {
    stickyMainNav()
})
