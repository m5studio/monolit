function formaThousands(number, precision=0) {
    number = parseFloat(number).toFixed(precision)
    // Cure NaN issue
    if (isNaN(number)) {
        number = ''
    }
    return number.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ' ')
}


function objectCardSitesInfo() {
    $('.object-card').each((index, el) => {
        let site_info_url = $(el).data('sites-info-url')

        $.getJSON(site_info_url, (data) => {
            $.each(data, (index, val) => {
                if ( val['object_total_sites_qty'] === 0 ) {
                    $(el).addClass('nothing')
                    $(el).find('.object-card__features').html('нет в продаже')
                }

                if ( val['object_total_sites_qty'] > 0 ) {
                    // let flats_qty_text = () => {
                    //     if ( val['object_total_sites_qty'] === 1) {
                    //         return val['object_total_sites_qty'] + ' квартира'
                    //     } else if ( val['object_total_sites_qty'] > 1 && val['object_total_sites_qty'] < 5 ) {
                    //         return val['object_total_sites_qty'] + ' квартиры'
                    //     } else {
                    //         return val['object_total_sites_qty'] + ' квартир'
                    //     }
                    // }

                    // $(el).find('.oc-flats-total-qty').text( flats_qty_text() )

                    $(el).find('.object-card__flat--count').append(
                        '<a href="">' +
                            '<span class="oc-flats-total-qty">' + val['object_total_sites_qty'] + ' квартир</span>' +
                        '</a>'
                    )

                    // $(el).find('.object-card__footer').append(
                    //     '<a href="" class="object-card__footer-btn object-card__footer-btn--dark object-card__footer-btn--choose-flat">Выбрать квартиру</a>'
                    // )
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
                        $(el).find('.object-card__emerge').append(
                            '<div class="object-card__emerge-object">' +
                                '<a href="" class="object-card__emerge-link">' +
                                    '<div class="object-card__flat-types-item">'+v['rooms']+'</div>' +
                                    '<div class="object-card__emerge-title">'+v['flats_qty']+' квартиры</div>' +
                                    '<div class="object-card__emerge-area-space">'+formaThousands(v['min_area'], 1)+' - '+formaThousands(v['max_area'], 1)+' м<sup>2</sup></div>' +
                                    '<div class="object-card__emerge-arrow"></div>' +
                                '</a>' +
                            '</div>'
                        )

                        $(el).find('.object-card__flat-types').append('<a href="" class="object-card__flat-types-item">'+v['rooms']+'</a>')
                    }
                })
            })
        })
    })
}


export {objectCardSitesInfo}
