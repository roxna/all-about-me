/**
 * Created by roxnairani on 7/25/14.
 */


$(document).ready(function() {

    var vimeo_api_key = "c833e102672739816c1414409da1b0c1";

    function loadImageHTML(content){
        $('#pageHeader').text("");
        $('#pageBody').html(
            '<h4 class="panel-title" id="title" data-title="'+content.title+'">'+content.title+'</h4>' +
            '<div id="description" data-description=""></div>' +
            '<img id="url" data-url="'+content.url+'" src="'+content.url+'"/>'
            );
        }

    function loadVideoHTML(content){
        $('#pageHeader').text("");
        $('#pageBody').html(
            '<h4 class="panel-title" id="title" data-title="'+content.title+'">'+content.title+'</h4><br>' +
            '<div id="description" data-description="'+content.description+'>'+content.description+'</div>' +
            '<video width="640" height="480" controls autoplay>'+
                '<source id="url" data-url="'+content.url+'" src="'+content.url+'"/> <em>Your browser doesn\'t support video</em>'+
            '</video>'
            );
        }


    // CHANGE FAVORITES BUTTON ON CLICK //
    $(document).on('click', '.favorite', function(){
       $(this).attr('src', '/static/img/non-favorite.jpeg');
    });

    $(document).on('click', '.not_favorite', function(){
       $(this).attr('src', '/static/img/favorite.jpeg');
    });


    // I'm a bit confused why both of these blocks have a favorite and unfavorite clause
    // Doesn't one add a favorite and one unfavorites?
    // If that's the case then can't you just unfavorite via the PK of the Entertainment in the DB?

    // ADDS / REMOVES ENTERTAINMENT PIECE FROM FAVORITES ON CLICK ON DASHBOARD PAGES //
    $(document).on('click', '#favorite-icon-entertainment', function(){
        favorite_entertainment = {};
        favorite_entertainment.title = $(this).parents('#pageBody').find('#title').data('title');
        favorite_entertainment.url = $(this).parents('#pageBody').find('#url').data('url');
        favorite_entertainment.description = $(this).parents('#pageBody').find('#description').data('description');
        favorite_entertainment.source = $(this).parents('.row').find('#pageHeader').data('source');
        favorite_entertainment.origin = '/dashboard/';
        console.log(favorite_entertainment);
        if($(this).hasClass("not_favorite")){
            $.ajax({
                url: "/add_favorite_entertainment/",
                type: "POST",
                dataType: "html",
                data: JSON.stringify(favorite_entertainment),
                success: function(favorite){
                    console.log(favorite);
                },
                error: function(error_message){
                    console.log(error_message);
                }
            });
        }
        if($(this).hasClass("favorite")){
            $.ajax({
                url: "/remove_favorite_entertainment/",
                type: "POST",
                dataType: "html",
                data: JSON.stringify(favorite_entertainment),
                success: function(favorite){
                    console.log(favorite);
                },
                error: function(error_message){
                    console.log(error_message);
                }
            });

        }
        $(this).toggleClass("favorite").toggleClass("not_favorite");
    });


    // ADDS / REMOVES ENTERTAINMENT PIECE FROM FAVORITES ON CLICK ON FAVORITES PAGE //
    $(document).on('click', '#favorite-icon-entertainment-saved', function(){
        favorite_entertainment = {};
        favorite_entertainment.title = $(this).parent().find('#title').data('title');
        favorite_entertainment.url = $(this).parent().find('#url').data('url');
        favorite_entertainment.description = $(this).parents('#favoritesBody').find('#description').data('description');
        favorite_entertainment.source = $(this).parents('#favoritesBody').find('#source').data('source');
        favorite_entertainment.origin = '/favorites/';
        console.log(favorite_entertainment);
        if($(this).hasClass("not_favorite")){
            $.ajax({
                url: "/add_favorite_entertainment/",
                type: "POST",
                dataType: "html",
                data: JSON.stringify(favorite_entertainment),
                success: function(favorite){
                    console.log(favorite);
//                    location.reload();
                },
                error: function(error_message){
                    console.log(error_message);
//                    location.reload();
                }
            });
        }
        if($(this).hasClass("favorite")){
            $.ajax({
                url: "/remove_favorite_entertainment/",
                type: "POST",
                dataType: "html",
                data: JSON.stringify(favorite_entertainment),
                success: function(favorite){
                    console.log(favorite);
//                    location.reload();
                },
                error: function(error_message){
                    console.log(error_message);
//                    location.reload();
                }
            });

        }
        $(this).toggleClass("favorite").toggleClass("not_favorite");
    });


    // AJAX REQUESTS FOR ALL ENTERTAINMENT SITES //

    // XKCD
    function parseXKCDData(response){
        var comic = {};
        comic.identifier = response.num;
        comic.title = response.title;
        comic.description = response.alt;
        comic.published_date = response.year+"-"+response.month+"-"+response.day;
        comic.url = response.img;

        $('#pageHeader').data("source", "XKCD");
        $('#sourceLogo').attr('src', '/static/img/xkcd.png');
        loadImageHTML(comic);
        $('#pageBody').append(
                '<br><br><button id="randomComic" class="btn btn-primary">Random Comic</button>'+
                '<br><br><p><em> &nbsp Favorite</em>'+
                    '<img id="favorite-icon-entertainment" class="not_favorite" src="/static/img/non-favorite.jpeg"/>'+
                '</p>'
        );
    }

    $.ajax({
        url: "http://dynamic.xkcd.com/api-0/jsonp/comic/",
        type: "GET",
        dataType: "jsonp",
        success: function (response) {
            $('li#xkcd').on('click', function() {
                console.log(response);
                parseXKCDData(response);
            });
        },
        error: function (error_message) {
            console.log(error_message);
        }
    });

    $(document).on('click', '#randomComic', function(){
        var comicNum = Math.floor((Math.random() * 1500) + 1);
        $.ajax({
            url: "http://dynamic.xkcd.com/api-0/jsonp/comic/"+comicNum,
//            url: "http://dynamic.xkcd.com/random/comic/",
            type: "GET",
            dataType: "jsonp",
            success: function (response) {
                parseXKCDData(response);
            },
            error: function (error_message) {
                console.log(error_message);
            }
        });
    });


    // VIMEO
    function parseVimeoData(response){
        var video = {};
        video.identifier = response[0].id;
        video.title = response[0].title;
        video.description = response[0].description;
        video.published_date = response[0].upload_date;
        video.url = response[0].url;
        console.log(video.url);

        $('#pageHeader').data("source", "Vimeo");
        $('#sourceLogo').attr('src', '/static/img/vimeo.png');
        loadVideoHTML(video);
        $('#pageBody').append(
                '<br><br><button id="randomVideo" class="btn btn-primary">Random Video</button>'+
                '<br><br><p><em> &nbsp Favorite</em>'+
                    '<img id="favorite-icon-entertainment" class="not_favorite" src="/static/img/non-favorite.jpeg"/>'+
                '</p>'
        );
    }

    $.ajax({
        url: "http://vimeo.com/api/v2/video/"+50+".json",
        type: "GET",
        dataType: "jsonp",
        success: function (response) {
            $('li#vimeo').on('click', function() {
                console.log(response);
                parseVimeoData(response);
            });
        },
        error: function (error_message) {
            console.log(error_message);
        }
    });

    $(document).on('click', '#randomVideo', function(){
        videoNum = Math.floor((Math.random() * 800) + 1);
        $.ajax({
            url: "http://vimeo.com/api/v2/video/"+videoNum+".json",
            type: "GET",
            dataType: "jsonp",
            success: function (response) {
                parseVimeoData(response);
            },
            error: function (error_message) {
                console.log(error_message);
            }
        });
    });



});
