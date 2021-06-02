
$(window).scroll(function(p, a){
	var scrollLeft = $(window).scrollLeft();
  	var scrollTop = $(window).scrollTop();
  	if(scrollTop>=50){
  		$(".navbar-brand.logo span img").css("display","none");
  	}else{
  		$(".navbar-brand.logo span img").css("display","block");
  	}
});