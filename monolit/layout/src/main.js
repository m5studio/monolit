import "./main.scss"
import "./bootstrap/bootstrap"

import {stickyMainNav, toggleMainNav} from "./menu/main-nav"

// Fiters
import {familyFiltersToggle} from "./filters/family-filters-toggle"
import {familyFiltersReset} from "./filters/family-filters-reset"

// Realty filters
import {realtySquareFilters} from "./modules/nouislider/realty_square_filters"
import {realtyPriceFilters} from "./modules/nouislider/realty_price_filters"
import {realtyFloorFilters} from "./modules/nouislider/realty_floor_filters"

// Scroll to Top
import {scrollToTop} from "./modules/scroll-to-top/scroll-to-top"

// Ajax
import {objectPageGalleries} from "./ajax/object-page-galleries"
import {objectPageDocsPagination} from "./ajax/object-page-documents-pagination"

// Fancybox https://fancyapps.com/fancybox/3/
import '@fancyapps/fancybox'


$(document).ready(function() {
    toggleMainNav()

    // Homepage
    if ( $('#section-realty-homepage-filters').length ) {
        realtySquareFilters()
        realtyPriceFilters()
    }

    // Flats
    if ( $('#section-realty-flats-filters').length ) {
        realtySquareFilters()
        realtyPriceFilters()
        realtyFloorFilters()
    }

    familyFiltersToggle()
    familyFiltersReset()

    scrollToTop()

    // Object page galleries ajax documents pagination
    if ( $('.object-page').length ) {
        objectPageGalleries()
        objectPageDocsPagination()
    }
    // END Object page galleries ajax documents pagination
})


$(document).ajaxStop(function() {
    // Object Documents Ajax pagination
    if ( $('.object-page').length ) {
        objectPageDocsPagination()
    }
    // END Object Documents Ajax pagination
})


$(window).scroll(function() {
    stickyMainNav()
})
