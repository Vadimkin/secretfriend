$(document).ready(function(){
	$('.agreeRules').on('change', function() {
		if($(this).prop("checked") == false) {
			$('.btn-sendData').attr('disabled', 'disabled');
		} else {
			$('.btn-sendData').removeAttr('disabled');
		}
	});

	$('.js-signForm').on('submit', function() {
		alert("test");
		return false;
	});
});