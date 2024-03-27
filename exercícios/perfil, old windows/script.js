let currentColor = [0, 0, 0]; // Inicialmente define a cor como preto
let strokes = []; // Array para armazenar os traços desenhados
let isErasing = false;

function setup() {
    createCanvas(400, 400);
    background(245, 242, 207);
}

function draw() {
    if (mouseIsPressed) {
        if (isErasing) {
            strokes.push({ x: mouseX, y: mouseY, erase: true }); // Adiciona traço ao array de traços com a marcação de apagar
        } else {
            strokeWeight(4);
            stroke(currentColor[0], currentColor[1], currentColor[2]);
            line(mouseX, mouseY, pmouseX, pmouseY);
            strokes.push({ x: mouseX, y: mouseY, erase: false }); // Adiciona traço ao array de traços
        }
    }
}

function keyPressed() {
    if (keyIsDown(90) && (keyIsDown(CONTROL) || keyIsDown(LEFT_CONTROL) || keyIsDown(RIGHT_CONTROL))) {
        undo(); // Se Ctrl+Z é pressionado, desfaz a última ação
    }
}

function undo() {
    if (strokes.length > 0) {
        strokes.pop(); // Remove o último traço do array
        background(245, 242, 207); // Limpa o canvas
        redrawStrokes(); // Redesenha todos os traços restantes
    }
}

function redrawStrokes() {
    for (let i = 0; i < strokes.length; i++) {
        if (!strokes[i].erase) {
            if (i === 0 || !strokes[i - 1].erase) {
                beginShape();
                vertex(strokes[i].x, strokes[i].y);
            } else {
                endShape();
            }
        }
    }
}

// Muda a cor do traço
function setColor(r, g, b) {
    currentColor = [r, g, b];
    isErasing = false; // Garante que o modo de apagar esteja desativado ao selecionar uma cor
}

// Define a cor de apagar
function setEraserColor() {
    isErasing = true;
}

