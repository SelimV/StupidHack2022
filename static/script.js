function eat() {
    console.log("Pressed eat")
    $.ajax({
        url: "/eat"
    })
    console.log("Ran ajax")
}