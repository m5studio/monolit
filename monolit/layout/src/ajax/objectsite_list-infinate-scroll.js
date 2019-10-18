// $.fn.isInViewport = function() {
//     let elementTop = $(this).offset().top
//     let elementBottom = elementTop + $(this).outerHeight()
//
//     let viewportTop = $(window).scrollTop()
//     let viewportBottom = viewportTop + $(window).height()
//
//     return elementBottom > viewportTop && elementTop < viewportBottom
// }


function getFlats(mypage) {
    // let next_page_url = $('#section-flats-list').data('next-pagination-url')

    $.ajax({
        // url: mypage,
        // url: next_page_url,
        // url: '/sites/?page=2',
        url: '/sites/?page=' + mypage.toString(),
        type: 'GET',
        success: (data) => {
            // console.log(next_page_url)
            $('#section-flats-list__inner').append( $(data).find('#section-flats-list__inner').html() )

            // setTimeout(function() {
            //     active = false
            //     i = i++
            // }, 3000)
        }
    })
}


// let mypage = 1

let current_pagination_number = parseInt($('#section-flats-list').data('current-pagination-number'), 10)
const max_pagination_number = parseInt($('#section-flats-list').data('max-pagination-number'), 10)

function objectsite_list_infinate_scroll() {
    // console.clear()

    // if last .flat-card in viewport
    // if ( $('.flat-card').last().isInViewport() ) {
    //     console.log('in viewport')
    // } else {
    //     console.log('NOT in viewport')
    // }

    console.log('objectsite_list_infinate_scroll')

    // let current_pagination_number = parseInt($('#section-flats-list').data('current-pagination-number'), 10)
    // const max_pagination_number = parseInt($('#section-flats-list').data('max-pagination-number'), 10)

    // console.log(current_pagination_number)
    // console.log(max_pagination_number)

    if ( $(window).scrollTop() + 1 >= $('body').height() - $(window).height() ) {
        // mypage++
        // mypage = (mypage < max_pagination_number) ? mypage++ : max_pagination_number
        // mypage = (current_pagination_number <= max_pagination_number) ? current_pagination_number++ : "Juice"
        // console.log(mypage)

        // if ( mypage <= max_pagination_number ) {
        //     // console.log(mypage)
        //     mypage++
        //     getFlats(mypage)
        // }

        if ( current_pagination_number < max_pagination_number ) {
            current_pagination_number++
            getFlats(current_pagination_number)
            console.log(current_pagination_number)

            // TODO: setTimeout
            setTimeout(function(){
                console.log('set time out');
            }, 3000)
        }
    }
}


export {objectsite_list_infinate_scroll}
