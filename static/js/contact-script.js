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

/*****************************
 * = Innitialize Tooltipster *
 *****************************/
$(document).ready(function () {
    $("#id_email").tooltipster({
        theme: "tooltipster-light",
        animation : "grow",
        trigger: "click",
        content: "E.g. john@gmail.com",
    });
    
    $("#id_phone").tooltipster({
        theme: "tooltipster-light",
        animation : "grow",
        trigger: "click",
        content: "E.g. 4121234567. Up to 15 digits allowed.",
    });
    $("#id_interest").tooltipster({
        theme: "tooltipster-light",
        animation : "grow",
        trigger: "click",
        content: "What is your area of interest?",
    });
    $("nav").find(".bt-icon").tooltipster({
        theme: "tooltipster-light",
        animation : "grow",
        trigger: "click",
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
if ($(".message").text() == "Accepted") {
    // Show the message when animation ends
    $(".animsition").one("animsition.end", function() {
        swal({
            title: "Thank you!",
            text: "We will get in touch with you soon!",
            type: "success",
        },
        function () {
            $(".notifications").notify({
                message: { text: "You have succesfully send us a message!"},
                type: "success",
                closable: false,
            }).show()
        });
    });
};

if ($(".message").text() == "Rejected") {
    // Show the message when animation ends
    $(".animsition").one("animsition.end", function() {
        swal({
            title: "Oops!",
            text: "There is error in your form!",
            type: "error",
        },
        function () {
            $(".notifications").notify({
                message: { text: "Please fix your form! "},
                type: "danger",
                closable: false,
            }).show()
        });
    });
};

/***********************************
 * = Show Max Length for Text Area *
 ***********************************/
$("#id_message").maxlength({
    alwaysShow: true,
    threshold: 250,
});

/*********************
 * = Initialize Wave *
 *********************/
Waves.attach("button", []);
Waves.init();