


var casper = require('casper').create({   
    verbose: true, 
    logLevel: 'debug',
    pageSettings: {
		
		// The WebPage instance used by Casper will
        loadImages:  false,
		
		// use these settings
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



var login_url = 'http://rosalind.info/accounts/login/';
casper.start(login_url, function() {
	console.log("page loaded");
	
	//this.test.assertExists('form#id_form_login', 'form is found');
	//console.log("found login form...");
	
	this.fill('form#id_form_login', {
        username: 'giphahneapi',
        password: 'g9G-s6U-ebt-tv5'
    }, true);

	console.log("logged in...?")
});


var problem_page_url = 'http://rosalind.info/problems/' + casper.cli.args[0] + '/';

casper.thenOpen(problem_page_url, function() {
	console.log("loaded problem page: " + casper.cli.args[0]);
	console.log("Problem Name: " + document.querySelector('h1').textContent); 
});

casper.run();
