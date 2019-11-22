import {singularPlural} from "../modules/singular-plural"
import {formatNumber} from "../modules/format-number"


function objectCardSitesInfo() {
    $('.object-card').each((index, el) => {
        let site_info_url = $(el).data('sites-info-api-url')
        let sites_url = $(el).data('sites-url')

        $.getJSON(site_info_url, (data) => {
            $.each(data, (index, val) => {
                // Кол-во квартир
                if ( val['object_total_sites_qty'] > 0 ) {
                    $(el).find('.object-card__site--count').append(
                        '<a href="">' +
                            '<span class="oc-sites-total-qty">' + val['object_total_sites_qty'] + ' ' + singularPlural(val['object_total_sites_qty'], ['квартира', 'квартиры', 'квартир']) + '</span>' +
                        '</a>'
                    )
                }

                // Площадь от - до
                if ( val['object_min_site_area'] && val['object_max_site_area'] ) {
                    $(el).find('.object-card__features').append(
                        '<div class="object-card__features--block oc-sites-min-max-area--block">' +
                            '<div class="object-card__features--name">Площадь</div>' +
                            '<div class="object-card__features--value">' +
                                '<span class="oc-sites-area-min">от ' + formatNumber(val['object_min_site_area'], 1) + '</span>' +
                                '<span class="oc-sites-area-max"> до ' + formatNumber(val['object_max_site_area'], 1) + ' м<sup>2</sup></span>' +
                            '</div>' +
                        '</div>'
                    )
                }

                // Минимальная стоимость
                if ( val['object_min_site_price'] ) {
                    $(el).find('.object-card__features').append(
                        '<div class="object-card__features--block oc-sites-min-price--block">' +
                            '<div class="object-card__features--name">Стоимость</div>' +
                            '<div class="object-card__features--value">' +
                                '<span class="oc-sites-min-price">от ' + formatNumber( val['object_min_site_price'].toString() ) + ' руб.</span>' +
                            '</div>' +
                        '</div>'
                    )
                }
            })

            $.each(data[1], (index, val) => {
                $.each(val, (i, v) => {
                    if ( v['sites_qty'] > 0 ) {
                        // Квартиры в .object-card__emerge-object
                        $(el).find('.object-card__emerge').append(
                            '<div class="object-card__emerge-object">' +
                                '<a href="" class="object-card__emerge-link">' +
                                    '<div class="object-card__site-types-item">' + v['name'] + '</div>' +
                                    '<div class="object-card__emerge-title">' + v['sites_qty'] + ' ' + singularPlural(v['sites_qty'], ['квартира', 'квартиры', 'квартир'], true) + '</div>' +
                                    '<div class="object-card__emerge-area-space">' + formatNumber(v['min_area'], 1) + ' - ' + formatNumber(v['max_area'], 1) + ' м<sup>2</sup></div>' +
                                    '<div class="object-card__emerge-arrow"></div>' +
                                '</a>' +
                            '</div>'
                        )
                        $(el).find('.object-card__site-types').append('<a href="" class="object-card__site-types-item">' + v['name'] + '</a>')
                    }
                })
            })
        })
    })
}


export {objectCardSitesInfo}
