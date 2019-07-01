import {formatNumber} from "../../modules/format-number"


function objectPageSitesInfo() {
    if ( $('#section-object-page-main-info').data('sites-info-url') ) {
        const site_info_url = $('#section-object-page-main-info').data('sites-info-url')

        $.getJSON(site_info_url, (data) => {
            const objectStats = data[0]
            const objectFlatsStats = data[1]

            $('.obj-area-min').append( '<small>от</small> ' + formatNumber(objectStats['object_min_site_area'], 2) )
            $('.obj-area-max').append( ' <small>до</small> ' + formatNumber(objectStats['object_max_site_area'], 2) + ' <small>м<sup>2</sup></small>' )

            $('.obj-min-price').append( '<small>от</small> ' + formatNumber(objectStats['object_min_site_price'], 0) + ' <small>руб.</small>' )

            // console.log( data )
            // console.log( objectStats )
            // console.log( objectFlatsStats )
        })
    }
}


export {objectPageSitesInfo}
