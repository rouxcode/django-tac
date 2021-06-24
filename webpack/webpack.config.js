const path = require("path")

const node_modules = path.resolve(__dirname, 'node_modules')


// webpack entry points -------------------------------------------------------

module.exports = [

    // tac assets ---------------------------------------------------------
    {
        entry: {
            'tac/tac': path.resolve(__dirname, '../tac/static_src/tac/tac.js')
        },
        resolve: {
            // add custom  node_modules import path
            modules: [node_modules, 'node_modules'],
        },
        output: {
            path: path.resolve(__dirname, "../tac/static"),
            filename: "[name].js",
        },
        plugins: [],
        module: {},
    },
]
