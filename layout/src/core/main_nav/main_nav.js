function stickyMainNav() {
    let pxFromTop = $(document).scrollTop()
    const mainNav = $("#header__bottom")
    const stickyClass = 'sticky-main-nav'

    // 40px from top
    if (pxFromTop >= 40) {
        mainNav.addClass(stickyClass)
    } else {
        mainNav.removeClass(stickyClass)
    }
}


function toggleMainNav() {
    const mainNav = $('#main-navigation')
    const menuToggle = $('#main-navigationToggle')

    menuToggle.click(function() {
        if (mainNav.hasClass('opened')) {
            $('body').removeClass('body-overflow-hidden')
            $(this).removeClass('opened')
            mainNav.removeClass('opened')
            menuToggle.removeClass('opened')
        } else {
            $('body').addClass('body-overflow-hidden') // prevent background scroll
            $(this).addClass('opened')
            mainNav.addClass('opened')
            menuToggle.addClass('opened')
        }
    })
}

export {stickyMainNav, toggleMainNav}
