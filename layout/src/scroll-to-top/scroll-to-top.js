function scrollToTop() {
    const scrollToTopName = 'scroll-to-top'
    const scrollToTopId = '#'+scrollToTopName

    const pxFromTop = 500

    $('#footer').append('<div id="'+scrollToTopName+'">Наверх страницы</div>')
    $(scrollToTopId).hide()

    $(scrollToTopId).click(() => {
        $('html, body').animate({scrollTop: 0}, 600)
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
