var navb = document.getElementById("navhead");
      var navm = document.getElementById("navmenu");
      window.onscroll = function(){
        if(window.pageYOffset >= navm.offsetTop){
            navb.classList.add("sticky");
        }
        else{
            navb.classList.remove("sticky");
        }
      }