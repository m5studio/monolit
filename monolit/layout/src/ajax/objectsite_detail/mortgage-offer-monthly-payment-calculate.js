import {formatNumber} from "../../modules/format-number"

// function calculateMortgagePayment() {
//     return first_payment_from
// }


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
                        // Первоначальный платеж
                        let first_payment_from = mortgage_offer_data[0]['first_payment_from']
                        let first_payment_to = mortgage_offer_data[0]['first_payment_to']

                        // Срок кредита
                        let loan_term_from = mortgage_offer_data[0]['loan_term_from']
                        let loan_term_to = mortgage_offer_data[0]['loan_term_to']

                        // % ставка
                        let rate_from = mortgage_offer_data[0]['rate_from']
                        let rate_to = mortgage_offer_data[0]['rate_to']


                        // Calculation
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
                        console.log('Сумма займа: ' + loan_val + ' руб')

                        // let result = one_percent
                        // $(el).find('.mortgage-offer__monthly-payment .mortgage-offer__val').append( formatNumber(result, 1) + ' руб')

                        console.log('')
                    })
                })
            })
        }
    }
}


export {mortgageOfferMonthlyPaymentCalculate}
