jQuery.fn.thicker = function(options) {

    var actionBlocker = false;

    var settings = {
        childrens: '.Item',
        speed: 6000,
        delay: 500,
        idThickerStart: null,
        idThickerStop: null,
        idThickerPrevious: null,
        idThickerNext: null,
        idThickerGoTo: null,
        idThickerGoToActiveClass: 'On',
        effect: 'slide'
    };

    if (options)
        jQuery.extend(settings, options);

    var itemsList = jQuery(this).children(settings.childrens);
    var index = -1;
    var indexToMoveOut = -1;
    var timer = null;
    var thickerContainer = jQuery(this);
    var itemWidth = null;
    var itemHeight = null;
    var moveObjectOut = false;

    var init = function() {
        itemWidth = thickerContainer.width();
        itemHeight = thickerContainer.height();

        $(".ConteneurEnBref, .ConteneurPartenaires").mouseover(function() {
            stopAnimation();
        });

        $(".ConteneurEnBref, .ConteneurPartenaires").mouseout(function() {
            timer = setInterval(showNextItem, settings.delay);
        });

        if (settings.idThickerStart)
            jQuery(settings.idThickerStart).click(function() {
                showNextItem();
                timer = setInterval(showNextItem, settings.delay);
                return false;
            });

        if (settings.idThickerStop)
            jQuery(settings.idThickerStop).click(function() {
                stopAnimation();
                return false;
            });

        if (settings.idThickerPrevious)
            jQuery(settings.idThickerPrevious).click(function() {
                if (!actionBlocker) {
                    actionBlocker = true;
                    stopAnimation();
                    showPreviousItem();
                    timer = setInterval(showNextItem, settings.delay);
                }
                return false;
            });

        if (settings.idThickerNext)
            jQuery(settings.idThickerNext).click(function() {
                if (!actionBlocker) {
                    actionBlocker = true;
                    stopAnimation();
                    showNextItem();
                    timer = setInterval(showNextItem, settings.delay);
                }
                return false;
            });

        if (settings.idThickerGoTo)
            jQuery(settings.idThickerGoTo).click(function() {
				if (jQuery(this).attr("rel"))
					stopAnimation();
                showItem(jQuery(this).attr("rel") - 1);
                timer = setInterval(showNextItem, settings.delay);
                return false;
            });

        function stopAnimation() {
            if (timer != null)
                clearInterval(timer);
        }

        function setItemsListIndexes(backward) {
            if (backward == true) {
                if (index > 0)
                    index--;
                else
                    index = itemsList.length - 1;

                indexToMoveOut = index + 1;
                if (index == itemsList.length - 1)
                    indexToMoveOut = 0;
            } else {
                if (index < itemsList.length - 1)
                    index++;
                else
                    index = 0;

                indexToMoveOut = index - 1;
                if (index == 0)
                    indexToMoveOut = itemsList.length - 1;
            }
			//if (jQuery(".Controleur").length == 1) jQuery(".BoutonControleur").removeClass("On");
			//infoChanger(index +1);
        }

        function setItemsListZIndex() {
            for (i = 0; i < itemsList.length; i++) {
                jQuery(itemsList[i]).css('z-Index', 1);
            }
            jQuery(itemsList[indexToMoveOut]).css('z-Index', 2);
            jQuery(itemsList[index]).css('z-Index', 3);
        }

        function showNextItem() {
			setItemsListIndexes();
            setItemsListZIndex();
            switch (settings.effect) {
                case 'slide':
                    moveItem('-' + itemWidth, 0, itemWidth, jQuery(itemsList[index]), jQuery(itemsList[indexToMoveOut]));
                    break;
                case 'fade':
                    jQuery(itemsList[index]).fadeIn(settings.speed, unblockAction);
                    setTimeout(function() { jQuery(itemsList[indexToMoveOut]).hide(); }, settings.speed);
                    break;
                default:
                    alert('Invalid effect');
            }
            setSelectedLink(index);
            moveObjectOut = true;
        }

        function showPreviousItem() {
            setItemsListIndexes(true);
            setItemsListZIndex();
            switch (settings.effect) {
                case 'slide':
                    moveItem(itemWidth, 0, '-' + itemWidth, jQuery(itemsList[index]), jQuery(itemsList[indexToMoveOut]));
                    break;
                case 'fade':
                    jQuery(itemsList[index]).fadeIn(settings.speed, unblockAction);
                    setTimeout(function() { jQuery(itemsList[indexToMoveOut]).hide(); }, settings.speed);
                    break;
                default:
                    alert('Invalid effect');
            }
            setSelectedLink(index);
        }

        function showItem(selectedIndex) {
            if (index != -1 && index != selectedIndex) {
                indexToMoveOut = index;
                index = selectedIndex;
                setItemsListZIndex();
                switch (settings.effect) {
                    case 'slide':
                        moveItem(itemWidth, 0, '-' + itemWidth, jQuery(itemsList[index]), jQuery(itemsList[indexToMoveOut]));
                        break;
                    case 'fade':
                        jQuery(itemsList[index]).fadeIn(settings.speed, unblockAction);
                        setTimeout(function() { jQuery(itemsList[indexToMoveOut]).hide(); }, settings.speed);
                        break;
                    default:
                        alert('Invalid effect');
                }
                setSelectedLink(index);
            }
        }

        function setSelectedLink(selectedIndex) {
            if (settings.idThickerGoTo) {
                jQuery(settings.idThickerGoTo).removeClass(settings.idThickerGoToActiveClass);
                jQuery(settings.idThickerGoTo).eq(selectedIndex).addClass(settings.idThickerGoToActiveClass);
            }
        }

        function moveItem(itemToShowStart, itemToShowEnd, itemToHideEnd, itemToShow, itemToHide) {
            itemToShow.css({ right: itemToShowStart + 'px' });
            itemToShow.show();
            itemToShow.animate({ right: itemToShowEnd + 'px' }, settings.speed, null, unblockAction);
            if (moveObjectOut && itemToHide)
                itemToHide.animate({ right: itemToHideEnd + 'px' }, settings.speed);
        }

        function unblockAction() {
            actionBlocker = false;
        }

        showNextItem();
        if (itemsList.length > 1) {
            timer = setInterval(showNextItem, settings.delay);
        }
    };

    init();
};