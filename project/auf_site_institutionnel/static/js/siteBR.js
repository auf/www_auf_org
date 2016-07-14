// JavaScript de moi

$(document).ready(function(){
						   				   
$("#id_adresse").val('adresse@courriel.com');

/*SLIDER*/
$('#slides').bxSlider({
	wrapper_class: 'slides_wrap',
	mode: 'fade',
	pause: 6000,
	speed: 1500,
	auto: true
});

//Tab onglet	
						   
    //When page loads...
    $("#tabonglet .tab_content").hide(); //Hide all content
    $("#tabonglet ul.tabs li:first").addClass("active").show(); //Activate first tab
    $("#tabonglet .tab_content:first").show(); //Show first tab content

    //On Click Event
    $("#tabonglet ul.tabs li").click(function() {

        $("#tabonglet ul.tabs li").removeClass("active"); //Remove any "active" class
        $(this).addClass("active"); //Add "active" class to selected tab
        $("#tabonglet .tab_content").hide(); //Hide all tab content

        var activeTab = $(this).find("a").attr("href"); //Find the href attribute value to identify the active tab + content
        $(activeTab).fadeIn(); //Fade in the active ID content
        return false;
    });

});