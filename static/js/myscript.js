window.onscroll = function () { scrollFunction() };

function scrollFunction() {
  if (document.body.scrollTop > 160 || document.documentElement.scrollTop > 160) {
    // Navbar wrapper
    document.getElementsByClassName("navbar")[0].classList.add("navbar-event");



    var nav_text = document.getElementsByClassName("navbar-text-font");
    for (var i = 0; i < nav_text.length; i++) {
      nav_text[i].classList.add("navbar-text-color-black");
    }
    // Navbar font
    document.getElementsByClassName("navbar-brand")[0].classList.add("navbar-text-color-black");
    // Navbar toggler color changer
    // document.getElementsByClassName("navbar-toggler-main-icon")[0].classList.add("navbar-toggler-color-black");
    // Button scroller
    document.getElementsByClassName("scroll-up-wrapper")[0].style.visibility = "visible"

  } else {
    
    // Button scroller
    document.getElementsByClassName("scroll-up-wrapper")[0].style.visibility = "hidden"

    function myFunction(x) {
      if (x.matches) { // If media query matches
        // Navbar wrapper
        document.getElementsByClassName("navbar")[0].classList.remove("navbar-event");
        var nav_text = document.getElementsByClassName("navbar-text-font");
        for (var i = 0; i < nav_text.length; i++) {
          nav_text[i].classList.remove("navbar-text-color-black");
        }
        // Navbar font
        document.getElementsByClassName("navbar-brand")[0].classList.remove("navbar-text-color-black");

        // Navbar toggler color changer
        // document.getElementsByClassName("navbar-toggler-main-icon")[0].classList.remove("navbar-toggler-color-black");
     
      } 
    }
    var x = window.matchMedia("(min-width: 992px)")
    myFunction(x) // Call listener function at run time
    

  }
}

function toggleFunction(x) {
  x.classList.toggle("change");
}


