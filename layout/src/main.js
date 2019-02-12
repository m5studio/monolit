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

    // TODO: reset filter btn
    if ( $('#section-realty-flats-filters').length ) {
        $('#section-realty-flats-filters').prepend('<div id="filter-reset-button"><button type="button" name="" class="green-button">Сбросить фильтры</button></div>')
        $('#filter-reset-button').hide()
    }

    $('#section-realty-flats-filters').on('click', () => {
        // if ( $('#filter-reset-button').length === 0 ) {
        if ( $('#filter-reset-button').length ) {
            $('#filter-reset-button').fadeIn('slow')
        }
    })
})


$(window).scroll(function() {
    stickyMainNav()
})
