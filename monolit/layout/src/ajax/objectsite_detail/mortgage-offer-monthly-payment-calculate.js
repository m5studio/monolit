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


                        console.log( 'Цена квартиры: ' + site_price_total + ' руб' )

                        let first_payment_rub = (site_price_total / 100) * first_payment_from
                        console.log( 'Первоначальный взнос: ' + first_payment_rub + ' руб' )

                        let loan_rub = site_price_total - first_payment_rub
                        console.log( 'Сумма кредита: ' + loan_rub + ' руб' )


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
                        loanTermSlider.noUiSlider.on('update', (years) => {
                            $('#' + loan_term_slider_years_id).empty()
                            $('#' + loan_term_slider_years_id).html(years + ' лет')

                            let rate = rate_from
                            let month_rate = rate / 12 / 100
                            let months = years * 12

                            let k = month_rate * (1 + month_rate) ** months / ((1 + month_rate) ** months - 1)
                            let payment = k * site_price_total * (1 - loan_rub / 100)

                            // let installment_per_month_rub = loan_rub / years_to_months
                            // Считаем  годовые
                            // let result = ((installment_per_month_rub * 12) / 100) * rate_from + (loan_rub / years_to_months)

                            $(el).find('.mortgage-offer__monthly-payment .mortgage-offer__val').empty()
                            $(el).find('.mortgage-offer__monthly-payment .mortgage-offer__val').html( formatNumber(payment, 2) + ' руб')
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
