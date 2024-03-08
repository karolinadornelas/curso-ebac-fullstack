document.getElementById("passagem").addEventListener("submit", function(event){
    event.preventDefault();

    var name = document.getElementById("name").value;
    var aeroportoSaindo = document.querySelector('select[name="aeroportoSaindo"]').value;
    var aeroportoDestino = document.querySelector('select[name="aeroportoDestino"]').value;
    var date = document.getElementById("date").value;
    var time = document.getElementById("time").value;

    var dadosPassagem = {
        name: name,
        aeroportoSaindo: aeroportoSaindo,
        aeroportoDestino: aeroportoDestino,
        date: date,
        time: time
    };

    gerarPassagem(dadosPassagem);

});

function gerarPassagem(data){
    var estiloPassagem = `
        .passageiro {
            font-weight: bold;
            color: #041053;
        }
        
        .aeroportoSaindo {
            font-style: italic;
        }
        
        .aeroportoDestino {
            text-decoration: underline;
        }
        
        .data {
            font-size: 14px;
        }
        
        .horario {
            font-size: 14px;
            color: green;
        }
        
        .passagem-container {
            display: flex;
            padding: 20px;
            border: 2px solid #333;
            border-radius: 10px;
            background-color: #f0f0f0;
            font-family: Arial, sans-serif;
        }
        
        .icone{
            width: 100px;
            height: 100px;
            border-radius: 50%; 
            background-color: transparent; 
            position: absolute;
            border: 1px solid #041053;
        }
    `;

    var passagemHTML = `
    <div class="passagem-container">
    <div class="icone"></div>
    <img src="./assets/flying.png" alt="icone avião de frente" width="70" height="70">
    <h2>WI.IO airlines</h2>
    <p class= "passageiro">Passageiro:${data.name}</p>
    <p class= "aeroportoSaindo">Saindo de:${data.aeroportoSaindo}</p>
    <p class= "aeroportoDestino">Destino:${data.aeroportoDestino}</p>
    <p class= "date">data:${data.date}</p>
    <p class= "horario">Horario:${data.horario}</p>`
    var outraAba = window.open('', '_blank');
    outraAba.document.write(`<style>"${estiloPassagem}"</style>${passagemHTML}</div>`);
    outraAba.document.close();
}
