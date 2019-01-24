// noUiSlider for realty square filter in homepage
// https://refreshless.com/nouislider/examples/#section-html5
function realtySquareSlider() {
    const realtySquareSlider = document.getElementById('realty-filters__square-slider');

    noUiSlider.create(realtySquareSlider, {
        start: [35, 245],
        connect: true,
        range: {
            'min': 35,
            'max': 245
        }
    });

    const inputNumberMin = document.getElementById('square-slider--input-min');
    const inputNumberMax = document.getElementById('square-slider--input-max');

    realtySquareSlider.noUiSlider.on('update', function (values, handle) {
        let value = values[handle];

        if (handle) {
            inputNumberMax.value = Math.round(value)
        } else {
            inputNumberMin.value = Math.round(value)
        }
    });

    inputNumberMin.addEventListener('change', function () {
        realtySquareSlider.noUiSlider.set([this.value, null]);
    });
    inputNumberMax.addEventListener('change', function () {
        realtySquareSlider.noUiSlider.set([null, this.value]);
    });
}


export {realtySquareSlider};
