function preventPressEnter() {
    $(window).keydown((event) => {
        if (event.keyCode == 13) {
            event.preventDefault()
            return false
        }
    })
}


function search_by_site_id() {
    const search_id = $('#search-by-site-id')
    const search_results_id = $('#search-by-site-id__results')
    const all_sites_api = search_id.data('api-all-sites')

    preventPressEnter()

    $('#search-by-site-id').keyup((event) => {
        search_results_id.empty()
        // search_results_id.html('')

        let serch_val = search_id.val()
        let expression = new RegExp(serch_val, "i")

        $.getJSON(all_sites_api, function(data) {
            $.each(data, function(index, el) {
                if (el.crm_id.search(expression) != -1) {
                    search_results_id.append('<div>' + el['crm_id'] + '</div>')
                }
            })
        })
    })
}


export {search_by_site_id}
