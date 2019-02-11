import "./main.scss"

import "./boostrap/boostrap"

import {stickyMainNav, toggleMainNav} from "./menu/main-nav"

// Realty filters
import {realtySquareFilters} from "./nouislider/realty_square_filters"
import {realtyPriceFilters} from "./nouislider/realty_price_filters"
import {realtyFloorFilters} from "./nouislider/realty_floor_filters"

import {familyFiltersToggle} from "./filters/family-filters-toggle"


$(document).ready(function() {
    toggleMainNav()

    // homepage
    if ( $('#section-realty-homepage-filters').length ) {
        realtySquareFilters()
        realtyPriceFilters()
    }
    // flats
    if ( $('#section-realty-flats-filters').length ) {
        realtySquareFilters()
        realtyPriceFilters()
        realtyFloorFilters()
    }

    familyFiltersToggle()

})


$(window).scroll(function() {
    stickyMainNav()
})
