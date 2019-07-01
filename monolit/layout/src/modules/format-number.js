function formatNumber(number, precision=0) {
    number = parseFloat(number).toFixed(precision)
    // Fix NaN issue
    if (isNaN(number)) {
        number = ''
    }
    return number.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ' ')
}


export {formatNumber}
