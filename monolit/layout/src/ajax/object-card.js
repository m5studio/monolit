function formaThousands(number, precision=0) {
    number = parseFloat(number).toFixed(precision)
    // Cure NaN issue
    if (isNaN(number)) {
        number = ''
    }
    return number.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ' ')
}

// function flatSingularPlural(number) {
//     number = parseInt(number, 10)
//     let ending = ''
//
//     if (number === 1) {
//         ending = 'квартира'
//     } else if (number >= 2 && number <= 4 || number >= 22 && number <= 24 || number >= 32 && number <= 34) {
//         ending = 'квартиры'
//     } else if (number >= 5 && number <= 20) {
//         ending = 'квартир'
//     }
//     return number.toString() + ' ' + ending
// }


function singularPlural(n, text_list, show_number=false) {
    // n = parseInt(n, 10)
    n = Math.abs(n) % 100
    let n1 = n % 10

    if (n > 10 && n < 20) {
        if (show_number) {
            return n + ' ' + text_list[2]
        } else {
            return text_list[2]
        }
    }
    if (n1 > 1 && n1 < 5) {
        if (show_number) {
            return n + ' ' + text_list[1]
        } else {
            return text_list[1]
        }
    }
    if (n1 == 1) {
        if (show_number) {
            return n + ' ' + text_list[0]
        } else {
            return text_list[0]
        }
    }
    if (show_number) {
        return n + ' ' + text_list[2]
    } else {
        return text_list[2]
    }
}

// const n=251
// console.log( n + ' ' + num2str(n, ['квартира', 'квартиры', 'квартир']) )
//
// const y=467
// console.log( y + ' ' + num2str(y, ['квартира', 'квартиры', 'квартир']) )
//
// const x=982
// console.log( x + ' ' + num2str(x, ['квартира', 'квартиры', 'квартир']) )



function objectCardSitesInfo() {
    $('.object-card').each((index, el) => {
        let site_info_url = $(el).data('sites-info-url')

        $.getJSON(site_info_url, (data) => {
            $.each(data, (index, val) => {
                // Кол-во квартир
                if ( val['object_total_sites_qty'] > 0 ) {
                    $(el).find('.object-card__flat--count').append(
                        '<a href="">' +
                            // '<span class="oc-flats-total-qty">' + val['object_total_sites_qty'] + '</span>' +
                            '<span class="oc-flats-total-qty">' + singularPlural(val['object_total_sites_qty'], ['квартира', 'квартиры', 'квартир'], true) + '</span>' +
                        '</a>'
                    )
                }

                // Площадь от - до
                if ( val['object_min_site_area'] && val['object_max_site_area'] ) {
                    $(el).find('.object-card__features').append(
                        '<div class="object-card__features--block oc-flats-min-max-area--block">' +
                            '<div class="object-card__features--name">Площадь</div>' +
                            '<div class="object-card__features--value">' +
                                '<span class="oc-flats-area-min">от ' + formaThousands(val['object_min_site_area'], 1) + '</span>' +
                                '<span class="oc-flats-area-max"> до ' + formaThousands(val['object_max_site_area'], 1) + ' м<sup>2</sup></span>' +
                            '</div>' +
                        '</div>'
                    )
                }

                // Минимальная стоимость
                if ( val['object_min_site_price'] ) {
                    $(el).find('.object-card__features').append(
                        '<div class="object-card__features--block oc-flats-min-price--block">' +
                            '<div class="object-card__features--name">Стоимость</div>' +
                            '<div class="object-card__features--value">' +
                                '<span class="oc-flats-min-price">от ' + formaThousands( val['object_min_site_price'].toString() ) + ' руб.</span>' +
                            '</div>' +
                        '</div>'
                    )
                }
            })

            $.each(data[1], (index, val) => {
                $.each(val, (i, v) => {
                    if ( v['flats_qty'] > 0 ) {
                        // Квартиры в .object-card__emerge-object
                        $(el).find('.object-card__emerge').append(
                            '<div class="object-card__emerge-object">' +
                                '<a href="" class="object-card__emerge-link">' +
                                    '<div class="object-card__flat-types-item">' + v['rooms'] + '</div>' +
                                    // '<div class="object-card__emerge-title">' + v['flats_qty'] + ' квартиры</div>' +
                                    '<div class="object-card__emerge-title">' + singularPlural(v['flats_qty'], ['квартира', 'квартиры', 'квартир'], true) + '</div>' +
                                    '<div class="object-card__emerge-area-space">' + formaThousands(v['min_area'], 1) + ' - ' + formaThousands(v['max_area'], 1) + ' м<sup>2</sup></div>' +
                                    '<div class="object-card__emerge-arrow"></div>' +
                                '</a>' +
                            '</div>'
                        )

                        $(el).find('.object-card__flat-types').append('<a href="" class="object-card__flat-types-item">' + v['rooms'] + '</a>')
                    }
                })
            })
        })
    })
}


export {objectCardSitesInfo}
