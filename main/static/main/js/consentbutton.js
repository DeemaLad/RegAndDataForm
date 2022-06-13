$('#consent').click(function(){
	if ($(this).is(':checked')){
		$('#btn').removeAttr('disabled');
	} else {
		$('#btn').attr('disabled', 'disabled'); 
	}
});