function eat() {
    console.log("Pressed eat")
    $.ajax({
        url: "/eat"
    })
    console.log("Ran ajax")
}

var happiness=100;
var ateRecently=false;

setInterval(
    function(){
        happiness-=10;
        if(happiness<=0){
            document.getElementById('furycat').style.display='inline';
            document.getElementById('sadcat').style.display='none';
            document.getElementById('happycat').style.display='none';
            document.getElementById('happiestcat').style.display='none';

            document.getElementById('ripped').style.display='inline';
            document.getElementById('folder').style.display='none';
            if(!ateRecently){
                eat();
                ateRecently=true;
            }
            happiness=0
        }else if(happiness<=40){
            document.getElementById('furycat').style.display='none';
            document.getElementById('sadcat').style.display='inline';
            document.getElementById('happycat').style.display='none';
            document.getElementById('happiestcat').style.display='none';
        }else if(happiness<=80){
            document.getElementById('furycat').style.display='none';
            document.getElementById('sadcat').style.display='none';
            document.getElementById('happycat').style.display='inline';
            document.getElementById('happiestcat').style.display='none';
        }else {
            document.getElementById('furycat').style.display='none';
            document.getElementById('sadcat').style.display='none';
            document.getElementById('happycat').style.display='none';
            document.getElementById('happiestcat').style.display='inline';
        }
        console.log(happiness);
    },
    1000
);

