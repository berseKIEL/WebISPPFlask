let previousFila;

$(document).ready(function(){
    let orientacionid = document.getElementById('orientacionid').value;
    let carreraid = document.getElementById('carreraid').value;
    let planid = document.getElementById('planid').value;

    $('.fila').click(function(){
        var idtr = $(this).attr('id');
        $(previousFila).css('background-color', '');
        $(previousFila).css('color', 'black');
        $(previousFila).find('.a-icon').css('filter', '');
        $(this).css('background-color', 'rgb(193, 207, 227)');
        $(this).find('.a-icon').css('filter', 'invert(27%) sepia(69%) saturate(753%) hue-rotate(174deg) brightness(90%) contrast(99%)');
        previousFila = this
    })
    
    $('.fila').dblclick(function(){
        var idtr = $(this).attr('id');
        if(carreraid == -1){
            document.getElementById('carreraid').value = idtr;
            document.getElementById('orientacionid').value = orientacionid;
            document.getElementById('planid').value = planid;
        }
        else{
            if(orientacionid == -1){
                document.getElementById('orientacionid').value = idtr;
                document.getElementById('carreraid').value = carreraid;
                document.getElementById('planid').value = planid;
            }
            if(orientacionid > -1){
                document.getElementById('orientacionid').value = orientacionid;
                document.getElementById('carreraid').value = carreraid;
                document.getElementById('planid').value = idtr;
            }
        }
        document.getElementById("form-dbclick").submit();
    })
})

