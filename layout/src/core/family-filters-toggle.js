function familyFiltersToggle() {
    $('#section-family-types-filters__top').click(function() {
        $('#section-family-types-filters__inner').toggleClass('display-grid-family-filters')
    })
}

export {familyFiltersToggle}
