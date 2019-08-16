function search_by_site_id() {
    console.log('search_by_site_id')

    const all_sites_api = $('#search-by-site-id').data('api-all-sites') 

    $('#search-by-site-id').keyup((event) => {
        console.log('keyup ' + all_sites_api)
    })
}


export {search_by_site_id}
