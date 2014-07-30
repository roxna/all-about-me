/**
 * Created by roxnairani on 7/24/14.
 */


$(document).ready(function() {


    $('#twitter').on('click', function(){
        $('#pageHeader').text("Twitter");
        $('#pageBody').html("");
        $('#sourceLogo').attr('src', '/static/img/twitter.jpeg');
        $('#search').html('<div class="form-group input-group">'+
                            '<span class="input-group-addon">@</span>'+
                             "<input type='text' class='form-control' id='searchTerm' style='width: 300px' placeholder='Enter twitter handle to follow'></input>"+
                             "<button id='searchTwitter' style='margin-left: 5px; display: inline-block;' class='btn btn-primary' type='submit'>Show me the tweets</button>"+
                          '</div>');
        $.ajax({
            url: '/twitter/',
            type: 'GET',
            dataType: 'html',
            success: function(tweets) {
                $('#pageBody').html(tweets);
            },
            error: function(error_response) {
                console.log(error_response);
            }
        });

        $('#searchTwitter').on('click', function(){
            var searchTerm = $('#searchTerm').val();
            $.ajax({
                url: '/twitter/',
                type: 'POST',
                dataType: 'html',
                data: JSON.stringify(searchTerm),
                success: function(tweets) {
                    $('#pageBody').html(tweets);
                },
                error: function(error_response) {
                    console.log(error_response);
                }
            });
        });
    });

});