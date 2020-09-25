$(function(){
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
});
