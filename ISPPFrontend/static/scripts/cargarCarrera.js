const inputOrientacion=document.querySelector('.inputOrientacion');
const inputPlan=document.querySelector('.inputPlan');
$(document).ready(function(){
    
    $('.id_orientacion').change(function(){

        let opcionO=document.querySelector('.id_orientacion').value;

        if (opcionO=="otra")
            inputOrientacion.classList.toggle("hide");
        else
            inputOrientacion.classList.add("hide");

    })

    $('.id_plan').change(function(){

        let opcionP=document.querySelector('.id_plan').value;

        if (opcionP =="otro")
            inputPlan.classList.toggle("hide");
        else
            inputPlan.classList.add("hide");

    })

})