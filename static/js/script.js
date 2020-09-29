$(function(){
    $(window).load(function() {
        // get document & footer height
        var body_height =  $("body").height();
        var $footer = $('.footer');
        var footer_height = $footer.outerHeight();
        var footer_top_pos = $footer.position().top;
        // check footer position
        if (footer_top_pos < body_height - footer_height) {
            $footer.css({"position": "absolute", "bottom": "0"});
        }
    });
    // datepicker
    $(".datepicker").datepicker({
        dayNamesShort: ["日", "月", "火", "水", "木", "金", "土"],
        dateFormat: "mm.dd(D)",
    });
    // accordion
    $(".accordion").accordion({
        active: false,
        collapsible: true,
        icons: false
    });
    // mobile menu behaviour
    $(".navbar-toggler").click(function() {
        $(".navbar-collapse").addClass("show");
    });
    $(".close").click(function() {
        $(".navbar-collapse").removeClass("show");
    });
});
