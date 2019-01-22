function stickyMainNav() {
    let pxFromTop = $(document).scrollTop()
    const mainNav = $("#header__bottom")
    const stickyClass = 'sticky-main-nav'

    // 40 px from top
    if (pxFromTop >= 40) {
        mainNav.addClass(stickyClass)
    } else {
        mainNav.removeClass(stickyClass)
    }
}

export {stickyMainNav}
