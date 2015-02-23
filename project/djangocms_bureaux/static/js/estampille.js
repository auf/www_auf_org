/*

AUF Estampille - PHILEOG ELEVEN 2014
====================================

Insert into web page :

------------- cut here ----------------

<script type="text/javascript">
(function() {
    function async_load(){
      var auf = document.createElement('script'); auf.id='auf-script'; auf.type = 'text/javascript'; auf.async = true;
      auf.src = 'http://cdn.phileog.com/static/AUF/Estampille_Sites_partenaires/estampille.js';
      var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(auf, s);
    }
    window.attachEvent ? window.attachEvent('onload', async_load) : window.addEventListener('load', async_load, false);
})();
</script>

------------- cut here ----------------

// inspiration async loading http://friendlybit.com/js/lazy-loading-asyncronous-javascript/

*/

(function(){

	// we are windows.load()...

    function loadCSS(url, callback)
    {
	    // Adding the script tag to the head 
	    var head = document.getElementsByTagName('head')[0];
	    var link = document.createElement('link');
	    link.type = 'text/css';
	    link.rel = 'stylesheet';
	    link.href = url;
	    link.media = 'all';

	    // Then bind the event to the callback function.
	    // There are several events for cross browser compatibility.
	    link.onreadystatechange = callback;
	    link.onload = callback;

	    // Fire the loading
	    head.appendChild(link);
	}

	var html =    '	<div class="auf-couleurs">'
				+ '	<div class="auf-bleu">&nbsp</div>'
				+ '		<div class="auf-jaune">&nbsp</div>'
				+ '		<div class="auf-vert">&nbsp</div>'
				+ '		<div class="auf-violet">&nbsp</div>'
				+ '		<div class="auf-rouge">&nbsp</div>'
				+ '	</div>'

				+ '	<div class="auf-phrase">'
				+ '		SITE PARTENAIRE, HÉBERGÉ PAR L\'<b>AGENCE UNIVERSITAIRE DE LA FRANCOPHONIE</b>'
				+ '	</div>';

	var wrapper = document.createElement("div");
	wrapper.id = 'auf-estampille'
	wrapper.innerHTML = html;

	var spacer = document.createElement('div');
	spacer.id ='auf-spacer';

	loadCSS(document.getElementById("auf-script").src.replace(/(\w*).js/i, 'estampille.css'), function() {
		document.body.insertBefore(wrapper, document.body.firstChild);
		document.body.insertBefore(spacer, document.body.firstChild);
	});
	loadCSS('http://fonts.googleapis.com/css?family=Open+Sans:300italic,400italic,600italic,700italic,300,700,400,600', function() {});


})();

