$(document).ready(function() {

    var dots_string = '';
    for (i = 0; i < 30000; i++) {
        dots_string += '.';
    }

    $('.selectors').html(dots_string);

    $('img').click(function(e){
        e.preventDefault();
        var url = $(this).attr('href');
        //console.log('++ url: %s', url);
        //window.open(url, 'window name', 'toolbar=yes, menubar=yes, resizable=yes');
        window.location = url;
        return false;
    });

});




