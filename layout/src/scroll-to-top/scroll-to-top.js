function scrollToTop() {
    $('#footer').append('<div id="scroll-to-top">Наверх страницы</div>')

    $('#scroll-to-top').click(() => {
        $('html, body').animate({scrollTop: 0}, 800)
    })

    $(window).scroll(function() {
    // $(window).scroll(() => {
        console.log( $(window).scrollTop() )
        // console.log( $(this).scrollTop() )
    })
}

export {scrollToTop}
