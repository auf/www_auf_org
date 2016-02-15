
// This code is from here: https://github.com/raysaagar/hcs-mailman-signup-tool
// Plus translation, unsubscribe and customization for the AUF
// Minus the insults ;)

$(document).ready(function(){
	$('#submit').click(subscribe);
	$('#close').click(resetForm);

	$('.mlist').click(
		function(event){
			if($(event.target).hasClass('icon-ok')){
				$(event.target).parent().parent().toggleClass('btn-success');
				$(event.target).parent().toggle();
			}
			else if($(event.target).hasClass('listname')){
				$(event.target).parent().toggleClass('btn-success');
				$(event.target).parent().children('.icons').toggle();
			}
			else{
				$(event.target).toggleClass('btn-success');
				$(this).children('.icons').toggle();
			}
		}
	);
});

function validEmail(emailAddress) {
    var pattern = new RegExp(/^((([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+(\.([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+)*)|((\x22)((((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(([\x01-\x08\x0b\x0c\x0e-\x1f\x7f]|\x21|[\x23-\x5b]|[\x5d-\x7e]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(\\([\x01-\x09\x0b\x0c\x0d-\x7f]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]))))*(((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(\x22)))@((([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.)+(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.?$/i);
    return pattern.test(emailAddress);
};

function resetForm(){
	$('#email').val('');
	$('#fullname').val('');
	$('#noneSelectedError').html('');
	$('#badEmailError').html('');

	selectedLists = $('.mlist.active');
	selectedLists.each(function(){
		$(this).removeClass('btn-success');
		$(this).removeClass('active');

		$(this).children('.icons').toggle();
	});
}


function subscribe() {

	var email = $('#email').val();
    if (!validEmail(email)){
        $('#badEmailError').html('<div id="badEmail" class="alert alert-error"> <a class="close" data-dismiss="alert">×</a><strong>Error! </strong>Invalid email, you noob.</div>');
        return;
    }
	var fullname = $('#fullname').val();

	var paramsArray = {
		"email" : email,
		"fullname":fullname
	};

	var lists = [];
	selectedLists = $('.mlist.active');
	if (selectedLists.length < 1) {
		$('#noneSelectedError').html('<div id="badEmail" class="alert alert-error"> <a class="close" data-dismiss="alert">×</a><strong>Error! </strong>Select at least one list.</div>');
		return
	}
	else
	{
		selectedLists.each(function(){lists.push($(this).children('.listname').html());});
	}
	for (var i in lists) {
		listName = lists[i].toLowerCase();
		var url = "https://listes.auf.org/mailman/subscribe/"+listName;
		var data = "email="+email+"&fullname="+fullname;
		$.ajax({
			type: "POST",
			url: url,
			data: data,
			dataType: 'json',
			success: function(data){
				// alert("nomnom");
				// alert(data);
			},
			//this fails by default
			error: function(data){
				//alert("/cry");
			}
		});
	}

	$('#myModal').modal('toggle');
	resetForm();
};
