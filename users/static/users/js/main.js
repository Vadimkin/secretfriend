$(document).ready(function(){
	$('.agreeRules').on('change', function() {
		if($(this).prop("checked") == false) {
			$('.btn-sendData').attr('disabled', 'disabled');
		} else {
			$('.btn-sendData').removeAttr('disabled');
		}
	});

	$("#inputPhone").inputmask("(999) 999-99-99");

	$('.js-signForm').on('submit', function() {
		data = $(this).serialize();
//		$('.js-signForm input[type="text"]').each(function() {
//		    if($(this).val() == "") {
//		        $(this).focus().slideError();
//		        return false;
//		    }
//		})

        $.ajax({
            type: "POST",
            url: "/",
            data: data,
            success: function(result){
                if(result['status'] == 0) {
                    $("input[name='" + result['error_value'] + "']").focus().slideError();
                } else {
                    $(".js-signForm").html(result['data']);
                }

            }
        });

		return false;
	});

});

$.fn.slideError = function(){
	$(this).stop(true, true);
	$(this).css({position: 'relative'});
	for(x = 0; x < 100; x++) {
		l = (1 / (Math.pow (x, 1.25) / 20 + 0.5) - 0.05) * Math.sin (x/2);
		if (x < 70) {
			var speed = 10;
		} else {
			var speed = 5;
		}
		$(this).animate({left: l * 10}, speed);
	}
	$(this).focus();
	return true;
 };