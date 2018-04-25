function trunctuateList() {
    if($('.collection-item').length > 10) {
        for (var i = 9; i < $('.collection-item').length; i++) {
            $('.collection-item').eq(i).hide();
        }
        $('.show-more-btn').show();
    } else {
        $('.show-more-btn').hide();
    }
    
}

function showMore() {
    var startPoint = $('.collection-item:visible').length;
    for (var i = startPoint; i < startPoint+10; i++) {
        $('.collection-item').eq(i).show();
    }
    if ($('.collection-item:visible').length == $('.collection-item').length) {
        $('.show-more-btn').hide();
    } 
}

$(document).ready(function() {
    trunctuateList();
});