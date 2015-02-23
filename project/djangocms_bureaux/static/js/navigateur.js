/*----------------------------------------------------------------------------//
// Detection Navigateurs et JavaScript  --------------------------------------//
//----------------------------------------------------------------------------//
// Version : 1.0
// Date    : 2 mars 2010
//----------------------------------------------------------------------------*/
/*
    Application :
    --------------------------
    1. Il faut seulement mettre la fonction InitOldBrowser();
       dans le document.ready du fichier site.js

    2. Ne pas oublier de mettre ce code à l'emplacement désiré pour le message:
    ...
    <!-- Boite Erreur Navigateur -->
    <noscript style="display:block;">
        <iframe scrolling="no" frameborder="0" style="border:0px; width:100%; overflow:hidden; margin:0px; height:92px;" src="/includes/navigateur/noscript_FR.html"></iframe>
    </noscript>
    <div id="BoxBrowserNotSupported"></div>
    ...

    3. Ne pas oublier de mettre le code (FR/EN) de langue par programmation sur
       le iframe si votre site est bilingue.

    4. Demandez au Programmeur d'ajouter ceci dans le robot.txt :
       Disallow: /includes/navigateur/

*/

/*----------------------------------------------------------------------------*/
// Detection des vieux navigateurs
/*----------------------------------------------------------------------------*/
function OldBrowserDetect() {
    if(jQuery.browser.mozilla && jQuery.browser.version.substr(0,3) < "1.9")//Firefox 2.0 et moins
        return true;
    else if (jQuery.browser.msie && jQuery.browser.version < "7.0")//IE 6.0 et moins
        return true;
    else if (jQuery.browser.safari && jQuery.browser.version <= "418.8")//Safari 2.0.4 et moins
        return true;
    else if (jQuery.browser.opera && jQuery.browser.version.substr(0,1) < "9")//Safari 2.0.4 et moins
        return true;
    else
        return false;
}

/*----------------------------------------------------------------------------*/
// Initialisation du message qui sera affiché à l'utilisateur
/*----------------------------------------------------------------------------*/
function InitOldBrowser() {
    var cookieOldBrowser = getcookie("OldBrowserError");
    if (OldBrowserDetect() && cookieOldBrowser == "") {
        // Message par langue, detection de la langue sur le BODY
        if (jQuery("body").attr("id") == "lang-EN") {
            var txtLang = "en";
            var txtCloseBtn = "Close this alert";
            var txtTitle = "Your browser is not supported!";
            var txtDescription = "For a better web experience, take the time to update your browser.";
            var txtDownload = "Download";
        } else {
            var txtLang = "fr";
            var txtCloseBtn = "Fermer cette alerte";
            var txtTitle = "Votre navigateur n'est pas support&eacute;&nbsp;!";
            var txtDescription = "Pour une meilleure exp&eacute;rience web, prenez le temps de mettre votre navigateur &agrave; jour parmi un de&nbsp;ceux-ci.";
            var txtDownload = "T&eacute;l&eacute;charger";
        }
        var box = "<div style='border: 1px solid #CA1600; background:#fffed7; text-align: center; clear: both; height: 90px; position: relative;'>";
        box += "<div style='position: absolute; right: 3px; top: 3px; font-family: courier new; font-weight: bold;'><a href='#' onclick='javascript:CloseOldBrowser(this);'><img src='../includes/navigateur/images/Bt_Fermer.gif' style='border: none;' alt='"+txtCloseBtn+"'/></a></div>";
        box += "<div style='width: 600px; margin: 0 auto; text-align: left; padding: 0 0 0 95px; overflow: hidden; color: black; background:#fffed7 url(../includes/navigateur/images/Ico_Erreur.png) no-repeat 15px 18px; height:90px;'>";
        box += "<div style='width: 275px; float: left; font-family: Arial, sans-serif;'>";
        box += "<div style='font-size: 14px; font-weight: bold; margin-top: 12px;'>"+txtTitle+"</div>";
        box += "<div style='font-size: 12px; margin-top: 6px;'>"+txtDescription+"</div>";
        box += "</div>";
        box += "<div style='width: 75px; float: left;'><a href='http://www.mozilla.com/" + txtLang + "/' target='_blank'><img src='../includes/navigateur/images/Img_Firefox.gif' style='border: none;' alt='" + txtDownload + " Firefox 3.5'/></a></div>";
        box += "<div style='width: 75px; float: left;'><a href='http://www.microsoft.com/downloads/details.aspx?FamilyID=341c2ad5-8c3d-4347-8c03-08cdecd8852b&DisplayLang=" + txtLang + "' target='_blank'><img src='../includes/navigateur/images/Img_IE.gif' style='border: none;' alt='" + txtDownload + " Internet Explorer 8'/></a></div>";
        box += "<div style='width: 73px; float: left;'><a href='http://www.apple.com/" + (txtLang=='fr' ? 'fr/' : '') + "safari/download/' target='_blank'><img src='../includes/navigateur/images/Img_Safari.gif' style='border: none;' alt='" + txtDownload + " Safari 4'/></a></div>";
        box += "<div style='float: left;'><a href='http://www.google.com/chrome?hl=" + txtLang + "' target='_blank'><img src='../includes/navigateur/images/Img_Chrome.gif' style='border: none;' alt='" + txtDownload + " Google Chrome'/></a></div>";
        box += "</div>";
        box += "</div>";
        jQuery("#BoxBrowserNotSupported").html(box);
    }
}

/*----------------------------------------------------------------------------*/
// Fermeture du message
/*----------------------------------------------------------------------------*/
function CloseOldBrowser(obj) {
    obj.parentNode.parentNode.style.display='none';
    putcookie("OldBrowserError", "true", 30);
    return false;
}

/*----------------------------------------------------------------------------*/
// Fonctions pour la gestion des cookies
/*----------------------------------------------------------------------------*/
function putcookie(name, value, days) {
  var expire = "";
  if(days != null) {
    expire = new Date((new Date()) + days);
    expire = "; expires=" + expire.toGMTString()+";";
  }
  document.cookie = name + "=" + escape(value) + expire + "path=/";
}
function getcookie(name) {
  var cookieValue = "";
  var search = name + "=";
  if(document.cookie.length > 0) {
    offset = document.cookie.indexOf(search);
    if (offset != -1) {
      offset += search.length;
      end = document.cookie.indexOf(";", offset);
      if (end == -1) end = document.cookie.length;
      cookieValue = unescape(document.cookie.substring(offset, end))
    }
  }
  return cookieValue;
}
