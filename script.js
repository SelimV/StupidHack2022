function eat() {
    console.log("Pressed eat")
    $.ajax({
        url: "hello.py"
    })
    console.log("Ran ajax")
}