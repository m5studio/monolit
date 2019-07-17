import {formatNumber} from "../../modules/format-number"


function mortgageOfferMonthlyPaymentCalculate() {
    if ( $('#section-flat-page-content').data('object-site') ) {
        const site_info_url = $('#section-flat-page-content').data('object-site')

        if ( $('#section-flat-page-mortgage') ) {
            $.getJSON(site_info_url, (site_info_data) => {
                // Site total price
                const site_price_total = site_info_data[0]['price_total']

                $('.mortgage-offer').each((index, el) => {
                    let mortgage_offer_api_url = $(el).data('api-mortgage-offer')

                    $.getJSON(mortgage_offer_api_url, (mortgage_offer_data) => {
                        let offer_id = mortgage_offer_data[0]['id']

                        // Первоначальный платеж
                        let first_payment_from = mortgage_offer_data[0]['first_payment_from']
                        let first_payment_to = mortgage_offer_data[0]['first_payment_to']

                        // Срок кредита
                        let loan_term_from = mortgage_offer_data[0]['loan_term_from']
                        let loan_term_to = mortgage_offer_data[0]['loan_term_to']

                        // % ставка
                        let rate_from = mortgage_offer_data[0]['rate_from']
                        let rate_to = mortgage_offer_data[0]['rate_to']


                        // Mortgage Calculation
                        // 1% от стоимости помещения
                        let one_percent = (site_price_total / 100)
                        console.log('1% = ' + one_percent + ' руб')

                        // Первоначальный платеж в руб
                        let first_payment_val = 0
                        if ( first_payment_from === first_payment_to ) {
                            first_payment_val = first_payment_from * one_percent
                            console.log('[Равны] от: ' + first_payment_from + ' до: ' + first_payment_to)

                        } else if ( first_payment_from != null && first_payment_to != null ) {
                            first_payment_val = first_payment_from * one_percent
                            console.log('[НЕ null] от: ' + first_payment_from + ' до: ' + first_payment_to)

                        } else if ( first_payment_to === null ) {
                            first_payment_val = first_payment_from * one_percent
                            console.log('[null first_payment_to] от: ' + first_payment_from + ' до: ' + first_payment_to)

                        } else if ( first_payment_from === null ) {
                            first_payment_val = first_payment_to * one_percent
                            console.log('[null first_payment_from] от: ' + first_payment_from + ' до: ' + first_payment_to)
                        }
                        console.log('Первый платеж: ' + first_payment_val + ' руб')

                        // Сумма кредита
                        let loan_val = site_price_total - first_payment_val
                        console.log('Сумма кредита: ' + loan_val + ' руб')

                        // Переплата по кредиту
                        // TODO: check rate_from and rate_to
                        let bank_interest = site_price_total + (rate_from * one_percent)

                        console.log('')
                        // END Mortgage Calculation


                        // Create loan term slider
                        let loan_term_slider_id = 'loan_term_slider_' + offer_id
                        let loan_term_slider_years_id = 'loan_term_years_' + offer_id

                        $(el).find('.mortgage-offer__pay-off .mortgage-offer__val').append('<div id="' + loan_term_slider_years_id + '" class="mortgage-offer__years"></div>' +
                                                                                           '<div id="' + loan_term_slider_id + '"></div>')

                        let loanTermSlider = document.getElementById(loan_term_slider_id)
                        noUiSlider.create(loanTermSlider, {
                            behaviour: 'snap',
                            // start: loan_term_to,
                            start: Math.floor(Math.random() * (loan_term_to - loan_term_from)) + loan_term_from, // Generate random number in range loan_term_from and loan_term_to
                            step: 1,
                            connect: [true, false],
                            range: {
                                'min': loan_term_from,
                                'max': loan_term_to
                            },
                            format: {
                                to: (value) => {
                                    return Math.round(value)
                                },
                                from: (value) => {
                                    return Math.round(value)
                                }
                            }
                        })
                        // END Create loan term slider


                        // loan term slider Changed
                        loanTermSlider.noUiSlider.on('update', (value) => {
                            $('#' + loan_term_slider_years_id).empty()
                            $('#' + loan_term_slider_years_id).html(value + ' лет')

                            let months = value * 12
                            // let result = loan_val / months
                            // let result = site_price_total / months
                            let result = bank_interest / months

                            $(el).find('.mortgage-offer__monthly-payment .mortgage-offer__val').empty()
                            $(el).find('.mortgage-offer__monthly-payment .mortgage-offer__val').html( formatNumber(result, 2) + ' руб')
                            // $(el).find('.mortgage-offer__monthly-payment .mortgage-offer__val').html( formatNumber(result, 0) + ' руб')
                        })
                        // END loan term slider Changed
                    })
                })
            })
        }
    }
}


export {mortgageOfferMonthlyPaymentCalculate}
