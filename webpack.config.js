const path = require('path')
const webpack = require('webpack')
const HtmlWebpackPlugin = require('html-webpack-plugin')
const CleanWebpackPlugin = require('clean-webpack-plugin')
const MiniCssExtractPlugin = require('mini-css-extract-plugin')
const OptimizeCssAssetsPlugin = require('optimize-css-assets-webpack-plugin')
const CopyWebpackPlugin = require('copy-webpack-plugin')


module.exports = {
    mode: 'production',
    entry: './layout/src/main.js',
    output: {
        filename: 'js/[name].js',
        path: path.resolve(__dirname, './layout/dist'),
        publicPath: '../'
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: ['babel-loader']
            },
            {
                test: /\.scss$/,
                use: [
                    MiniCssExtractPlugin.loader,
                    'css-loader',
                    'sass-loader'
                ]
            },
            {
                test: /\.(png|svg|jpg|gif)$/,
                use: [
                    {
                        loader: 'file-loader',
                        options: {
                            name: '[name].[ext]',
                            outputPath: 'images/',
                            useRelativePath: true
                        }
                    },
                    {
                        loader: 'image-webpack-loader',
                        options: {
                            mozjpeg: {
                                progressive: true,
                                quality: 70
                            },
                            optipng: {
                                enabled: true,
                            },
                            pngquant: {
                                quality: '65-90',
                                speed: 4
                            }
                        }
                    }
                ]
            },
        ]
    },
    optimization: {
        splitChunks: {
            chunks: 'all'
        }
    },
    plugins: [
        new CleanWebpackPlugin([
            // instead clenning inner folders, delete entire dist
            'layout/dist'

            // './layout/dist/**/*.*',
            // './layout/dist/css/**/*.*',
            // './layout/dist/html/**/*.*',
            // './layout/dist/images/*.*',
            // './layout/dist/js/**/*.*'
        ]),

        // Copy favicons
        new CopyWebpackPlugin([
            {from:'./layout/src/images/favicons', to:'images/favicons'}
        ]),

        // Add jQuery to Webpack
        new webpack.ProvidePlugin({
            $: 'jquery',
            jQuery: 'jquery',
            'window.jQuery': 'jquery',
            Popper: ['popper.js', 'default'],
            noUiSlider: 'nouislider',
        }),

        new MiniCssExtractPlugin({
            filename: 'css/styles.css'
        }),

        new OptimizeCssAssetsPlugin({
            // CSS minification
            assetNameRegExp: /\.css$/g,
            cssProcessor: require('cssnano'),
            cssProcessorPluginOptions: {
                preset: ['default', {
                    discardComments: {
                        removeAll: true
                    }
                }]
            },
            canPrint: true
        }),

        new HtmlWebpackPlugin({
            filename: 'html/homepage.html',
            template: './layout/src/html/homepage.html'
        }),

        // Objects
        new HtmlWebpackPlugin({
            filename: 'html/objects.html',
            template: './layout/src/html/objects/objects.html'
        }),
        new HtmlWebpackPlugin({
            filename: 'html/objects_page.html',
            template: './layout/src/html/objects/objects_page.html'
        }),

        // Commercial
        new HtmlWebpackPlugin({
            filename: 'html/commercial.html',
            template: './layout/src/html/commercial/commercial.html'
        }),
        new HtmlWebpackPlugin({
            filename: 'html/commercial_page.html',
            template: './layout/src/html/commercial/commercial_page.html'
        }),

        // Flats
        new HtmlWebpackPlugin({
            filename: 'html/flats.html',
            template: './layout/src/html/flats/flats.html'
        }),
        new HtmlWebpackPlugin({
            filename: 'html/flats_page.html',
            template: './layout/src/html/flats/flats_page.html'
        }),

        // Mortgage
        new HtmlWebpackPlugin({
            filename: 'html/mortgage.html',
            template: './layout/src/html/mortgage/mortgage.html'
        }),
        new HtmlWebpackPlugin({
            filename: 'html/mortgage_military.html',
            template: './layout/src/html/mortgage/mortgage_military.html'
        }),
        new HtmlWebpackPlugin({
            filename: 'html/mortgage_mother.html',
            template: './layout/src/html/mortgage/mortgage_mother.html'
        }),
        new HtmlWebpackPlugin({
            filename: 'html/mortgage_corporactive.html',
            template: './layout/src/html/mortgage/mortgage_corporactive.html'
        }),
        new HtmlWebpackPlugin({
            filename: 'html/mortgage_corporactive.html',
            template: './layout/src/html/mortgage/mortgage_corporactive.html'
        }),

        // Company
        new HtmlWebpackPlugin({
            filename: 'html/company.html',
            template: './layout/src/html/company/company.html'
        }),
        new HtmlWebpackPlugin({
            filename: 'html/company_mission.html',
            template: './layout/src/html/company/company_mission.html'
        }),
        new HtmlWebpackPlugin({
            filename: 'html/company_management.html',
            template: './layout/src/html/company/company_management.html'
        }),
        new HtmlWebpackPlugin({
            filename: 'html/company_structure.html',
            template: './layout/src/html/company/company_structure.html'
        }),
        new HtmlWebpackPlugin({
            filename: 'html/company_vacancy.html',
            template: './layout/src/html/company/company_vacancy.html'
        }),
        new HtmlWebpackPlugin({
            filename: 'html/company_responsibility.html',
            template: './layout/src/html/company/company_responsibility.html'
        }),
        new HtmlWebpackPlugin({
            filename: 'html/company_history.html',
            template: './layout/src/html/company/company_history.html'
        }),
        new HtmlWebpackPlugin({
            filename: 'html/company_partnership.html',
            template: './layout/src/html/company/company_partnership.html'
        }),
        // TODO: Tenders
        // new HtmlWebpackPlugin({
        //     filename: 'html/company_tenders.html',
        //     template: './layout/src/html/company/company_tenders.html'
        // }),

        // News
        new HtmlWebpackPlugin({
            filename: 'html/news.html',
            template: './layout/src/html/news/news.html'
        }),
        new HtmlWebpackPlugin({
            filename: 'html/news_page.html',
            template: './layout/src/html/news/news_page.html'
        }),

        // Actions
        new HtmlWebpackPlugin({
            filename: 'html/actions.html',
            template: './layout/src/html/actions/actions.html'
        }),
        new HtmlWebpackPlugin({
            filename: 'html/actions_page.html',
            template: './layout/src/html/actions/actions_page.html'
        }),

        // Contacts
        new HtmlWebpackPlugin({
            filename: 'html/contacts.html',
            template: './layout/src/html/pages/contacts.html'
        }),
    ]
}
