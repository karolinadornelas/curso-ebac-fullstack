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
    var passagemHTML = `
        <h2> WI.IO airlines</h2>
        <p>Passageiro:${data.name}</p>
        <p>Saídndo de:${data.aeroportoSaindo}</p>
        <p>Destino:${data.aeroportoDestino}</p>
        <p>Data:${data.date}</p>
        <p>Horário:${data.time}</p>

    `;
    var outraAba = window.open('', '_blank');
    outraAba.document.write(passagemHTML);
    outraAba.document.close();
}