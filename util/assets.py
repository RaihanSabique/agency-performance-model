from flask_assets import Bundle
bundles = {

    'index_js': Bundle(
        'js/index.js',
        output='gen/index.js'),

    'home_css': Bundle(
        'css/index.css',
        output='gen/index.css'),
}


