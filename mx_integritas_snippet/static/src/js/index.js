/*$('#recipeCarousel').carousel({
  interval: 10000
})

$('.carousel .carousel-item').each(function(){
    var minPerSlide = 3;
    var next = $(this).next();
    if (!next.length) {
    next = $(this).siblings(':first');
    }
    next.children(':first-child').clone().appendTo($(this));
    
    for (var i=0;i<minPerSlide;i++) {
        next=next.next();
        if (!next.length) {
            next = $(this).siblings(':first');
        }
        
        next.children(':first-child').clone().appendTo($(this));
      }
});*/

/*$(document).ready(function(){
    var id_carousel = $(".carousel-integritas-clientes").attr("id")
    alert(id_carousel)
    $(".container-principal-carousel").append(`

        <a href="`+id+`" class="carousel-control-prev" data-slide="prev" role="button" aria-label="Anterior" title="Anterior">
            <span class="fa fa-chevron-circle-left fa-2x" style="color:rgba(64,126,201,.75);"></span>
            <span class="sr-only">Anterior</span>
        </a>
        <a href="`+id+`" class="carousel-control-next" data-slide="next" role="button" aria-label="Siguiente" title="Siguiente">
            <span class="fa fa-chevron-circle-right fa-2x" style="color:rgba(64,126,201,.75);"></span>
            <span class="sr-only">Siguiente</span>
        </a>
    `)
})*/
