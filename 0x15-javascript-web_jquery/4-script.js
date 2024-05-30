// toggles the class of the <header> element
// when the user clicks on the tag DIV#toggle_header:

$('div#toggle_header').click(function () {
	const header = $('header');
	if (header.hasClass('red')) {
        header.removeClass('red').addClass('green');
    } else {
        header.removeClass('green').addClass('red');
    }
});
