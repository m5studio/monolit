import {formatNumber, formatNumberText} from "../../modules/format-number"


function objectPageSitesInfo() {
    if ( $('#section-object-page-main-info').data('sites-info-url') ) {
        const site_info_url = $('#section-object-page-main-info').data('sites-info-url')

        $.getJSON(site_info_url, (data) => {
            const objectStats = data[0]

            if ( objectStats['object_total_sites_qty'] === 0 ) {
                $('#section-object-page-main-info__stats').remove()
            } else {
                $('.obj-area-min').append( '<small>от</small> ' + formatNumber(objectStats['object_min_site_area'], 2) )
                $('.obj-area-max').append( ' <small>до</small> ' + formatNumber(objectStats['object_max_site_area'], 2) + ' <small>м<sup>2</sup></small>' )
                $('.obj-min-price').append( '<small>от</small> ' + formatNumber(objectStats['object_min_site_price'], 0) + ' <small>руб.</small>' )
            }
        })
    }
}


function objectPageFlatsTypes() {
    if ( $('#section-object-page-main-info').data('sites-info-url') ) {
        const site_info_url = $('#section-object-page-main-info').data('sites-info-url')
        const sectionFlatsType = $('#section-flats-types')

        $.getJSON(site_info_url, (data) => {
            // const objectStats = data[0]
            const objectFlatsInfo = data[1]['flats_info']

            $.each(objectFlatsInfo, (index, el) => {
                let flat_card = sectionFlatsType.find('.flat-type-card__room-'+index)

                if ( el['flats_qty'] > 0 ) {
                    flat_card.addClass('active')

                    flat_card.find('.flat-type-card__info--area').append( 'от ' + formatNumber(el['min_area'], 1) + '<br>до ' + formatNumber(el['max_area'], 1) + ' м<sup>2</sup>' )
                    flat_card.find('.flat-type-card__info--price').append('от ' + formatNumberText(el['min_price']) + ' руб.' )
                }
            })
        })
    }
}


export {objectPageSitesInfo, objectPageFlatsTypes}
