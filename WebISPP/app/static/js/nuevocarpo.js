const mostrarPrompt = document.getElementById("nuevo");
const promptBox = document.querySelector(".nuevocarpo");
const promptForm = document.querySelector(".form-carga-carpo");
const close = document.getElementById("close");

const orientaciones = document.getElementById('orientaciones')
const planes = document.getElementById('planes')



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

promptForm.onsubmit = (e) => {
  promptBox.classList.add("hide");
};

close.onclick = (e) => {
  promptBox.classList.add("hide");
  orientaciones.value = 'disable';
  orientaciones.style.color = "gray";
  planes.value = 'disable';
  planes.style.color = "gray";
};

const cargacarpo = document.querySelector('#carga-carpo')
const oriID = document.querySelector('#orientaciones')
const planID = document.querySelector('#planes')
