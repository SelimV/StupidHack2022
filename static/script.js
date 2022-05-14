function eat() {
    console.log("Pressed eat")
    $.ajax({
        url: "/eat"
    })
    console.log("Ran ajax")
}


var ctx = document.getElementById('cat').getContext('2d');
// load image
var image = new Image();
image.onload = function () {
    // draw the image into the canvas
    ctx.drawImage(image, 0, 0);
}
image.src = '/cats/furycat.jpg';