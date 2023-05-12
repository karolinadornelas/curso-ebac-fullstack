let valor1 = document.getElementById('numero1');
let valor2 = document.getElementById('numero2');
let form = document.getElementById('formulario');

form.addEventListener('submit', function (e){
    e.preventDefault();

    if(valor1.value > valor2.value){
        alert('O valor A é maior, tente outra vez.')
    } else{
        alert('O valor B é maior, continue assim!')
    }
})
