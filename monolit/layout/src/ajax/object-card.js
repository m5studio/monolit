function objectCardSitesInfo() {
    $('.object-card').each((index, el) => {
        let site_info_url = $(el).data('sites-info-url')

        $.getJSON(site_info_url, (data) => {
            $.each(data, (index, val) => {
                $(el).find('.oc-total-flats-qty').html( val['object_total_sites_qty'] )

                let site_price = val['object_min_site_price']
                // let site_price = parseInt(val['object_min_site_price'], 10)
                // let site_price = parseInt(val['object_min_site_price'], 10).toString()
                // let site_price = parseFloat(val['object_min_site_price'], 1).toString()
                // $(el).find('.oc-min-price').append( site_price.replace(/\B(?=(\d{3})+(?!\d))/g, " ") )
                // $(el).find('.oc-min-price').append( site_price.replace(/\B(?=(\d{3})+(?!\d))/g, " ").replace('NaN','') )
                $(el).find('.oc-min-price').append( site_price )
            })
        })
    })
}


export {objectCardSitesInfo}
