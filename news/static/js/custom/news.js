/**
 * Created by roxnairani on 7/23/14.
 */

$(document).ready(function(){

    var espn_api_key = "8ac49etstvkvnawwndz8g2fa";
    var npr_api_key = "MDE1MjA0OTM3MDE0MDYyMjc3NzAzZjE0Nw001";
    var usa_api_key = "dyctq75jnx3s4xk5hzdvk49y";
    var guardian_api_key = "22qv4ej7rnuhxsyzvxxkgzwm";
    var crunchbase_api_key = "2cxs6arxc2dnx6u4tnbcnaqb";
//    var nytimes_api_key = "6bdaaf4dc90f357bd0e3eec43415f288:15:69599771";

    function loadHTML(newsList){
        $('#pageBody').html("");
        $('#search').html("");

        for (var i=0; i<newsList.length; i++){
            $('#pageBody').append(
                '<div class="panel-group" id="accordion">'+
                    '<div class="panel panel-default">' +
                        '<div class="panel-heading">'+
                            '<h4 class="panel-title">' +
                                '<a data-toggle="collapse" data-parent="#accordion" href="#collapse'+i+'">'+newsList[i].title+'</a>'+
                            '</h4>' +
                        '</div>'+
                        '<div id="collapse'+i+'" class="panel-collapse collapse in">'+
//                               '<img src="'+newsList[i].image_url+' class="news-images"><br>'+
                               '<div class="panel-body">'+newsList[i].abstract+'</div><br>'+
                               '<a class="news-read-more" href="'+newsList[i].web_url+'">Read more</a>'+
                        '</div>'+
                    '</div>'+
                '</div>'
            );
        }
    }


    // ESPN //

    function parseESPNData(news_articles){
        var newsList = [];
        for (var i = 0; i < news_articles.headlines.length; i++) {
                var newsArticle = {};
                var article = news_articles.headlines[i];
                newsArticle.identifier = article.id;
                newsArticle.title = article.title;
                newsArticle.abstract = article.description;
                newsArticle.published_date = article.published;
                newsArticle.web_url = article.links.web.href;
                newsArticle.image_url = article.images[0].url;
                newsList.push(newsArticle);
            }
        $('#pageHeader').text("").text("ESPN");
        $('#sourceLogo').attr('src', '/static/img/ESPN.jpeg');
        loadHTML(newsList);
    }

    $.ajax({
        url: "http://api.espn.com/v1/sports/news/headlines/top?apikey=" + espn_api_key,
        type: "GET",
        dataType: "jsonp",
        success: function (news_articles) {
            $('li#espn').on('click', function() {
                console.log(news_articles);
                parseESPNData(news_articles);
            });
        },
        error: function (error_message) {
            console.log(error_message);
        }
    });


    // NPR //

    function parseNPRData(news_articles){
        var newsList = [];
        for (var i = 0; i < news_articles.list.story.length; i++) {
                var newsArticle = {};
                var article = news_articles.list.story[i];
                newsArticle.identifier = article.id;
                newsArticle.title = article.title.$text;
                newsArticle.abstract = article.teaser.$text;
                newsArticle.published_date = article.pubDate.$text;
                newsArticle.web_url = article.link[0].$text;
//                newsArticle.image_url = article.link[0].$text;
                newsList.push(newsArticle);
            }
        $('#pageHeader').text("").text("NPR");
        $('#sourceLogo').attr('src', '/static/img/npr.jpg');
        loadHTML(newsList);
    }


    $.ajax({
        url: "http://api.npr.org/query?id=1001&output=JSON&apikey=" + npr_api_key,
        type: "GET",
        dataType: "jsonp",
        success: function (news_articles) {
            $('li#npr').on('click', function() {
                parseNPRData(news_articles);
            });
        },
        error: function (error_message) {
            console.log(error_message);
        }
    });


    // USA TODAY //

    function parseUSAData(news_articles){
        var newsList = [];
        for (var i = 0; i < news_articles.stories.length; i++) {
                var newsArticle = {};
                var article = news_articles.stories[i];
//                newsArticle.identifier = article.id;
                newsArticle.title = article.title;
                newsArticle.abstract = article.description;
                newsArticle.published_date = article.pubDate;
                newsArticle.web_url = article.link;
//                newsArticle.image_url = article.images[0].url;
                newsList.push(newsArticle);
            }
        $('#pageHeader').text("").text("USA Today");
        $('#sourceLogo').attr('src', '/static/img/USAToday.jpeg');
        loadHTML(newsList);
    }


    $.ajax({
        url: "http://api.usatoday.com/open/articles/topnews?encoding=json&api_key=" + usa_api_key,
        type: "GET",
        dataType: "json",
        success: function (news_articles) {
            $('li#usatoday').on('click', function() {
                parseUSAData(news_articles);
            });
        },
        error: function (error_message) {
            console.log(error_message);
        }
    });


// GUARDIAN //

    function parseGuardianData(news_articles){
        var newsList = [];
        for (var i = 0; i < news_articles.response.results.length; i++) {
                var newsArticle = {};
                var article = news_articles.response.results[i];
                newsArticle.identifier = article.id;
                newsArticle.title = article.webTitle;
                newsArticle.abstract = article.webTitle;
                newsArticle.published_date = article.pubDate;
                newsArticle.web_url = article.webUrl;
//                newsArticle.image_url = article.images[0].url;
                newsList.push(newsArticle);
            }
        $('#pageHeader').text("").text("The Guardian");
        $('#sourceLogo').attr('src', '/static/img/Guardian.jpg');
        loadHTML(newsList);
    }


    $.ajax({
        url: "http://content.guardianapis.com/search?date-id=date%2Flast7days&format=json&api_key=" + guardian_api_key,
        type: "GET",
        dataType: "jsonp",
        success: function (news_articles) {
            $('li#guardian').on('click', function() {
                console.log(news_articles);
                parseGuardianData(news_articles);
            });
        },
        error: function (error_message) {
            console.log(error_message);
        }
    });


    // CRUNCHBASE //

    function parseCrunchbaseData(news_articles){
        var newsList = [];
        for (var i = 0; i < news_articles.results.length; i++) {
                var newsArticle = {};
                var article = news_articles.results[i];
//                newsArticle.identifier = article.id;
                newsArticle.title = article.name+' ('+article.description+')';
                newsArticle.abstract = article.overview;
//                newsArticle.published_date = article.pubDate;
                newsArticle.web_url = article.crunchbase_url;
//                newsArticle.image_url = article.image.available_sizes[0].1;
                newsList.push(newsArticle);
            }

        $('#pageHeader').text("").text("Crunchbase");
        $('#sourceLogo').attr('src', '/static/img/crunchbase.jpeg');
        loadHTML(newsList);
        $('#search').html("<input type='text' id='searchTerm' style='margin-left: 15px; width: 200px' placeholder='Search company name'></input>"+
                            "<button id='searchCrunchbase' style='margin-left: 5px;' class='btn btn-success' type='submit'>Search</button>");
    }

    var searchTerm = "startups";

    $.ajax({
        url: "http://api.crunchbase.com/v/1/search.js?query="+searchTerm+"&api_key=" + crunchbase_api_key,
        type: "GET",
        dataType: "jsonp",
        success: function (news_articles) {
            $('li#crunchbase').on('click', function() {
                parseCrunchbaseData(news_articles);
            });
        },
        error: function (error_message) {
            console.log(error_message);
        }
    });

    $(document).on('click', '#searchCrunchbase', function(){
        searchTerm = $('#searchTerm').val();
        $.ajax({
            url: "http://api.crunchbase.com/v/1/search.js?query="+searchTerm+"&api_key=" + crunchbase_api_key,
            type: "GET",
            dataType: "jsonp",
            success: function (news_articles) {
                parseCrunchbaseData(news_articles);
            },
            error: function (error_message) {
                console.log(error_message);
            }
        });
    });






//    // NY TIMES //

//    $.ajax({
//        url: "http://api.nytimes.com/svc/mostpopular/v2/mostemailed/all-sections/1.json??api-key="+nytimes_api_key,
//        type: "GET",
//        beforeSend: function(xhrObj){
//                xhrObj.setRequestHeader("Access-Control-Allow-Origin","http://api.nytimes.com");
//        },
//        dataType: "json",
//        contentType: "application/x-www-form-urlencoded; charset=utf-8",
//        crossDomain: true,
////        processData: true,
//        jsonpCallback: $.getJSON(),
//        jsonp: "callback",
//        success: function(news_articles){
//            console.log(news_articles);
//        },
//        error: function(error_message){
//            console.log(error_message)
//        }
//
//    });

});