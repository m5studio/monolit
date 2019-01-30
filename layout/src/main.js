import "./main.scss"

import "./boostrap/boostrap"

import {realtySquareFilters} from "./nouislider/realty_square_filters"
import {realtyPriceFilters} from "./nouislider/realty_price_filters"

import {stickyMainNav} from "./core/main_nav/main_nav"


$(document).ready(function() {
    realtySquareFilters()
    realtyPriceFilters()
})


$(window).scroll(function() {
    stickyMainNav()
})
