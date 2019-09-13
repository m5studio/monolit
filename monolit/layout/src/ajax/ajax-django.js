/*
    Django Ajax
    README: https://medium.com/@a01701414/how-to-apply-ajax-with-django-2-1-8e9a4943f73
*/

// Cookie obtainer Django
function getCookie(name) {
    let cookieValue = null
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
const csrftoken = getCookie('csrftoken')

// Setup ajax connections safetly
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method))
}
$.ajaxSetup({
    beforeSend: (xhr, settings) => {
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
