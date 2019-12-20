import {realtySquareFilters} from "../modules/nouislider/realty_square_filters"
import {realtyPriceFilters} from "../modules/nouislider/realty_price_filters"
import {realtyFloorFilters} from "../modules/nouislider/realty_floor_filters"


function facetFiltersSites() {
    realtySquareFilters()
    realtyPriceFilters()
    realtyFloorFilters()

    let urlParams = new URLSearchParams(window.location.search)
    // let rooms = ''

    $('#section-realty-sites-filters__rooms-block .realty-filters-block__content button').each(function(index, el) {
        $(el).on('click', function(e) {
            e.preventDefault()

            let room_value = $(el).data('value')

            if ( !$(el).hasClass('active') ) {
                $(el).addClass('active')

                // rooms += `&rooms=${room_value}`
                // urlParams.append('rooms', room_value)
            } else {
                $(el).removeClass('active')
            }

            if ( $(el).hasClass('disabled') ) {
                $(el).removeClass('active')
            }
        })
    })

    $("form#facet-filters-sites").submit(function(e) {
        // e.preventDefault()
        // window.location.search += "&my_field=foo&other_field=bar"

        // let url_rooms = urlParams.getAll('rooms')
        // url_rooms = ['']
        // window.location.search += rooms

        // urlParams.append('rooms', 222)
        // urlParams.set('rooms', '333')
    })
}


export {facetFiltersSites}
