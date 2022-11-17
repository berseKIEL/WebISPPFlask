let previousFila;

$(document).ready(function(){

    $('.fila').click(function(){
        var idtr = $(this).attr('id');
        $(previousFila).css('background-color', '');
        $(previousFila).css('color', 'black');
        $(previousFila).find('.a-icon').css('filter', '');
        $(previousFila).find('.a-icon').addClass('hide')
        $(this).css('background-color', 'rgb(193, 207, 227)');
        $(this).find('.a-icon').css('filter', 'invert(27%) sepia(69%) saturate(753%) hue-rotate(174deg) brightness(90%) contrast(99%)');
        $(this).find('.a-icon').removeClass('hide')
        previousFila = this;
        $(this).find('#remover').hover(function(){
            $(this).css('filter', 'invert(8%) sepia(95%) saturate(5598%) hue-rotate(16deg) brightness(95%) contrast(118%)');
        },function() {
            $(this).css('filter', 'invert(27%) sepia(69%) saturate(753%) hue-rotate(174deg) brightness(90%) contrast(99%)');
        })
    })

    $('.fila').dblclick(function() {
        var idtr = $(this).attr('id');

        var input=document.createElement("input");

        var val = this.value;

        input.classList.add('inputCarrera');

        input.value = idtr;

        input.onsubmit=function() {
            val = this.value;
            this.parentNode.id = val;
        }

        $(this).find('.titulo').html("");
        $(this).find('.titulo').append(input);

        input.focus();
    })
})