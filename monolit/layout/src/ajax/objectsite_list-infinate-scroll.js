$.fn.isInViewport = function() {
    var elementTop = $(this).offset().top
    var elementBottom = elementTop + $(this).outerHeight()

    var viewportTop = $(window).scrollTop()
    var viewportBottom = viewportTop + $(window).height()

    return elementBottom > viewportTop && elementTop < viewportBottom
}


function objectsite_list_Infinate_scroll() {
    // console.clear()

    // if last .flat-card in viewport
    if ( $('.flat-card').last().isInViewport() ) {
        console.log('in viewport')

        // let next_page_url = $('#section-flats-list').data('next-pagination-url')
        //
        // $.ajax({
        //     url: next_page_url,
        //     type: 'GET',
        //     success: (data) => {
        //         console.log(next_page_url)
        //         $('#section-flats-list__inner').append( $(data).find('#section-flats-list__inner').html() )
        //     }
        // })

    } else {
        console.log('NOT in viewport')
    }
}


export {objectsite_list_Infinate_scroll}
