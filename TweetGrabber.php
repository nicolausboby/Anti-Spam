<?php 
    require_once('TwitterAPIExchange.php');
    $settings = array(
        'oauth_access_token' => "308341308-pOqDjwHk7l3EFxhnBzyqKUvEt5WTysVT1sC5CZOz",
        'oauth_access_token_secret' => "GWQHRBKOhgyoGvytmCOZcfB0RtDwiLBTOtDhmxWJW5jvF",
        'consumer_key' => "nLWttflYaVautIU9O24OqsASr",
        'consumer_secret' => "qG6InZ7QPx0KF6JR7f6Z3lZX3oHKJz6cMiaYcs9pszGHud2uaz"
    );
    $url = 'https://api.twitter.com/1.1/search/tweets.json';
    $requestMethod = 'GET';
    $getfields ='?q=xkcd'; // Masukkan query di sini
    $twitter = new TwitterAPIExchange($settings);
    echo $twitter->setGetfield($getfields)->buildOauth($url, $requestMethod)->performRequest();
?>