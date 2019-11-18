// Django AJAX https://medium.com/@a01701414/how-to-apply-ajax-with-django-2-1-8e9a4943f73
function django_ajax() {
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
            // if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            if (!csrfSafeMethod(settings.type)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken)
            }
        }
    })
}
// END Django AJAX


export {django_ajax}
