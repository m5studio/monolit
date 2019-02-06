import "./main.scss"

import "./boostrap/boostrap"

import {stickyMainNav, toggleMainNav} from "./menu/main-nav"

import {realtySquareFilters} from "./nouislider/realty_square_filters"
import {realtyPriceFilters} from "./nouislider/realty_price_filters"


$(document).ready(function() {
    toggleMainNav()

    if ( $('#section-realty-filters').length ) {
        realtySquareFilters()
        realtyPriceFilters()
    }
})


$(window).scroll(function() {
    stickyMainNav()
})
