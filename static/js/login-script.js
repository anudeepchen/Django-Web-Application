/********************
 * = Intialize Page *
 ********************/
$(window).load(function() {
    $("#fullpage").removeClass("hidden");
    $("#bt-menu").removeClass("hidden");
});

/************************
 * = Intialize FullPage *
 ************************/

$(document).ready(function () {
    $("#fullpage").fullpage({
        scrollOverflow: true,
    });
});

/***************************
 * = Initialize Animsition *
 ***************************/
$(document).ready(function () {
    $(".animsition").animsition({
        inClass: "fade-in-left",
        outClass: "fade-out-left",
        linkElement: ".animsition-link",
        loading: false,
    });
});

/**************************
 * = Handle Nav Bar Click *
 **************************/
$(".bt-menu-trigger").on("click", function () {
    if ($(".bt-menu").hasClass("bt-menu-close")) {
        $(".wrapper").fadeTo(150, 1);
    }
    else {
        $(".wrapper").fadeTo(150, 0);
    }
});

$(".bt-overlay").on("click", function () {
    $(".wrapper").fadeTo(150, 1);
});

/********************************
 * = Handle Message from Server *
 ********************************/

if ($(".message").text() != "") {
    // Show the message when animation ends
    $(".animsition").one("animsition.end", function() {
        swal({
            title: "Error!",
            text: $(".message").text(),
            type: "error",
        })
    });
}

/*********************
 * = Initialize Wave *
 *********************/
Waves.attach("button", []);
Waves.init();