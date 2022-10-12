const mostrarPrompt = document.getElementById("nuevo");
const promptBox = document.querySelector(".nuevamateria");
const promptForm = document.querySelector(".nuevaMateriaForm");
const close = document.getElementById("close");

mostrarPrompt.onclick = (e) => {
  promptBox.classList.toggle("hide");
};

promptForm.onsubmit = (e) => {
  promptBox.classList.add("hide");
};

close.onclick = (e) => {
    promptBox.classList.add("hide");
    document.getElementById('cod').value = '';
    document.getElementById('nom').value = '';
    document.getElementById('tipo').value = '';
};
