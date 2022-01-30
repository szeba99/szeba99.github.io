function delay(time) {
    return new Promise(resolve => setTimeout(resolve, time));
  }
  
function redirect_home()
{
    beepThree.play();
    document.body.style.animation = "opacity_down 1s";
    delay(999).then(function name(params)
    {
        
        window.location = "index.html";

    })
}

function change_content(id)
{
    document.getElementById("content_page").style.animation = "opacity_down 1s";
    beepTwo.play();
    delay(1000).then(function name(params)
    {
        document.getElementById("content_page").style.animation = "opacity_up 1s";
        if (id === "home")
        {
            document.getElementById("content_page").innerHTML = "asd";
        }
        else if (id === "about_me")
        {
            document.getElementById("content_page").innerHTML = "esd";
        }
        else
        {
            document.getElementById("content_page").innerHTML = "not found";
        }
    })
    
    
    
    

}