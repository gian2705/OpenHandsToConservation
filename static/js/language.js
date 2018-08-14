
$(document).ready(function() {
    $('#language_selector').change(function() {
        if ($(this).val() == 'kiswahili') {
            $('.english').css("display", "none");
            $('.kiswahili').css("display", "block");
        } else {

        }
    });
});