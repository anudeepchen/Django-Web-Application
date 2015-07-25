/******************************
 * = Function to Check Mobile *
 ******************************/
var isMobile = false; //initiate as false
// device detection
if (/(android|bb\d+|meego).+mobile|avantgo|bada\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|ipad|iris|kindle|Android|Silk|lge |maemo|midp|mmp|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\.(browser|link)|vodafone|wap|windows (ce|phone)|xda|xiino/i.test(navigator.userAgent) || /1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\-)|ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|bw\-(n|u)|c55\/|capi|ccwa|cdm\-|cell|chtm|cldc|cmd\-|co(mp|nd)|craw|da(it|ll|ng)|dbte|dc\-s|devi|dica|dmob|do(c|p)o|ds(12|\-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(\-|_)|g1 u|g560|gene|gf\-5|g\-mo|go(\.w|od)|gr(ad|un)|haie|hcit|hd\-(m|p|t)|hei\-|hi(pt|ta)|hp( i|ip)|hs\-c|ht(c(\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i\-(20|go|ma)|i230|iac( |\-|\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\/)|klon|kpt |kwc\-|kyo(c|k)|le(no|xi)|lg( g|\/(k|l|u)|50|54|\-[a-w])|libw|lynx|m1\-w|m3ga|m50\/|ma(te|ui|xo)|mc(01|21|ca)|m\-cr|me(rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi|de|do|t(\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)\-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\-2|po(ck|rt|se)|prox|psio|pt\-g|qa\-a|qc(07|12|21|32|60|\-[2-7]|i\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\-|oo|p\-)|sdk\/|se(c(\-|0|1)|47|mc|nd|ri)|sgh\-|shar|sie(\-|m)|sk\-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|sp(01|h\-|v\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\-|tdg\-|tel(i|m)|tim\-|t\-mo|to(pl|sh)|ts(70|m\-|m3|m5)|tx\-9|up(\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)|vk(40|5[0-3]|\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(\-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|yas\-|your|zeto|zte\-/i.test(navigator.userAgent.substr(0,4))) isMobile = true;

/******************************
 * = Intialize Loading Screen *
 ******************************/
var loading_screen = pleaseWait({
    logo: "/static/images/logo/skycision-logo.png",
    backgroundColor: "#097054",
    loadingHtml: "<p class='loading-message'>Welcome to Skycision!</p><div class='sk-spinner sk-spinner-chasing-dots'><div class='sk-dot1'></div><div class='sk-dot2'></div></div>"
});

$(window).load(function() {
    loading_screen.finish();
    $("#fullpage").removeClass("hidden");
    $("#bt-menu").removeClass("hidden");
}) 

/************************
 * = Intialize FullPage *
 ************************/
$(document).ready(function () {
    $("#fullpage").fullpage({
        scrollOverflow: true,
        
        afterRender: function() {
          // Start slide show going right
          slideTimeout = setInterval(function () {
              $.fn.fullpage.moveSlideRight();
          }, 5000);  
        },
        
        afterLoad: function(anchorLink, index) {
            if (index == 1) {
                // Delay to wait for loading screen to fade out
                setTimeout(function () {
                    // Start animate Section 1, slide 1
                    $("#section1").find("#slide1 .title-row div").removeClass("hidden").addClass("animated fadeInLeft");
                    $("#section1").find("#slide1 .subtitle-row div").removeClass("hidden").addClass("animated fadeInLeft");
                }, 1700);
            }
            
            if (index == 2) {
                // Start animate Section 2, slide 1
                $("#section2").find(".hovicon").removeClass("hidden").addClass("animated fadeInUp");
                $("#section2").find(".img-subtitle").removeClass("hidden").addClass("animated fadeInLeft");
            }
        },
        
        afterSlideLoad: function(anchorLink, index, slideAnchor, slideIndex) {
            if ((index == 1) && (slideIndex == 1)){
                // Start animate Section 1, slide 2
                $("#section1").find("#slide2 .title-row div").removeClass("hidden").addClass("animated fadeInLeft");
                $("#section1").find("#slide2 .subtitle-row div").removeClass("hidden").addClass("animated fadeInLeft");
            }
          
            if ((index == 1) && (slideIndex == 2)){
                // Start animate Section 1, slide 3
                $("#section1").find("#slide3 .title-row div").removeClass("hidden").addClass("animated fadeInLeft");                
                $("#section1").find("#slide3 .subtitle-row div").removeClass("hidden").addClass("animated fadeInLeft");
            }
            
            if ((index == 2) && (slideIndex != 0)) {
                // Start animate in Section 2, slide 2-4
                $("#section2").find(".title-row div").removeClass("hidden").addClass("animated fadeInUp");
                $("#section2").find(".go-back").removeClass("hidden").addClass("animated fadeInRight");
            }
        },
        
        onLeave: function (index, direction) {
            if (index == 1) {
                // Remove slide show animation 
                clearInterval(slideTimeout);
            }
        },
    });
    $.fn.fullpage.setKeyboardScrolling(false, "left, right");
});

/*****************************
 * = Innitialize Tooltipster *
 *****************************/
$(document).ready(function() {
    $("nav").find(".bt-icon").tooltipster({
        theme: "tooltipster-light",
        animation : "grow",
        trigger: "click",
    });
    if (!isMobile) {
        $("#section2").find("#slide1").find(".hovicon").tooltipster({
            theme: "tooltipster-light",
            animation : "grow",
            trigger: "hover",
            content: "Click for more!",
        });
        $(".go-back").tooltipster({
            theme: "tooltipster-light",
            animation : "grow",
            trigger: "hover",
            content: "Go back",
        });
    }
});

/*********************************
 * = Handle Section 2 Icon Click *
 *********************************/
$("#section2").find(".hovicon").on("click", function() {
    // Get the desire slide
    var slide = $(this).attr("slide-target");
    // Start anime out Section 2, slide 1
    $("#section2").find(".hovicon").removeClass("animated fadeInUp").addClass("animated fadeOutDown");
    $("#section2").find(".img-subtitle").removeClass("animated fadeInUp").addClass("animated fadeOutRight");
    setTimeout(function () {
        $.fn.fullpage.silentMoveTo(2, slide);
    }, 1000);
});

/*******************************
 * = Handle Next Section Click *
 *******************************/
$(".next-section").find(".fa-angle-down").on("click", function() {
    // Get the desire section
    var section = $(this).attr("section-target");
    $.fn.fullpage.moveTo(section);
});

/***************************
 * = Initialize Animsition *
 ***************************/
$(document).ready(function () {
    $(".animsition").animsition({
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

/*******************************
 * = Handle Close Button Click *
 *******************************/
$(".go-back").on("click", function () {
    // Start animate out Section 2, slide 2-4
    $("#section2").find(".title-row div").removeClass("animated fadeInUp").addClass("animated fadeOutDown");
    $("#section2").find(".go-back").removeClass("anmiated fadeInRight").addClass("animated fadeOutLeft");
    setTimeout(function () {
        // Hide the close button
        $("#section2").find(".go-back").addClass("hidden").removeClass("animated fadeOutLeft");
        $("#section2").find(".title-row div").addClass("hidden").removeClass("animated fadeOutDown");
        $.fn.fullpage.silentMoveTo(2, 0);
        // Start animate in Section 1, slide 1
        $("#section2").find(".hovicon").removeClass("animated fadeOutDown").addClass("animated fadeInUp");
        $("#section2").find(".img-subtitle").removeClass("animated fadeOutRight").addClass("animated fadeInLeft");
    }, 1500);
});