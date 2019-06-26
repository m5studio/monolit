function formaThousands(number, precision=0) {
    // number = parseInt(number, 10).toFixed(precision)
    number = parseFloat(number).toFixed(precision)
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
                $(el).find('.oc-total-flats-qty').html( val['object_total_sites_qty'] )
                $(el).find('.oc-min-price').append( formaThousands(val['object_min_site_price']) )

                $(el).find('.oc-flats-area-min').append( formaThousands(val['object_min_site_area'], 1) )
                $(el).find('.oc-flats-area-max').append( formaThousands(val['object_max_site_area'], 1) )
            })
        })
    })
}


export {objectCardSitesInfo}
