import "./main.scss"
import "./bootstrap/bootstrap"

import {stickyMainNav, toggleMainNav} from "./menu/main-nav"

// Fiters
import {familyFiltersToggle} from "./filters/family-filters-toggle"
import {familyFiltersReset} from "./filters/family-filters-reset"

// Realty filters
import {realtySquareFilters} from "./modules/nouislider/realty_square_filters"
import {realtyPriceFilters} from "./modules/nouislider/realty_price_filters"
import {realtyFloorFilters} from "./modules/nouislider/realty_floor_filters"

// Scroll to Top
import {scrollToTop} from "./modules/scroll-to-top/scroll-to-top"

// Ajax
import {objectPageGalleries} from "./ajax/object-page-galleries"

// Fancybox https://fancyapps.com/fancybox/3/
import '@fancyapps/fancybox'


$(document).ready(function() {
    toggleMainNav()

    // Homepage
    if ( $('#section-realty-homepage-filters').length ) {
        realtySquareFilters()
        realtyPriceFilters()
    }

    // Flats
    if ( $('#section-realty-flats-filters').length ) {
        realtySquareFilters()
        realtyPriceFilters()
        realtyFloorFilters()
    }

    familyFiltersToggle()
    familyFiltersReset()

    scrollToTop()


    // Object page galleries
    if ( $('.object-page').length ) {
        objectPageGalleries()
    }


    // Django Ajax
    // README: https://medium.com/@a01701414/how-to-apply-ajax-with-django-2-1-8e9a4943f73
    // Cookie obtainer Django
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            let cookies = document.cookie.split(';')
            for (let i = 0; i < cookies.length; i++) {
                let cookie = jQuery.trim(cookies[i])
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1))
                    break
                }
            }
        }
        return cookieValue
    }
    let csrftoken = getCookie('csrftoken')
    // Setup ajax connections safetly

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method))
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken)
            }
        }
    })

    // $('form#ajax-form').submit(function(e) {
    //     e.preventDefault()
    //     const docs_list_container = $('#section-object-downloads__inner')
    //     // let message_val = $('input#message', this).val()
    //     // console.log(message_val)
    //     let object_id_url = $('#object_id_url', this).val()
    //
    //     docs_list_container.empty()
    //
    //     $.ajax({
    //         url: object_id_url,
    //         type: 'POST',
    //         dataType: 'json',
    //         data: {
    //             'test': 3,
    //         },
    //         success: function(data) {
    //             console.log(data)
    //
    //             $.each(data, (i, val) => {
    //                 let file_link = '/media/'+val.file
    //                 let doc_layout = '<div class="doc-download"><div class="doc-download__t-d-u-wrap"><div class="doc-download__title">'+val.title+'</div><div class="doc-download__d-u-wrap"><div class="doc-download__date">Дата: '+val.date+'</div><div class="doc-download__user-name">Автор: '+val.author__name+'</div></div></div><div class="doc-download__size">{{ document.file.url|get_file_ext|upper }}, {{ document.file.size|bytes_to_mb }}</div><div class="doc-download__link"><div class="icon icon-32 icon-download"></div><a href="'+file_link+'" class="stretched-link" target="_blank" title="Скачать"></a></div></div>'
    //                 docs_list_container.append(doc_layout)
    //             })
    //         }
    //     })
    // })
    // END Django Ajax


    // Object Documents Ajax pagination
    /*
    $('a#page-docs-prev').click((e) => {
        e.preventDefault()
        let page_url = $('a#page-docs-prev', this).attr('href')
        console.log( page_url )

        $.ajax({
            url: page_url,
            type: 'GET',
            success: (data) => {
                $('#section-object-downloads__inner').empty()
                $('#section-object-downloads__inner').append( $(data).find('#section-object-downloads__inner').html() )

                $('#page-docs-pagination').empty()
                $('#page-docs-pagination').append( $(data).find('#page-docs-pagination').html() )
            }
        })

        // $.get(page_url, function(data) {
        //     $('#section-object-downloads__inner').empty()
        //     $('#section-object-downloads__inner').append( $(data).find('#section-object-downloads__inner').html() )
        //
        //     $('#page-docs-pagination').empty()
        //     $('#page-docs-pagination').append( $(data).find('#page-docs-pagination').html() )
        // })
    })
    $('a#page-docs-next').click((e) => {
        e.preventDefault()
        let page_url = $('a#page-docs-next', this).attr('href')
        console.log( page_url )

        $.ajax({
            url: page_url,
            type: 'GET',
            success: (data) => {
                $('#section-object-downloads__inner').empty()
                $('#section-object-downloads__inner').append( $(data).find('#section-object-downloads__inner').html() )

                $('#page-docs-pagination').empty()
                $('#page-docs-pagination').append( $(data).find('#page-docs-pagination').html() )
            }
        })

        // $.get(page_url, function(data) {
        //     $('#section-object-downloads__inner').empty()
        //     $('#section-object-downloads__inner').append( $(data).find('#section-object-downloads__inner').html() )
        //
        //     $('#page-docs-pagination').empty()
        //     $('#page-docs-pagination').append( $(data).find('#page-docs-pagination').html() )
        // })
    })
    */
    // END Object Documents Ajax pagination

    // Object Documents Ajax pagination
    $('#page-docs-pagination a.page-link').each((index, el) => {
        $(el).click((e) => {
            e.preventDefault()

            let page_url = $(el).attr('href')
            // console.log( page_url )

            $.ajax({
                url: page_url,
                type: 'GET',
                success: (data) => {
                    $('#section-object-downloads__inner').empty()
                    $('#section-object-downloads__inner').append( $(data).find('#section-object-downloads__inner').html() )

                    $('#page-docs-pagination').empty()
                    $('#page-docs-pagination').append( $(data).find('#page-docs-pagination').html() )
                }
            })
        })
    })
    // END Object Documents Ajax pagination

})


$(document).ajaxStop(function() {
    // Object Documents Ajax pagination
    $('#page-docs-pagination a.page-link').each((index, el) => {
        $(el).click((e) => {
            e.preventDefault()

            let page_url = $(el).attr('href')
            // console.log( page_url )

            $.ajax({
                url: page_url,
                type: 'GET',
                success: (data) => {
                    $('#section-object-downloads__inner').empty()
                    $('#section-object-downloads__inner').append( $(data).find('#section-object-downloads__inner').html() )

                    $('#page-docs-pagination').empty()
                    $('#page-docs-pagination').append( $(data).find('#page-docs-pagination').html() )
                }
            })
        })
    })
    // END Object Documents Ajax pagination
})


$(window).scroll(function() {
    stickyMainNav()
})
