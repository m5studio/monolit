// noUiSlider for realty square filter in homepage
// https://refreshless.com/nouislider/examples/#section-html5

function realtyAreaFilters() {
    const realtySquareSlider = document.getElementById('realty-filter__area-slider')
    let urlParams = new URLSearchParams(window.location.search)

    noUiSlider.create(realtySquareSlider, {
        // start: [35, 245],
        start: (urlParams.has('area_min')) ? [urlParams.get('area_min'), urlParams.get('area_max')] : [35, 245],
        connect: true,
        range: {
            'min': 35,
            'max': 245
        }
    })

    const inputNumberMin = document.getElementById('realty-filter__area--input-min')
    const inputNumberMax = document.getElementById('realty-filter__area--input-max')

    realtySquareSlider.noUiSlider.on('update', function(values, handle) {
        let value = values[handle]

        if (handle) {
            inputNumberMax.value = Math.round(value)
        } else {
            inputNumberMin.value = Math.round(value)
        }
    })

    inputNumberMin.addEventListener('change', function() {
        realtySquareSlider.noUiSlider.set([this.value, null])
    })
    inputNumberMax.addEventListener('change', function() {
        realtySquareSlider.noUiSlider.set([null, this.value])
    })
}

export {realtyAreaFilters}
