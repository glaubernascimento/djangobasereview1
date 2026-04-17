// cadastro/static/cadastro/js/adicionar.js

const addBtn = document.getElementById('add-telefone');
const totalForms = document.getElementById('id_telefones-TOTAL_FORMS');

addBtn.addEventListener('click', () => {
    const count = parseInt(totalForms.value);

    const newDiv = document.createElement('div');
    newDiv.className = 'd-flex align-items-center gap-2 mb-3';
    newDiv.innerHTML = `
        <label for="id_telefones-${count}-numero">Número:</label>
        <input type="text" 
               name="telefones-${count}-numero" 
               id="id_telefones-${count}-numero" 
               class="form-control" 
               style="width: auto;">
    `;

    addBtn.before(newDiv);
    totalForms.value = count + 1;
});