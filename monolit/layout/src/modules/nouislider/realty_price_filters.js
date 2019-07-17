// noUiSlider for realty square filter in homepage
// https://refreshless.com/nouislider/examples/#section-html5

function realtyPriceFilters() {
    const realtyPriceSlider = document.getElementById('realty-filter__price-slider')

    noUiSlider.create(realtyPriceSlider, {
        start: [2919000, 18360000],
        step: 1000,
        connect: true,
        range: {
            'min': 2919000,
            'max': 18360000
        }
    })

    const inputNumberMin = document.getElementById('realty-filter__price--input-min')
    const inputNumberMax = document.getElementById('realty-filter__price--input-max')

    realtyPriceSlider.noUiSlider.on('update', function(values, handle) {
        let value = values[handle]

        if (handle) {
            inputNumberMax.value = Math.round(value)
        } else {
            inputNumberMin.value = Math.round(value)
        }
    })

    inputNumberMin.addEventListener('change', function() {
        realtyPriceSlider.noUiSlider.set([this.value, null])
    })
    inputNumberMax.addEventListener('change', function() {
        realtyPriceSlider.noUiSlider.set([null, this.value])
    })
}


export {realtyPriceFilters}
