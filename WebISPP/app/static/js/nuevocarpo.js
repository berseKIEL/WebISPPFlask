// Boton para agregar CARPO
const mostrarPrompt = document.getElementById("nuevo");
// Para habilitar ivsibilidad
const nuevoCarpo = document.querySelector('.nuevocarpo')
// Id del Carga del Carpo y Hide
const cargacarpo = document.querySelector('#carga-carpo')
// Form del Carpo
const promptForm = document.querySelector(".form-carga-carpo");
// Cerrar
const cerrar = document.getElementById("close");

// IDs importantes
const orientaciones = document.querySelector('#orientaciones')
const planes = document.querySelector('#planes')

// Ids Input al sacar Hide
const carreraele = document.querySelector('#add_carrera')
const addplan = document.querySelector('#add_plan')
const addori = document.querySelector('#add_orientacion')

// Padres de los Hide
const carrerapadreele = carreraele.parentNode
const planpadreele = planes.parentNode
const oripadreele = orientaciones.parentNode



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
  nuevoCarpo.classList.toggle("hide");
};


cerrar.onclick = (e) => {
  nuevoCarpo.classList.add("hide");
  orientaciones.value = 'disable';
  orientaciones.style.color = "gray";
  planes.value = 'disable';
  planes.style.color = "gray";
  if (document.querySelector('.spanstyle')) {
    document.querySelector('.spanstyle').remove()
  }
  addori.value = '';
  addori.classList.add("hide");
  addplan.value = '';
  addplan.classList.add("hide");
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

    let optionPlan = planes.value;

    if (optionPlan=="other") {
      addplan.classList.toggle("hide")
    }
    else {
      addplan.classList.add("hide")
    }

  })

})


async function fetchOriPlan(url) {
  try {
    const response = await fetch(url);
    const oriplanes = await response.json();
    return oriplanes;
  }
  catch {
    console.error(error)
  }
}

async function renderOri(url) {
  const oriplanes = await fetchOriPlan(url)
  var max = oriplanes['Orientaciones'].length
  for (var i = 0; i < max; i++) {
    var opt = document.createElement('option')
    opt.value = oriplanes['Orientaciones'][i]['OrientacionID']
    opt.innerHTML = oriplanes['Orientaciones'][i]['OrientacionNombre']
    orientaciones.prepend(opt)
  }
}

async function renderPlan(url) {
  const oriplanes = await fetchOriPlan(url)
  var max = oriplanes['Planes'].length
  console.log(max)
  for (var i = 0; i < max; i++) {
    var opt = document.createElement('option')
    opt.value = oriplanes['Planes'][i]['PlanID']
    opt.innerHTML = "Plan "+oriplanes['Planes'][i]['PlanNombre']
    planes.prepend(opt)
  }
}