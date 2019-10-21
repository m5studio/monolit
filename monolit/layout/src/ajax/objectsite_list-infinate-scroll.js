$.fn.isInViewport = function() {
    var elementTop = $(this).offset().top
    var elementBottom = elementTop + $(this).outerHeight()

    var viewportTop = $(window).scrollTop()
    var viewportBottom = viewportTop + $(window).height()

    return elementBottom > viewportTop && elementTop < viewportBottom
}


function getFlats(page_number) {
    let page_url = $('#section-flats-list').data('page-url')

    $.ajax({
        url: page_url + '?page=' + page_number.toString(),
        type: 'GET',
        success: (data) => {
            $('#section-flats-list__inner').append( $(data).find('#section-flats-list__inner').html() )
            // $('#section-flats-list__inner').append( $(data).find('#section-flats-list__inner').html() ).hide().fadeIn(2000)

            // Count .flat-card
            // console.log( ".flat-card quantity = " + $(data).find('.flat-card').length )
        }
    })
}


let current_pagination_number = parseInt($('#section-flats-list').data('current-pagination-number'), 10)
const max_pagination_number = parseInt($('#section-flats-list').data('max-pagination-number'), 10)

let working = false

function objectsite_list_infinate_scroll() {
    console.clear()
    console.log('objectsite_list_infinate_scroll')
    console.log('current_pagination_number ' + current_pagination_number)

    // if scrolled to page bottom
    // if scrolled little bit upper than very bottom
    // if ( $(window).scrollTop() + 1 >= $('body').height() - $(window).height() ) {

    // if #footer in viewport
    if ( $('#footer').isInViewport() ) {
        if ( current_pagination_number < max_pagination_number ) {
            if ( working == false ) {
                working = true

                current_pagination_number++
                console.log(current_pagination_number)
                getFlats(current_pagination_number)

                // Timeout before call
                setTimeout(function(){
                    working = false
                }, 1000)
            }
        }
    }
}


export {objectsite_list_infinate_scroll}
