const play_btn = document.querySelector('.buter')
const audio = document.querySelector('.audio')
var source = document.getElementById('audioSource');
let time = document.querySelector('.duration')
let tra = document.querySelector('.track')
let vol = document.querySelector('.slider_valume')
let name_and_name = document.querySelector('.block_name_song')
var module = document.querySelector(".block_playlist_text a");
let name_song = document.querySelector('.name_song')
let time_track = document.querySelectorAll('.time_track2, .time_track')
let time_track2 = document.querySelectorAll('.time_track')
let play_track = document.querySelectorAll('.buter_track2')
let track = document.createElement('audio');
track.setAttribute('preload', 'auto')
duration = track.duration;
valum = track.volume
currentTime = track.currentTime
track.volume = 0.3
let id_music = 1
$('.slider_valume').attr("value", track.volume * 100)
let song_index = 0
let Playing_song = false
let what_play = false
function load_songs(song) {
    audio.src = `${song}`
}
console.log(track)
let resize2 = false;
var burger_menu = document.querySelector('.burger_menu')
var fat = document.querySelector('.dell')
let burger_on = false
$(document).ready(function() {
    $(document).on('click', '.burg', function () {
//        console.log("burger")
        if (burger_on === false) {
//            console.log("burger false")
            burger_on = true;
            // burger_menu.style.display = '';
            $('.content_zone1').append('<ul class="burger_menu">\n' +
                '            <li><a href="profile.html">Профиль</a></li>\n' +
                            '<li><a>|</a></li>\n'+

                '            <li><a href="index.html">Главная</a></li>\n' +
                '<li><a>|</a></li>\n'+
                '            <li><a href="my_music.html">Моя музыка</a></li>\n' +

                '<li><a>|</a></li>\n'+
                '            <li><a href="artists.html">Артисты</a></li>\n' +

                '<li><a>|</a></li>\n'+
                '            <li><a href="magazine.html">Журнал</a></li>\n' +
                '<li><a>|</a></li>\n'+
                '            <li><a href="add_music.html">Добавить песню</a></li>\n' +
                '<li><a>|</a></li>\n'+
                '            <li><a href="add_news.html">Добавить статью</a></li>\n' +
                '<li><a>|</a></li>\n'+
                '            <li><a href="#audio">Плеер</a></li>\n' +
                '        </ul>');
        }else{
//            console.log("burger true")
            burger_on = false;
            $('.burger_menu').remove()
            // burger_menu.style.display = 'none'
        }
    })
})

function play_song(){
    console.log(track.duration);
//    track.load();
    track.addEventListener('canplay', function (){
        track.addEventListener('loadeddata', function (){
            track.currentTime = 30;
            track.play();
            });
        });
        };
//    track.play()
//    track.addEventListener('canplaythrough', isAppLoaded, false);

function getmetadata()
{
    console.log(12)
}
function pause_song(){
    track.pause()
}
function play_track_create(){
    track.pause()
}

duration = track.duration;


//console.log('num_song')
let time1 = document.querySelector('.slider')
let valuev = document.querySelector('.slider')
$(document).on("change",".slider_valume", function() {
    let vol = document.querySelector('.slider_valume')
    track.volume = Number(`0.${vol.value}`);

    // $(".slider_valume").attr("max", track.volume);
})

//$(".slider").on("change", function () {
//    console.log(322)
//    console.log($('.slider').val())
////    track.addEventListener('canplay', function() {
//////        track.currentTime = $('.slider').val();
////        track.currentTime == 163.29189
////        $(".slider").attr("max", track.duration);
////
////    });
//    track.currentTime = $('.slider').val();
//    console.log(track.currentTime)
//})
time1.addEventListener('click', function(event){

    console.log(duration)
    currentTime = 120;
    });
//    track.currentTime=40;
//        console.log($('.slider').val())
//        track.currentTime = $('.slider').val();

//})
//$(document).bind("click", ".slider", function () {
//    track.addEventListener('loadedmetadata', function (){
//
//        console.log($('.slider').val())
//        track.currentTime = $('.slider').val();
//        });
//})

const slider = document.querySelector(".slider");
let name_song_list = '';
let id_time = 0

function update_progress(e) {
    const {duration, currentTime} = e.srcElement
    $(".slider").attr("max", track.duration);
    // const progressPercent = (currentTime / duration) * 100
    slider.value = track.currentTime
//    console.log(slider.value)
    let seconds = slider.value%60 // Получаем секунды
    let minutes = slider.value/60%60
//    time_track2[id_time].innerHTML = `${Math.trunc(minutes)}:${seconds}`
    time_track[id_time].innerHTML = `${Math.trunc(minutes)}:${seconds}`

    $('.slider').attr("value", track.currentTime)
}

track.addEventListener('timeupdate', update_progress)
// auto next track
var song = []

let num_song = 0
let all_song_page = document.querySelectorAll('.buter_track2')
let track_mass = new Map()
for (var i = 0; i < all_song_page.length; i++) {
    song.push(`${all_song_page[i].value}`)
    track_mass.set(all_song_page[i].id, `${all_song_page[i].value}`)
//    console.log(all_song_page[i].value)
}
let track2 = document.querySelectorAll('.fuck_audio');

function pzdc(aud){
    aud.addEventListener('loadedmetadata', function() {
//            console.log(track.duration)
        });
}
//$("#play").mouseenter(function () {
//    for (var i = 0; i<song.length; i++){
//        track.src = song[1];
//        track.addEventListener('loadedmetadata', function() {
//
////            console.log(track)
////            console.log(i)
//            });
//            };
//});
//    for (var i = 0; i<song.length; i++){
//        track.src = song[i];
//        track.addEventListener('loadedmetadata', function() {
//            alert(audio.duration);
//            console.log(track)
//            console.log(i)
//            });
//
//
//    };
//    });
console.log(track_mass)
track.addEventListener('ended', function () {
//    console.log(id_music)
//    console.log(track_mass)
//    console.log(track_mass.get(`id_music`))
//    console.log('fucki')
//    console.log(id_music)
    for (var i =0; i < play_track.length; i++) {
        play_track[i].style.backgroundColor = "rgba(0,0,0,.0)";
    }
    id_music = Number(id_music) + 1;
    name_song_list = track_mass.get(`${id_music}`);
    console.log(id_music)
    if (name_song_list !== undefined) {
        $(".buter_track2, .playlist_play").empty();
        id_time+=1
        $(`.black_img #${id_music}`).append('<img class="play_track_img2" src="/static/profile_user/img/Stop.png">');
        play_track[id_music - 1].style.backgroundColor = "rgba(0,0,0,.5)";
        console.log(true);
        console.log(track.name_song_list)
        track.src = `${name_song_list}`;
        track.play();
    } else {
        id_time = 0
        id_music = 1
        name_song_list = track_mass.get(`${id_music}`);
        $(".buter_track2, .playlist_play").empty();

        $(`.black_img #${id_music}`).append('<img class="play_track_img2" src="/static/profile_user/img/Stop.png">');
        play_track[id_music - 1].style.backgroundColor = "rgba(0,0,0,.5)";

        console.log(false);
        track.src = `${name_song_list}`;
        track.play();
    }
});

var play_img = "/static/profile_user/img/Polygon12(2).png";
let id = 0
let play_song_real_life = false
$(document).on('click', '#play', function (){
    let play_playlist = document.getElementsByClassName('.playlist_play')

    if (what_play === true) {
        console.log(' 878732');
        if (Playing_song === false) {
            console.log(1);
            $(this).empty();
            // track.src = `audio/${this.value}.mp3`;
            play_song();
            id_time = this.id - 1;
            id = this.value
            Playing_song = true;
            $(lol).empty()
            $(lol).append('<img class="play_track_img2" src="/static/profile_user/img/Stop.png">');
            $('.playlist_play').empty()
            console.log(play_song_real_life)
            $(play_song_real_life).append('<img class="play_track_img2" src="/static/profile_user/img/Stop.png">');
            $(this).append('<img src="/static/profile_user/img/Stop.png">');
        } else {
            console.log(24);
            Playing_song = false;
            track.pause()
            $('.buter_track2').empty()
            // $(".playlist_play").css("backgroundColor", "rgba(0,0,0,.0)");
            $(lol).append(`<img class="play_track_img2" src=${play_img}>`);
            $('.playlist_play').empty()
            // play_playlist.style.backgroundColor = '';
            $(play_song_real_life).append(`<img class="play_track_img2" src=${play_img}>`);

            $("#play").empty();
            $("#play").append(`<img class="play_track_img2" src=${play_img}>`);
        }
    }else{

    }
})
let lol= false

$(document).on('click', '.buter_track2, .playlist_play', function (){
    if (play_song_real_life === false || play_song_real_life === this) {
        if (Playing_song === false) {
//            console.log(this.id);
            id_music = this.id
//            console.log(1);
            id_time = this.id - 1;
            $('.block_name_song').empty();
            name_and_name.innerHTML = "<p id='title1'>"+this.name+"</p>";
            $(this).empty();
            if (play_song_real_life === false) {
                track.src = `${this.value}`;
            }
            console.log(this.name)
            track.addEventListener('loadedmetadata', function(){

                loaded = true;
                play_song();
            });

            id = this.value
            console.log(track.currentTime)
//            console.log(id)
            Playing_song = true;
            play_song_real_life = this;
            $(this).append('<img class="play_track_img2" src="/static/profile_user/img/Stop.png">');
            $("#play").empty();
//            console.log(4);
            lol = this
            $("#play").append('<img src="/static/profile_user/img/Stop.png">');
            this.style.backgroundColor = "rgba(0,0,0,.5)";
            what_play = true

        } else {
//            console.log('Первая пауза')
//            console.log(2);
            $('.playlist_play').empty()
            $("#play").empty();
            $("#play").append(`<img class="play_track_img2" src=${play_img}>`);
            lol = this

            $(".buter_track2, .playlist_play").empty();
            this.style.backgroundColor = "";
//            console.log(2);
            id_music = this.id
            Playing_song = false;
            track.pause()

        }
    }else{
//        console.log(3);
        console.log('вторая пауза')
        $("#play").empty();
        lol = this
        $(".playlist_play").css("backgroundColor", "rgba(0,0,0,.0)");

        $("#play").append('<img src="/static/profile_user/img/Stop.png">');
        $(".buter_track2, .playlist_play").empty();
        $(this).append('<img class="play_track_img2" src="/static/profile_user/img/Stop.png">');
        for (var i =0; i < play_track.length; i++) {
            play_track[i].style.backgroundColor = "rgba(0,0,0,.0)";
        }
        this.style.backgroundColor = "rgba(0,0,0,.5)";

        track.pause()
        track.src = this.value;
        console.log(5);
        track.currentTime = 0;
        id_time = this.id -1;
        slider.value = track.currentTime
        console.log(slider.value)
        $('.slider').attr("value", track.currentTime)
        $('.block_name_song').empty();
        name_and_name.innerHTML = "<p id='title1'>"+this.name+"</p>";
        play_song()

//        console.log('второй плей')
        id_music = this.id
        play_song_real_life = this
        Playing_song = true
    }

});
$(function() {

    $(".buter_track2, .playlist_play").mouseenter(function () {
//        console.log(21)
        if (play_song_real_life === false || play_song_real_life === this) {

            if (Playing_song === false) {
            lol = this
            $(this).append(`<img class="play_track_img2" src=${play_img}>`);

            }else{

            }}
        else{
            $(this).append(`<img class="play_track_img2" src=${play_img}>`);

        }});
    $(".buter_track2, .playlist_play").mouseleave(function () {
        if (play_song_real_life === this && Playing_song === true) {

        }else{
            $(this).empty();

        }
    });
});
var add_music_profile_user2 = document.querySelector('.fuck_button_add');
var music_but_menu_js = document.querySelectorAll('.music_but_menu');
$(document).on('click', '.music_but_menu', function () {
    for (var i=0; i < music_but_menu_js.length; i++){
        music_but_menu_js[i].style.color='#9A9A9A';
        music_but_menu_js[i].style.borderBottom = '1px solid #9A9A9A'
    }
//    console.log('12131')
    this.style.color='#E0DFDF';
    this.style.borderBottom = '1px solid #E0DFDF'
})

var add_music_profile_user = document.querySelectorAll('.fuck_button_add');
var delete_song_by_user = document.querySelectorAll('.delete_song_by_user')
$(document).on('click', '#add_music_user', function () {
    var vaal = add_music_profile_user[this.value-1];
    console.log(add_music_profile_user[this.value-1])
    ff = delete_song_by_user[this.value-1].style.display = 'inline';
    gg = vaal.style.display = 'none'
    console.log(add_music_profile_user2)
    $.ajax({
        url: "",
        data: {'this': this.value},
        success: function (response) {
                gg
                ff
            }})
})
$(document).on('click', '.delete_song_by_user', function () {
//    console.log(this.value)
    f = `#${this.value}`
//    console.log(this.name)

    $.ajax({
        url: `/profile/${this.name}/`,
        data: {'this': this.value},
        success: function (response) {
                $(f).remove()
            }})
})
function getCookie(name) {

    var matches = document.cookie.match(new RegExp(
      "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
    ))
    return matches ? decodeURIComponent(matches[1]) : undefined
}
var like_page_article_label = document.getElementById('like_page_article_label')
$(document).on('click', '.like_page_article', function () {
    f = this.name
//    console.log(this.value)
//    console.log(like_page_article_label.innerHTML)
    if (this.name === 'like'){
        $.ajax({
            url: `/magazine_page/${this.value}`,
            data: {'this': this.name, csrfmiddlewaretoken: getCookie('csrftoken')},
            type: 'post',
            success: function (response) {
                like_page_article_label.innerHTML = Number(like_page_article_label.innerHTML) + 1
                $('.like_page_article').attr('name', 'disslike')
                }})
    }else{
        $.ajax({
            url: `/magazine_page/${this.value}`,
            data: {'this': this.name, csrfmiddlewaretoken: getCookie('csrftoken')},
            type: 'post',
            success: function (response) {
                like_page_article_label.innerHTML = Number(like_page_article_label.innerHTML) - 1
                $('.like_page_article').attr('name', 'like')
        }})
    }
})
var subs = document.querySelector('.subs')
var un_subs = document.querySelector('.un_subs')
$(document).on('click', '#subs', function () {
    $.ajax({
            url: `/profile/${this.value}/`,
            data: {'this_sub': this.value, csrfmiddlewaretoken: getCookie('csrftoken')},
            type: 'post',
            success: function (response) {
                subs.style.display = 'none'
                un_subs.style.display = ''
        }})
})
