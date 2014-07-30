/**
 * Created by roxnairani on 7/25/14.
 */


$(document).ready(function() {

    var vimeo_api_key = "c833e102672739816c1414409da1b0c1";

    function loadImageHTML(content){
        $('#pageBody').html(
            '<h4 class="panel-title">'+content.title+'</h4>' +
            '<img src="'+content.url+'"/>'
            );
        }

    function loadVideoHTML(content){
        $('#pageBody').html(
            '<h4 class="panel-title">'+content.title+'</h4><br>' +
            '<div>'+content.description+'</div>' +
            '<video width="640" height="480" controls autoplay>'+
                '<source src="'+content.url+'"/>'+
            '</video>'
            );
        }

    // XKCD

    function parseXKCDData(response){
        var comic = {};
        comic.identifier = response.num;
        comic.title = response.title;
        comic.description = response.alt;
        comic.published_date = response.year+"-"+response.month+"-"+response.day;
        comic.url = response.img;

        $('#pageHeader').text("XKCD");
        $('#sourceLogo').attr('src', '/static/img/xkcd.png');
        loadImageHTML(comic);
        $('#pageBody').append('<br><br><button id="randomComic" class="btn btn-primary">Random Comic</button>');
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

        $('#pageHeader').text("").text("Vimeo");
        $('#sourceLogo').attr('src', '/static/img/vimeo.png');
        loadVideoHTML(video);
        $('#pageBody').append('<br><br><button id="randomVideo" class="btn btn-primary">Random Video</button>');
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