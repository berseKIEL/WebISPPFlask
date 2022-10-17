const mostrarPrompt = document.getElementById("nuevo");
const promptBox = document.querySelector(".nuevamateria");
const promptFormMateria = document.querySelector(".nuevaMateriaForm");
const cargamateria = document.querySelector("#carga-materia");
const close = document.getElementById("close");
const matnom = document.getElementById('materianombre');
const year = document.getElementById('materiaaño')
const tipo = document.getElementById('materiatipo')

if (year.value == "disable") {
  year.style.color = "gray";
}

year.addEventListener("change", function () {
  if (year.value != "disable") {
    year.style.color = "black";
  }
}
)


if (tipo.value == "disable") {
  tipo.style.color = "gray";
}

tipo.addEventListener("change", function () {
  if (tipo.value != "disable") {
    tipo.style.color = "black";
  }
}
)

mostrarPrompt.onclick = (e) => {
  promptBox.classList.toggle("hide");
};


close.onclick = (e) => {
    promptBox.classList.add("hide");
    matnom.value = ''
    year.value = 'disable';
    year.style.color = "gray";
    tipo.value = 'disable';
    tipo.style.color = "gray";
};

