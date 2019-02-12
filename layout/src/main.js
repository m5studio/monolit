import "./main.scss"

import "./boostrap/boostrap"

import {stickyMainNav, toggleMainNav} from "./menu/main-nav"

// Realty filters
import {realtySquareFilters} from "./nouislider/realty_square_filters"
import {realtyPriceFilters} from "./nouislider/realty_price_filters"
import {realtyFloorFilters} from "./nouislider/realty_floor_filters"

import {familyFiltersToggle} from "./filters/family-filters-toggle"

// Scroll to Top
import {scrollToTop} from "./scroll-to-top/scroll-to-top"

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
    scrollToTop()
})


$(window).scroll(function() {
    stickyMainNav()
})
