let previousFila;


$(document).ready(function(){
    let Orientacion = document.getElementById('idorientacion').value;

    $('.fila').click(function(){
        var idtr = $(this).attr('id');
        $(previousFila).css('background-color', '');
        $(previousFila).css('color', 'black');
        $(previousFila).find('.a-icon').css('filter', '');
        $(this).css('background-color', 'rgb(193, 207, 227)');
        $(this).find('.a-icon').css('filter', 'invert(27%) sepia(69%) saturate(753%) hue-rotate(174deg) brightness(90%) contrast(99%');

        previousFila = this
    })
    $('.fila').dblclick(function(){
        var idtr = $(this).attr('id');
        document.getElementById('idcarrera').value = idtr;
        document.getElementById('idorientacion').value = Orientacion;
        document.getElementById("form-dbclick").submit();
    })
})

