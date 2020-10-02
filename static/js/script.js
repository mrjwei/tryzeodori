$(function(){
    $(window).load(function() {
        // get document & footer height
        var body_height =  $("body").height();
        var win_height = $(window).height();
        var $footer = $(".footer");
        // check footer position
        if (body_height < win_height) {
            $footer.css({"position": "absolute", "bottom": "0", "width": "100%"});
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
    // $(".close").click(function() {
    //     $(".navbar-collapse").toggleClass("show");
    // });
    $(".navbar-toggler").click(function(e) {
        e.stopPropagation();
        $(".navbar-collapse").addClass("show");
    });
    $(".close").click(function(e) {
        e.stopPropagation();
        $(".navbar-collapse").removeClass("show");
    });
    // fix textarea cannot break line problem
    $("textarea").html("<pre></pre>");
});
