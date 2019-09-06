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
// import {objectPageGalleries} from "./ajax/ajax-django"
import {newsPageLoadMoreNews} from "./ajax/news-page-load-more-news"
import {objectPageGalleries} from "./ajax/object-page-galleries"
import {objectPageDocsPagination} from "./ajax/object-page-documents-pagination"
import {objectCardSitesInfo} from "./ajax/object-card"
import {objectPageSitesInfo, objectPageFlatsTypes} from "./ajax/object_detail/object-page-sites-info"
import {mortgageOfferMonthlyPayment} from "./ajax/objectsite_detail/mortgage-offer-monthly-payment-calculate"
import {search_by_site_id} from "./ajax/search_by_site_id"
import {companyTendersPagePagination} from "./ajax/company-tenders-page-tenders-pagination"


// Fancybox https://fancyapps.com/fancybox/3/
import '@fancyapps/fancybox'


$(document).ready(function() {

    toggleMainNav()
    stickyMainNav()

    // Search by site id
    search_by_site_id()

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

    // Object page
    if ( $('.object-page').length ) {
        objectPageSitesInfo()
        objectPageFlatsTypes()
        objectPageGalleries()
        objectPageDocsPagination()
    }
    // END Object page

    // News page
    if ( $('.news').length ) {
        newsPageLoadMoreNews()
    }
    // END News page

    // Flat page
    if ( $('.flat-page').length ) {
        mortgageOfferMonthlyPayment()
    }
    // END Flat page

    // Get object-card sites info
    if ( $('.object-card').length ) {
        objectCardSitesInfo()
    }
    // END Get object-card sites info

    // Company Tenders page
    if ( $('.company-tenders').length ) {
        companyTendersPagePagination()
    }
    // END Company Tenders page
})


$(document).ajaxStop(function() {
    // Object Documents Ajax pagination
    if ( $('.object-page').length ) {
        objectPageDocsPagination()
    }
    // END Object Documents Ajax pagination

    // Company Tenders page
    if ( $('.company-tenders').length ) {
        companyTendersPagePagination()
    }
    // END Company Tenders page

    // News page Load more news...
    if ( $('.news').length ) {
        newsPageLoadMoreNews()
    }
    // END News page Load more news...
})


$(window).scroll(function() {
    stickyMainNav()
})
