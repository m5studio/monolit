function singularPlural(n, text_list, show_number=false) {
    // n = parseInt(n, 10)
    n = Math.abs(n) % 100
    let n1 = n % 10

    if (n > 10 && n < 20) {
        if (show_number) {
            return n + ' ' + text_list[2]
        } else {
            return text_list[2]
        }
    }
    if (n1 > 1 && n1 < 5) {
        if (show_number) {
            return n + ' ' + text_list[1]
        } else {
            return text_list[1]
        }
    }
    if (n1 == 1) {
        if (show_number) {
            return n + ' ' + text_list[0]
        } else {
            return text_list[0]
        }
    }
    if (show_number) {
        return n + ' ' + text_list[2]
    } else {
        return text_list[2]
    }
}


export {singularPlural}
