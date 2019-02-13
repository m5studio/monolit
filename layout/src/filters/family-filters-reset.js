function familyFiltersReset() {
    const realtyFiltersId = '#section-realty-flats-filters'

    const filtersResetName = 'filter-realty-flats-reset'
    const filtersResetId = '#' + filtersResetName

    if ( $(realtyFiltersId).length ) {
        $(realtyFiltersId).prepend('<div id="'+filtersResetName+'"><a href=""><div class="icon icon-14 icon-cross-green"></div> Сбросить фильтры</a></div>')
        $(filtersResetId).hide()
    }

    $(realtyFiltersId).on('click', () => {
        if ( $(filtersResetId).length ) {
            $(filtersResetId).fadeIn('slow')
        }
    })
}

export {familyFiltersReset}
