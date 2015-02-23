/*----------------------------------------------------------------------------//
// Javascript pour le site client  -------------------------------------------//
//----------------------------------------------------------------------------//
// Client : Agence universitaire de la Francophonie
// Note   : -
// Date   : -
//----------------------------------------------------------------------------*/

/*----------------------------------------------------------------------------*/
// Declarations jQuery
/*----------------------------------------------------------------------------*/

var menuTotalWidth = 0;
var menuWidth = 0;
var menuPosition = 0;
var infoItem = 0;
var mapZones = new Array(
    zone0 = "Afrique-Centrale",
    zone1 = "Afrique-de-l-Ouest",
    zone2 = "Ameriques",
    zone3 = "Asie-Pacifique",
    zone4 = "Caraibes",
    zone5 = "Europe-centrale-et-orientale",
    zone6 = "Moyen-Orient",
    zone7 = "Ocean-Indien",
    zone8 = "Maghreb",
	zone9 = "Europe-de-l-Ouest"
);
var selectedRegion = "International"

/*Verifier mail newsletter*/
function valide(){
	  if(document.news.email.value != "adresse@courriel.com") {
		return true;
	  }
	  else {
		alert("Veullez saisir votre propre adresse");
		return false;
	  }
	}

$(document).ready(function(){
						   
	$( ".datepicker" ).datepicker({
			inline: true
	});
						   
	/*CARTE MARC*/
	jQuery("#carte AREA").hover(
								
		function() {
			var regionMap = '#'+$(this).attr('id')+'-map';
			var regionDesc = '#'+$(this).attr('id')+'-desc';
			$(regionMap).stop().animate({"opacity": "1"}, "slow");
			$(regionDesc).stop().animate({"opacity": "1"}, "slow");	
			$("#inter").stop().animate({"opacity": "0"}, "slow");	
		},
		function() {
			var regionMap = '#'+$(this).attr('id')+'-map';
			var regionDesc = '#'+$(this).attr('id')+'-desc';
			$(regionMap).stop().animate({"opacity": "0"}, "slow");
			$(regionDesc).stop().animate({"opacity": "0"}, "fast");
			$("#inter").stop().animate({"opacity": "1"}, "slow");
		});

    InitOldBrowser();

    // -----------------------------------------------------------------------------------------------------------------
    // PrÃ©chargement des images de la carte ----------------------------------------------------------------------------
    // -----------------------------------------------------------------------------------------------------------------
    jQuery.preLoadImages(window.__media_prefix__ + "img/carte/ZoneAfrique-Centrale.png");
    jQuery.preLoadImages(window.__media_prefix__ + "img/carte/ZoneAfrique-de-l-Ouest.png");
    jQuery.preLoadImages(window.__media_prefix__ + "img/carte/ZoneAmeriques.png");
    jQuery.preLoadImages(window.__media_prefix__ + "img/carte/ZoneAsie-Pacifique.png");
    jQuery.preLoadImages(window.__media_prefix__ + "img/carte/ZoneCaraibes.png");
    jQuery.preLoadImages(window.__media_prefix__ + "img/carte/ZoneEurope-centrale-et-orientale.png");
    jQuery.preLoadImages(window.__media_prefix__ + "img/carte/ZoneEurope-de-l-Ouest.png");
    jQuery.preLoadImages(window.__media_prefix__ + "img/carte/ZoneMoyen-Orient.png");
    jQuery.preLoadImages(window.__media_prefix__ + "img/carte/ZoneOcean-Indien.png");
	jQuery.preLoadImages(window.__media_prefix__ + "img/carte/ZoneMaghreb.png");
    jQuery.preLoadImages(window.__media_prefix__ + "img/carte/ZoneMonde.png");

    // -----------------------------------------------------------------------------------------------------------------
    // Ajustements divers ----------------------------------------------------------------------------------------------
    // -----------------------------------------------------------------------------------------------------------------
    jQuery(".ChampRecherche input").Watermark("Recherche");
    jQuery(".ChampInscription input").Watermark("adresse@courriel.com");
    jQuery("#PiedPage li:last").addClass("DernierItem");
    jQuery("#FilAriane li:last").addClass("DernierItem");
    jQuery("#MenuSecondaire li:last").addClass("DernierItem");
    jQuery("hr").replaceWith("<div class=\"hr\">&nbsp;</div>");


    // -----------------------------------------------------------------------------------------------------------------
    // Formulaire pour bourse ou appel Ã  projet ------------------------------------------------------------------------
    // -----------------------------------------------------------------------------------------------------------------

    // Compteur de caractÃ¨res
    if(jQuery("#txtDescription").length == 1){
        $('#txtDescription').NobleCount('#Compteur', {
            on_negative: 'go_red'
        });
    }

    // Boutons Parcourir
    jQuery(".BoutonUpload").css({opacity: 0});
    jQuery(".BoutonUpload").change(function(){
        jQuery(this).parents(".Champ").children(".TxtBox").val(jQuery(this).val());
    });

    // Watermarks
    jQuery("#txtTitre").Watermark("Titre de la bourse ou de lâ€™appel Ã  projet");
    jQuery("#txtDescription").Watermark("DÃ©crivez lâ€™objectif, les conditions, le calendrier de la bourse ou de lâ€™appel Ã  projet");
    jQuery("#txtFond").Watermark("0");
    jQuery("#txtDateLimite").Watermark("JJ/MM/AAAA");

    // -----------------------------------------------------------------------------------------------------------------
    // Bloc Ã  onglets --------------------------------------------------------------------------------------------------
    // -----------------------------------------------------------------------------------------------------------------
    jQuery("form", "body.Formulaire").css("display", "none");
    jQuery("form:first",  "body.Formulaire").css("display", "block");
    jQuery("a:first", ".BlocOnglets").addClass("On");
    jQuery("a", ".BlocOnglets").click(function(){
        jQuery("a", ".BlocOnglets").removeClass("On");
        jQuery(this).addClass("On");
        var selectionOnglet = jQuery(this).attr("href");
        jQuery("form", "body.Formulaire").css("display","none");
        jQuery(selectionOnglet).css("display","block");
        return false;
    });


    // -----------------------------------------------------------------------------------------------------------------
    // Ajustements aux colonnes de l'accueil ---------------------------------------------------------------------------
    // -----------------------------------------------------------------------------------------------------------------
    if(jQuery("body").hasClass("Accueil")){
        if(jQuery("#ColonneLaterale").height() > jQuery("#BlocContenu").height()){
            jQuery("#BlocContenu").css("height", (jQuery("#ColonneLaterale").height() - 315) + "px");
        }
    }


    // -----------------------------------------------------------------------------------------------------------------
    // Ajustements dynamiques au menu principal ------------------------------------------------------------------------
    // -----------------------------------------------------------------------------------------------------------------
    menuTotalWidth = jQuery("#MenuPrincipal").width();
    menuWidth = jQuery("#MenuPrincipal ul").width();
    if(menuWidth < menuTotalWidth){
        menuPosition = Math.floor((menuTotalWidth - menuWidth) / 2);
        jQuery("#MenuPrincipal ul").css("margin-left", menuPosition);
    }


    // -----------------------------------------------------------------------------------------------------------------
    // Choix de la langue ----------------------------------------------------------------------------------------------
    // -----------------------------------------------------------------------------------------------------------------
    jQuery(".LangueSelectionnee").click(function(){
        jQuery("#ChoixLangue").toggleClass("Ouvert");
        jQuery(document).bind("click", function() {
            jQuery("#ChoixLangue").removeClass("Ouvert");
            jQuery(this).unbind("click");
        });
        return false;
    });


    // -----------------------------------------------------------------------------------------------------------------
    // Appels des tickers ----------------------------------------------------------------------------------------------
    // -----------------------------------------------------------------------------------------------------------------
    if(jQuery(".CadreImage").length == 1){
        jQuery(".CadreImage").thicker({
            idThickerPrevious: ".BoutonPrecedent",
            idThickerNext: ".BoutonSuivant",
            effect: 'fade',
            delay: 180000,
            speed: 400,
        });
    }

    if(jQuery(".ConteneurPartenaires").length == 1){
        jQuery(".ConteneurPartenaires").thicker({
            idThickerPrevious: ".BoutonPrecedent",
            idThickerNext: ".BoutonSuivant",
            effect: 'slide',
            delay: 6000,
            speed: 400
        });
    }

    if(jQuery(".ConteneurInformation").length == 1){
        jQuery(".ConteneurInformation").thicker({
            idThickerGoTo: ".BoutonControleur",
            effect: 'fade',
            delay: 6000,
            speed: 400
        });
    }

    jQuery(".CibleServices").each(function(){
        var text = jQuery(this).children("p");
        var totalHeight = text.height() - 7;
        var textHeight = jQuery(text).children("span").height();
        var heightDiff = Math.round((totalHeight - textHeight) / 2);
        jQuery(text).children("span").css("padding-top", heightDiff);
    });


    // -----------------------------------------------------------------------------------------------------------------
    // Ouverture/fermeture de la carte du monde ------------------------------------------------------------------------
    // -----------------------------------------------------------------------------------------------------------------

    // Ouverture/fermeture de la carte Ã  partir d'un clic sur la carte miniature
    jQuery(".SelectionCarte").click(function(){
        jQuery(".SelectionCarte").toggleClass ("On");
        jQuery("#BlocSelectionBureau").addClass("On");
        jQuery("#WrapperCarte").slideToggle(200);
        return false;
    });

    // Fermeture de la carte Ã  partir du bouton Â« Fermer la carte Â»
    jQuery(".FermetureCarte").click(function(){
        jQuery("#WrapperCarte").slideUp(200, function(){
            jQuery(".SelectionCarte").removeClass("On");
            jQuery("#BlocSelectionBureau").removeClass("On");
        });
        return false;
    });

    // Tooltip
    $("#Carte").children("a").tooltip({
        track: true,
        delay: 0,
        showURL: false,
        showBody: " - ",
        fade: 250
    });


    // -----------------------------------------------------------------------------------------------------------------
    // SÃ©lection d'un bureau  ------------------------------------------------------------------------------------------
    // -----------------------------------------------------------------------------------------------------------------

    // Ouverture/fermeture du menu dÃ©roulant
    jQuery(".SelectionBureau").click(function(){
        jQuery(".MenuDeroulantBureau").toggleClass("On");
        jQuery(document).bind("click", function(){
            jQuery(".MenuDeroulantBureau").removeClass("On");
            jQuery(this).unbind("click");
        });
        return false;
    });

    // SÃ©lection d'une rÃ©gion Ã  partir du menu dÃ©roulant
    jQuery("a",".MenuDeroulantBureau").click(function(){
        jQuery("a.SelectionBureau").html(jQuery(this).text());
        jQuery(".MenuDeroulantBureau").removeClass("On");
        setRegion(jQuery("span.RegionSelectionnee"), jQuery(this).text(), jQuery(this).attr("class"));
    });

    // SÃ©lection Ã  partir du lien Â« Toutes les rÃ©gions Â»
    jQuery(".BoutonToutesRegions").hover(
      function(){
        jQuery("#Carte").css("background-image","url(" + window.__media_prefix__ + "img/carte/ZoneMonde.png)"); },
      function(){ jQuery("#Carte").css("background-image","url(" + window.__media_prefix__ + "img/Img_CarteMonde.png)");
     });

    jQuery(".BoutonToutesRegions").click(function(){
        setRegion(jQuery("span.RegionSelectionnee"), "International", "International");
        setRegion(jQuery("a.SelectionBureau"), "International", "International");
    });

    // Affichage des rÃ©gions sur la carte + action sur le clic
    jQuery("#Carte").children("a").mouseover(function(){
        var zoneHighlight = jQuery(this).attr("class").substr(4);
        jQuery("#Carte").css("background-image","url(" + window.__media_prefix__ + "img/carte/Zone"+ mapZones[zoneHighlight] +".png)");
        jQuery(this).click(function(){
            setRegion(jQuery("a.SelectionBureau"), jQuery(this).text(), mapZones[zoneHighlight]);
            setRegion(jQuery("span.RegionSelectionnee"), jQuery(this).text(), mapZones[zoneHighlight])
        });
    });

    // RÃ©initialisation de la carte sur le mouseout
    jQuery("#Carte").children("a").mouseout(function(){
        jQuery("#Carte").css("background-image","url(" + window.__media_prefix__ + "img/Img_CarteMonde.png)");
    });
});

function setRegion(field, region, cssClass){
    jQuery(field).html(region);
    selectedRegion = cssClass;
    jQuery("span.RegionSelectionnee").attr("id", cssClass);
}

//Tab onglet

$(document).ready(function() {
						   
	$("#id_adresse").addClass("TxtBox");
						   
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

/*BACK TO TOP*/
            // hide #back-top first
            $("#back-top").hide();

            // fade in #back-top
            $(function () {
                $(window).scroll(function () {
                    if ($(this).scrollTop() > 250) {
                        $('#back-top').fadeIn();
                    } else {
                        $('#back-top').fadeOut();
                    }
                });

                // scroll body to 0px on click
                $('#back-top a').click(function () {
                    $('body,html').animate({
                        scrollTop: 0
                    }, 500);
                    return false;
                });
            });

/*MENU*/
            $('#MenuPrincipal li').hover(function(){
                    $(this).find('ul').css({visibility: "visible",display: "none"}).fadeIn(310); // effect 1
                },function(){
                    $(this).find('ul').css({visibility: "hidden"});
            });

});