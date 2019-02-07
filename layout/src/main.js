import "./main.scss"

import "./boostrap/boostrap"

import {stickyMainNav, toggleMainNav} from "./menu/main-nav"

import {realtySquareFilters} from "./nouislider/realty_square_filters"
import {realtyPriceFilters} from "./nouislider/realty_price_filters"

import {familyFiltersToggle} from "./core/family-filters-toggle"


$(document).ready(function() {
    toggleMainNav()

    if ( $('#section-realty-filters').length ) {
        realtySquareFilters()
        realtyPriceFilters()
    }

    familyFiltersToggle()

})


$(window).scroll(function() {
    stickyMainNav()
})


// $(document).mouseup(function(e) {
//
//     // Hide #section-family-types-filters__inner if click outside
//     const container = $('#section-family-types-filters__inner')
//     // if the target of the click isn't the container nor a descendant of the container
//     if (!container.is(e.target) && container.has(e.target).length === 0) {
//         // container.hide()
//         container.removeClass('display-grid-family-filters')
//     }
// })
