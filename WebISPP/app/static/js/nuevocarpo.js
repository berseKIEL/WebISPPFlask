const mostrarPrompt = document.getElementById("nuevo");
const promptBox = document.querySelector(".nuevocarpo");
const promptForm = document.querySelector(".form-carga-carpo");
const close = document.getElementById("close");

const orientaciones = document.getElementById('orientaciones')
const planes = document.getElementById('planes')

const addori = document.querySelector('#add_orientacion')
const addplan = document.querySelector('#add_plan')


const carreraele = document.querySelector('#add_carrera')
const carrerapadreele = carreraele.parentNode

const planpadreele = planes.parentNode

const oripadreele = orientaciones.parentNode


const cargacarpo = document.querySelector('#carga-carpo')
const oriID = document.querySelector('#orientaciones')
const planID = document.querySelector('#planes')


if (orientaciones.value == "disable") {
  orientaciones.style.color = "gray";
}

orientaciones.addEventListener("change", function () {
  if (orientaciones.value != "disable") {
    orientaciones.style.color = "black";
  }
}
)

if (planes.value == "disable") {
  planes.style.color = "gray";
}

planes.addEventListener("change", function () {
  if (planes.value != "disable") {
    planes.style.color = "black";
  }
}
)

mostrarPrompt.onclick = (e) => {
  promptBox.classList.toggle("hide");
};


close.onclick = (e) => {
  promptBox.classList.add("hide");
  orientaciones.value = 'disable';
  orientaciones.style.color = "gray";
  planes.value = 'disable';
  planes.style.color = "gray";
  if (document.querySelector('.spanstyle')) {
    document.querySelector('.spanstyle').remove()
  }  
};

// Select "Otro"

$(document).ready(function() {
  $('#orientaciones').change(function(){

    let optionOri = orientaciones.value;

    if (optionOri=="other") {
      addori.classList.toggle("hide")
    }
    else {
      addori.classList.add("hide")
    }

  })

  $('#planes').change(function(){

    let optionPlan = orientaciones.value;

    if (optionPlan=="other") {
      addplan.classList.toggle("hide")
    }
    else {
      addplan.classList.add("hide")
    }

  })

})