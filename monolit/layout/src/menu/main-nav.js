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

    const opened_class = 'opened'
    const body_overflow_class = 'body-overflow-hidden'

    menuToggle.click(function() {
        if (mainNav.hasClass(opened_class)) {
            $('body').removeClass(body_overflow_class)
            $(this).removeClass(opened_class)
            mainNav.removeClass(opened_class)
            menuToggle.removeClass(opened_class)
        } else {
            $('body').addClass(body_overflow_class) // prevent background scroll
            $(this).addClass(opened_class)
            mainNav.addClass(opened_class)
            menuToggle.addClass(opened_class)
        }
    })
}


export {stickyMainNav, toggleMainNav}
