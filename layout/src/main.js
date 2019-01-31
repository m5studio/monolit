import "./main.scss"

import "./boostrap/boostrap"

import {stickyMainNav, toggleMainNav} from "./core/main_nav/main_nav"

import {realtySquareFilters} from "./nouislider/realty_square_filters"
import {realtyPriceFilters} from "./nouislider/realty_price_filters"


$(document).ready(function() {
    toggleMainNav()

    realtySquareFilters()
    realtyPriceFilters()
})


$(window).scroll(function() {
    stickyMainNav()
})
