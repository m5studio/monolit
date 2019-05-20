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


    // Get object gallery images from json
    $('select[name=gallery_id]').change(function() {
        let selected_val = $("option:selected", this).val()
        $('#bp-and-news-pills-building-progress__inner').empty()

        $.getJSON('http://127.0.0.1:8000/object-gal/'+selected_val+'/', function(data) {
            $.each(data, function(i, val) {
                $('#bp-and-news-pills-building-progress__inner').append('<a data-fancybox="bp-gallery" data-caption="" class="bp-card" href="/media/'+val.image+'" style="background-image: url(/media/'+val.image+');"><div class="bp-card__date">28 сентября 2018</div></a>')
            })
        })
    })

})


$(window).scroll(function() {
    stickyMainNav()
})
