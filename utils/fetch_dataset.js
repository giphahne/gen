var casper = require('casper').create({   
	verbose: false, 
	logLevel: 'info',
    pageSettings: {
        loadImages:  false,
        loadPlugins: true,         
		userAgent: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4'
    }
});

// print out all the messages in the headless browser context
casper.on('remote.message', function(msg) {
    this.echo('remote message caught: ' + msg);
});

// print out all the messages in the headless browser context
casper.on("page.error", function(msg, trace) {
    this.echo("Page Error: " + msg, "ERROR");
});


var url = 'http://rosalind.info/';
var login_url = url + 'accounts/login/';
casper.start(login_url, function() {
	//console.log("page loaded");
	
	//this.test.assertExists('form#id_form_login', 'form is found');
	//console.log("found login form...");
	//console.log(casper.cli.get("u"));
	//console.log(casper.cli.get("p"));
	
	this.fill('form#id_form_login', {
        username: casper.cli.get("u"),
        password: casper.cli.get("p"),
    }, true);
	
});

var problem_page_url = url + 'problems/' + casper.cli.args[0] + '/';
casper.thenOpen(problem_page_url, function() {
	//console.log("loaded problem page: " + casper.cli.args[0]);
	//console.log("Problem Name: " + this.getTitle());

	var d = new Date();
	var seconds = Math.round(d.getTime() / 1000);
	var dataset_filename = casper.cli.args[0] + '_' + seconds + '.txt'
	this.download(
		url + 'problems/' + casper.cli.args[0] + '/dataset/',
		dataset_filename
	);
	console.log(dataset_filename);
});

casper.run();



