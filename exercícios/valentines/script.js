const modal = document.querySelector('.modal-container')
const tbody = document.querySelector('tbody')
const sPet = document.querySelector('#m-pet')
const sNome = document.querySelector('#m-nome')
const sRaca = document.querySelector('#m-breed')
const sTutor = document.querySelector('#m-tutor')
const sRegistro = document.querySelector('#m-registro')
const sContato = document.querySelector('#m-contato')
const sEntrada = document.querySelector('#m-entrada')
const sObservacao = document.querySelector('#m-obs')
const sPagamento = document.querySelector('#m-pagamento')
const btnSalvar = document.querySelector('#btnSalvar')


let itens
let id

function openModal(edit = false, index = 0) {
    modal.classList.add('active')
    modal.onclick = e => {
        if (e.target.className.indexOf('modal-container') !== -1){
            modal.classList.remove('active')
        }
    }
    
    if(edit){
        sPet.value = itens[index].pet
        sNome.value = itens[index].nome
        sRaca.value = itens[index].breed
        sTutor.value = itens[index].tutor
        sRegistro.value = itens[index].registro
        sContato.value = itens[index].contato
        sEntrada.value = itens[index].entrada
        sObservacao.value = itens[index].obs
        sPagamento.value = itens[index].pagamento
        
        id = index
    }else{
        sPet.value = '';
        sNome.value = '';
        sRaca.value = '';
        sTutor.value = '';
        sRegistro.value = '';
        sContato.value = '';
        sEntrada.value = '';
        sObservacao.value = '';
        sPagamento.value = '';
    }

}

function editItem(index){
    openModal(true, index)
}

function deleteItem(index){
    itens.splice(index, 1)
    setItensBD()
    loadItens()
}

function insertItem(item, index){
    let tr = document.createElement('tr')

    tr.innerHTML = `
    <td>${item.pet}</td>
    <td>${item.nome}</td>
    <td>${item.breed}</td>
    <td>${item.tutor}</td>
    <td>${item.registro}</td>
    <td>${item.contato}</td>
    <td>${item.entrada}</td>
    <td>${item.obs}</td>
    <td>${item.pagamento}</td>
    <td class = "acao"><button onclick="editItem(${index})"><i class='bx bx-edit'></i></button></td>
    <td class = "acao"><button onclick="deleteItem(${index})"><i class='bx bx-trash'></i></button></td>
    `
    tbody.appendChild(tr)

}

btnSalvar.onclick = e =>{
    if (sPet.value == '' || sNome.value == '' || sRaca.value == '' || sTutor.value == '' || sRegistro.value == '' || sContato.value == '' || sEntrada.value == '' || sObservacao.value == '' || sPagamento.value == ''){
        return
    }

    e.preventDefault();
    if (id !== undefined){
        itens[id].pet = sPet.value
        itens[id].nome = sNome.value
        itens[id].breed = sRaca.value
        itens[id].tutor =sTutor.value
        itens[id].registro =sRegistro.value
        itens[id].contato=sContato.value
        itens[id].entrada =sEntrada.value
        itens[id].obs = sObservacao.value
        itens[id].pagamento = sPagamento.value
    }   else{
        itens.push({
        'pet': sPet.value, 
        'nome': sNome.value, 
        'breed': sRaca.value,
        'registro': sRegistro.value,
        'contato': sContato.value,
        'tutor':sTutor.value, 
        'entrada':sEntrada.value, 
        'obs':sObservacao.value, 
        'pagamento':sPagamento.value
        })
    }
    
  setItensBD()

  modal.classList.remove('active')
  loadItens()
  id = undefined
}

function loadItens() {
  itens = getItensBD()
  tbody.innerHTML = ''
  itens.forEach((item, index) => {
    insertItem(item, index)
  })

}

const getItensBD = () => JSON.parse(localStorage.getItem('dbfunc'))
const setItensBD = () => localStorage.setItem('dbfunc', JSON.stringify(itens))

loadItens()