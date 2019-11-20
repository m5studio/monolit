import {get_session_favorites} from "./favorites"


$.fn.isInViewport = function() {
    var elementTop = $(this).offset().top
    var elementBottom = elementTop + $(this).outerHeight()

    var viewportTop = $(window).scrollTop()
    var viewportBottom = viewportTop + $(window).height()

    return elementBottom > viewportTop && elementTop < viewportBottom
}


function getFlats(page_number) {
    let page_url = $('#section-sites-list').data('page-url')

    $.ajax({
        url: page_url + '?page=' + page_number.toString(),
        type: 'GET',
        success: (data) => {
            $('#section-sites-list__inner').append( $(data).find('#section-sites-list__inner').html() )

            // Run to display favorite icons for objects already in session after ajax request to load more object sites
            get_session_favorites()
        }
    })
}


let current_pagination_number = parseInt($('#section-sites-list').data('current-pagination-number'), 10)
const max_pagination_number = parseInt($('#section-sites-list').data('max-pagination-number'), 10)

let working = false

function objectsite_list_infinate_scroll() {
    // if #footer in viewport
    if ( $('#footer').isInViewport() ) {
        if ( current_pagination_number < max_pagination_number ) {
            if ( working == false ) {
                working = true

                current_pagination_number++
                getFlats(current_pagination_number)

                // Timeout before call
                setTimeout(function(){
                    working = false
                // }, 1000)
                }, 500)
            }
        }
    }
}


export {objectsite_list_infinate_scroll}
