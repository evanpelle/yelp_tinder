currIndex = 0


$(document).ready(function() { 
    setValues(rest_data[currIndex])
    $('#left-btn').click(leftSwipe)
    $('#right-btn').click(rightSwipe)
});


function setValues(rest) {
    $('#rest-name').text(rest['name'])
    $('#rest-img').attr('src', rest['image'])
    $('#rest-rating').text("Rating " + rest['rating'])

    $(document).one('keyup', function(e) {
    switch(e.which) {
        case 37: // left
        leftSwipe()
        break;

        case 39: // right
        rightSwipe()
        break;

        default: return; // exit this handler for other keys
    }
    e.preventDefault(); // prevent the default action (scroll / move caret)
});
}

function leftSwipe() {
    currIndex++
    setValues(rest_data[currIndex])
}

function rightSwipe() {
    url = rest_data[currIndex]['url']
    win = window.open(url, '_blank');
    window.focus()
    currIndex++
    setValues(rest_data[currIndex])
}

function openInNewTab(url) {
  var win = window.open(url, '_blank');
  win.focus();
}