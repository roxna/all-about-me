/**
 * Created by roxnairani on 7/29/14.
 */


$(document).ready(function() {

    if(window.location.pathname == '/dashboard/'){
        $('nav #side-menu').children().css('display', 'block !important');
    }
    else{
        $('nav #side-menu').children().not(':first').hide();
    }

});