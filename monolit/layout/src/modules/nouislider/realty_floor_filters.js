// noUiSlider for realty square filter in homepage
// https://refreshless.com/nouislider/examples/#section-html5

function realtyFloorFilters() {
    const realtyFloorSlider = document.getElementById('realty-filter__floor-slider')

    noUiSlider.create(realtyFloorSlider, {
        start: [1, 35],
        step: 1,
        connect: true,
        range: {
            'min': 1,
            'max': 35
        }
    })

    const inputNumberMin = document.getElementById('realty-filter__floor--input-min')
    const inputNumberMax = document.getElementById('realty-filter__floor--input-max')

    realtyFloorSlider.noUiSlider.on('update', function(values, handle) {
        let value = values[handle]

        if (handle) {
            inputNumberMax.value = Math.round(value)
        } else {
            inputNumberMin.value = Math.round(value)
        }
    })

    inputNumberMin.addEventListener('change', function() {
        realtyFloorSlider.noUiSlider.set([this.value, null])
    })
    inputNumberMax.addEventListener('change', function() {
        realtyFloorSlider.noUiSlider.set([null, this.value])
    })
}


export {realtyFloorFilters}
