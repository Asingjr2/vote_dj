$(document).ready(function(){

    var startCharsCount = 250;
    var currentCharCount = 0;

    var form = $("#recommendation-form").val()

    $("#recommendation-form").append("<span id='chars_count'>CHARACTERS LEFT = " +  startCharsCount + " </span>")

    $("#recommendation-form textarea").keyup(function(e){
        var messageValue = $(this).val()
        currentCharCount = startCharsCount - messageValue.length
        var spanCharsCount = $("#chars_count")
        spanCharsCount.text("CHARACTERS LEFT = " + currentCharCount)
        console.log(messageValue)

    })

})
