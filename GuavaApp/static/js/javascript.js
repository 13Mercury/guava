/*$('#popover').popover({
    html : true,

    content: function() {
      return $("#popover-content").html();
    }
});

$('.carousel').carousel()
*/
(function($) {
    "use strict"; // Start of use strict

    // Smooth scrolling using jQuery easing
    $('a.js-scroll-trigger[href*="#"]:not([href="#"])').click(function() {
        if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
            var target = $(this.hash);
            target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
            if (target.length) {
                $('html, body').animate({
                    scrollTop: (target.offset().top - 48)
                }, 1000, "easeInOutExpo");
                return false;
            }
        }
    });

    // Closes responsive menu when a scroll trigger link is clicked
    $('.js-scroll-trigger').click(function() {
        $('.navbar-collapse').collapse('hide');
    });

    // Activate scrollspy to add active class to navbar items on scroll
    $('body').scrollspy({
        target: '#mainNav',
        offset: 54
    });

    // Collapse Navbar
    var navbarCollapse = function() {
        var element = document.getElementById('hh');
        if (typeof(element) != 'undefined' && element != null) {
            if ($("#mainNav").offset().top > 100) {
                $("#mainNav").addClass("navbar-shrink");
                $("#color").attr("src", "/static/img/sproutColor.png");
            } else {
                $("#mainNav").removeClass("navbar-shrink");
                $("#color").attr("src", "/static/img/sprout.png");
            }
        } else {
            $("#mainNav").addClass("navbar-shrink");
            $("#color").attr("src", "/static/img/sproutColor.png");
        }

    };
    // Collapse now if page is not at top
    navbarCollapse();
    // Collapse the navbar when page is scrolled
    $(window).scroll(navbarCollapse);

    // Collapse Navbar
    var clean = true;
    var mapScroll = function() {
        if (clean) {
            if ($("#mainNav").offset().top > 1400) {
                mapReload();
                clean = false;
            }
        } else {
            if ($("#mainNav").offset().top < 1300) {
                deleteMarkers();
                clean = true;
            }
        }
    };
    // Collapse the navbar when page is scrolled
    $(window).scroll(mapScroll);

})(jQuery); // End of use strict

$('body').on('click', '[data-toggle="modal"]', function() {
    $($(this).data("target") + ' .modal-content').load($(this).attr('href'));
});

$(document).ready(function() {
    var element = document.getElementById('messa');
    if (typeof(element) != 'undefined' && element != null) {
        if (element.children[0].textContent == "Usuario y/o contraseña incorrecto")
            $('#log').click();
        else if (element.children[0].textContent == "Nombre del area debe contener solo letras")
                $('#newArea').click();
        else
            $('#regis').click();  $('#newInfo').click();
    }

});
