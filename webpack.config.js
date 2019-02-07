const path = require('path')
const webpack = require('webpack')
const HtmlWebpackPlugin = require('html-webpack-plugin')
const CleanWebpackPlugin = require('clean-webpack-plugin')
const MiniCssExtractPlugin = require('mini-css-extract-plugin')
const OptimizeCssAssetsPlugin = require('optimize-css-assets-webpack-plugin')


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
            }
        ]
    },
    optimization: {
        splitChunks: {
            chunks: 'all'
        }
    },
    plugins: [
        new CleanWebpackPlugin([
            './layout/dist/*.*',
            './layout/dist/css/**/*.*',
            './layout/dist/html/**/*.*',
            './layout/dist/images/*.*',
            './layout/dist/js/**/*.*'
        ]),

        // add jQuery to Webpack
        new webpack.ProvidePlugin({
            $: 'jquery',
            jQuery: 'jquery',
            'window.jQuery': 'jquery',
            Popper: ['popper.js', 'default'],
            noUiSlider: 'nouislider'
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
        new HtmlWebpackPlugin({
            filename: 'html/objects.html',
            template: './layout/src/html/objects.html'
        }),
    ]
}
