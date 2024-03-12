var receitao= document.getElementById("receitarium");
var btn = document.getElementById("receitas");
var span = document.getElementsByClassName("close")[0];

btn.onclick = function(){
    receitao.style.display = "block";
}

span.onclick = function(){
    receitao.style.display = 'none';
}

window.onclick = function(event) {
    if (event.target == receitao) {
      receitao.style.display = "none";
    }
}
