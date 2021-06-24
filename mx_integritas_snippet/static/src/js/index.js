$(document).ready(function(){
    var id_carousel = $(".carousel-integritas-clientes").attr("id")
    $(".carousel-integritas-clientes").append(`
        <a href="#`+id_carousel+`" class="carousel-control-prev" data-slide="prev" role="button" aria-label="Anterior" title="Anterior">
            <span class="fa fa-chevron-circle-left fa-3x" style="color:rgba(64,126,201,.9);"></span>
            <span class="sr-only">Anterior</span>
        </a>
        <a href="#`+id_carousel+`" class="carousel-control-next" data-slide="next" role="button" aria-label="Siguiente" title="Siguiente">
            <span class="fa fa-chevron-circle-right fa-3x" style="color:rgba(64,126,201,.9);"></span>
            <span class="sr-only">Siguiente</span>
        </a>
    `)
})
