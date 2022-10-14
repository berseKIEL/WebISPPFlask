const mostrarPrompt = document.getElementById("nuevo");
const promptBox = document.querySelector(".nuevamateria");
const promptForm = document.querySelector(".nuevaMateriaForm");
const close = document.getElementById("close");
const year = document.getElementById('year')
const tipo = document.getElementById('tipo')


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

promptForm.onsubmit = (e) => {
  promptBox.classList.add("hide");
};

close.onclick = (e) => {
    promptBox.classList.add("hide");
    document.getElementById('cod').value = '';
    year.value = 'disable';
    year.style.color = "gray";
    tipo.value = 'disable';
    tipo.style.color = "gray";
};

