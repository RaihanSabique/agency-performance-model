from flask_assets import Bundle
bundles = {

    'index_js': Bundle(
        'js/index.js',
        "js/lib/jquery-1.11.1.min.js",
	    "js/lib/chart.min.js",
        "js/lib/chart-data.js",
	    "js/lib/easypiechart.js",
	    "js/lib/easypiechart-data.js",
	    "js/lib/bootstrap-datepicker.js",
	    "js/lib/custom.js",
        "js/lib/respond.min.js",
        "js/lib/html5shiv.min.js",
        output='gen/index.js'),

    'index_css': Bundle(
        'css/index.css',
        "css/lib/bootstrap.css",
        "css/lib/bootstrap.min.css",
	    "css/lib/font-awesome.min.css",
	    "css/lib/datepicker3.css",
	    "css/lib/styles.css",
        output='gen/index.css'),
}


