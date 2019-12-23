import {realtySquareFilters} from "../modules/nouislider/realty_square_filters"
import {realtyPriceFilters} from "../modules/nouislider/realty_price_filters"
import {realtyFloorFilters} from "../modules/nouislider/realty_floor_filters"


function removeItemByValFromArray(array_name, value) {
    let index = array_name.indexOf(value)
    if (index > -1) {
        array_name.splice(index, 1)
    }
}


function facetFiltersSites() {
    realtySquareFilters()
    realtyPriceFilters()
    realtyFloorFilters()

    let urlParams = new URLSearchParams(window.location.search)
    let urlParams_rooms = urlParams.getAll('rooms')
    console.log(urlParams_rooms)

    let rooms = []

    $('#section-realty-sites-filters__rooms-block .realty-filters-block__content button').each(function(index, el) {
        let room_value = $(el).data('value')

        $(el).on('click', function(e) {
            e.preventDefault()
            // let room_value = $(el).data('value')
            if ( !$(el).hasClass('active') ) {
                $(el).addClass('active')
                // remove from array
                removeItemByValFromArray(rooms, room_value)
                rooms.push(room_value)
            } else {
                $(el).removeClass('active')
                // remove from array
                removeItemByValFromArray(rooms, room_value)
            }

            if ( $(el).hasClass('disabled') ) {
                $(el).removeClass('active')
            }
        })

        // Add .active class to rooms buttons
        if (urlParams_rooms.includes(room_value.toString())) {
            $(el).addClass('active')
        }

        // Add to rooms array valuest with active buttons
        if ( $(el).hasClass('active') ) {
            // remove from array
            removeItemByValFromArray(rooms, room_value)
            rooms.push(room_value)
        }
    })

    $('form#facet-filters-sites').on('click', function() {
        console.log(rooms.sort())
    })

    $('form#facet-filters-sites').submit(function(e) {
        e.preventDefault()

        rooms.sort()

        let rooms_query = ''
        if (rooms.length > 0) {
            for (let i = 0; i < rooms.length; i++) {
                if ( rooms_query.length == 0 ){
                    rooms_query += 'rooms='+rooms[i]
                } else {
                    rooms_query += '&rooms='+rooms[i]
                }
            }

            window.location.search = '?' + rooms_query + '&square_min='+$('input[name="square_min"]').val()+'&square_max=245&price_min=2919000&price_max=18360000&block-section=all&year=all&floor_min=1&floor_max=35'
        } else {
            window.location.search = '?square_min='+$('input[name="square_min"]').val()+'&square_max=245&price_min=2919000&price_max=18360000&block-section=all&year=all&floor_min=1&floor_max=35'
        }

        // window.location.search += '&params=1&test=222'
        // window.location.search += '?' + (rooms_query.length > 0) ? rooms_query : ''

        // window.location.search += '?square_min='+$('input[name="square_min"]').val()+'&square_max=245&price_min=2919000&price_max=18360000&block-section=all&year=all&floor_min=1&floor_max=35'
    })
}


export {facetFiltersSites}
