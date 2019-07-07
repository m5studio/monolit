function scrollToTop() {
    const scrollToTopName = 'scroll-to-top'
    const scrollToTopId = '#'+scrollToTopName
    const pxFromTop = 500

    if ( $(window).scrollTop() > pxFromTop ) {
        $('#footer').append('<div id="'+scrollToTopName+'">Наверх страницы</div>')
    } else {
        $(scrollToTopId).hide()
    }

    $(scrollToTopId).click(() => {
        $('html, body').animate({scrollTop: 0}, 500)
    })

    $(window).scroll(function() {
        if ( $(this).scrollTop() > pxFromTop ) {
            $(scrollToTopId).fadeIn()
        } else {
            $(scrollToTopId).fadeOut()
        }
    })
}


export {scrollToTop}
