import {realtyAreaFilters} from "../modules/nouislider/realty_area_filters"
import {realtyPriceFilters} from "../modules/nouislider/realty_price_filters"
import {realtyFloorFilters} from "../modules/nouislider/realty_floor_filters"


function removeItemByValFromArray(array_name, value) {
    let index = array_name.indexOf(value)
    if (index > -1) {
        array_name.splice(index, 1)
    }
}

// ???
// function constructFiltersSitesDefaultState() {
//     const api_objects_summary_info_url = $('form#facet-filters-sites').data('api-objects-summary-info')
//
//     $.getJSON(api_objects_summary_info_url, (data) => {
//         // console.log(data)
//
//         const objects_summary     = data[0]['objects_summary']
//         const rooms_qty           = data[1]['rooms_qty']
//         const objects             = data[2]['objects']
//         const objects_sections    = data[3]['objects_sections']
//         const cities              = data[4]['cities']
//         const years_of_completion = data[5]['years_of_completion']
//
//         // console.log(objects_summary)
//         // console.log(rooms_qty)
//
//         // rooms
//         let room_html = "";
//         $.each(rooms_qty, function(i, item) {
//             if ( item['room'] == 0 ) {
//                 room_html += '<button class="circle-site" data-value="' + item['room'] + '">Cт</button>'
//             } else if ( item['room'] < 5 ) {
//                 room_html += '<button class="circle-site" data-value="' + item['room'] + '">' + item['room'] + '</button>'
//             }
//         })
//         $('#section-realty-sites-filters__rooms-block .realty-filters-block__content').html(room_html)
//     })
// }


function facetFiltersSites() {
    realtyAreaFilters()
    realtyPriceFilters()
    realtyFloorFilters()

    // ???
    // constructFiltersSitesDefaultState()

    // Process GET request
    let urlParams = new URLSearchParams(window.location.search)
    let urlParams_rooms = urlParams.getAll('rooms')

    let rooms = []

    // active class for rooms buttons
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

    $('form#facet-filters-sites').submit(function(e) {
        e.preventDefault()

        const area_min_val = $('input[name="area_min"]').val()
        const area_max_val = $('input[name="area_max"]').val()

        const price_min_val = $('input[name="price_min"]').val()
        const price_max_val = $('input[name="price_max"]').val()

        const object_val = $('select[name="object"] option:selected').val()

        const floor_min_val = $('input[name="floor_min"]').val()
        const floor_max_val = $('input[name="floor_max"]').val()

        // Sorting rooms array to correct get sequence: /?rooms=0&rooms=1&rooms=2...
        rooms.sort()

        // Rooms
        let rooms_query = ''
        if (rooms.length > 0) {
            for (let i = 0; i < rooms.length; i++) {
                // Append ampersand in case rooms more than one in get request
                rooms_query += ((rooms_query.length == 0) ? '' : '&') + 'rooms=' + rooms[i]
            }
        }

        // Area
        let area_min = ''
        if (area_min_val.length > 0) {
            // remove ?& in search query /?&area_min=35&...
            area_min = ((rooms_query.length == 0) ? '' : '&') + 'area_min=' + area_min_val
        }

        let area_max = ''
        if (area_max_val.length > 0) {
            area_max = '&area_max=' + area_max_val
        }

        // Price
        let price_min = ''
        if (price_min_val.length > 0) {
            price_min = '&price_min=' + price_min_val
        }

        let price_max = ''
        if (price_max_val.length > 0) {
            price_max = '&price_max=' + price_max_val
        }

        // Object
        let object = ''
        if (object_val.length > 0) {
            object = '&object=' + object_val
        }

        // Floors
        let floor_min = ''
        if (floor_min_val.length > 0) {
            floor_min = '&floor_min=' + floor_min_val
        }

        let floor_max = ''
        if (floor_max_val.length > 0) {
            floor_max = '&floor_max=' + floor_max_val
        }

        // Search query by itself
        window.location.search = '?' + rooms_query + area_min + area_max + price_min + price_max + object + floor_min + floor_max

        // window.location.search = '?area_min=35&area_max=245&price_min=2919000&price_max=18360000&block-section=all&year=all&floor_min=1&floor_max=35'
    })
}


export {facetFiltersSites}
