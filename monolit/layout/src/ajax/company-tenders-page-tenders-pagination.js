function companyTendersPagePagination() {
    $('#tenders-pagination a.page-link').each((index, el) => {
        $(el).click((e) => {
            e.preventDefault()
            let page_url = $(el).attr('href')
            // console.log( page_url )
            $.ajax({
                url: page_url,
                type: 'GET',
                success: (data) => {
                    $('#vacancies-list-accordion').empty()
                    $('#vacancies-list-accordion').append( $(data).find('#vacancies-list-accordion').html() )
                }
            })
        })
    })
}


export {companyTendersPagePagination}
