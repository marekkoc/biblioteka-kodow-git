Stwórzmy prosty przykład bezpośrednio w WebGL. WebGL jest znacznie bardziej niskopoziomowy niż Three.js czy Babylon.js, więc kod będzie dłuższy nawet dla prostej sceny.

Struktura projektu:
```
webgl-project/
  ├── index.html
  ├── styles.css
  └── main.js
```

1. `index.html`:
```html
<!DOCTYPE html>
<html>
<head>
    <title>WebGL Demo</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div id="info">WebGL Demo - Obracający się trójkąt i kwadrat</div>
    <canvas id="glCanvas"></canvas>
    <script src="main.js"></script>
</body>
</html>
```

2. `styles.css`:
```css
body {
    margin: 0;
    overflow: hidden;
}

#info {
    position: absolute;
    top: 10px;
    width: 100%;
    text-align: center;
    color: white;
    font-family: Arial, sans-serif;
    z-index: 100;
}

#glCanvas {
    width: 100vw;
    height: 100vh;
    display: block;
}
```

3. `main.js`:
```javascript
let gl;
let shaderProgram;
let rotation = 0;

// Vertex shader program
const vsSource = `
    attribute vec4 aVertexPosition;
    attribute vec4 aVertexColor;
    
    uniform mat4 uModelViewMatrix;
    uniform mat4 uProjectionMatrix;
    
    varying lowp vec4 vColor;
    
    void main() {
        gl_Position = uProjectionMatrix * uModelViewMatrix * aVertexPosition;
        vColor = aVertexColor;
    }
`;

// Fragment shader program
const fsSource = `
    varying lowp vec4 vColor;
    
    void main() {
        gl_FragColor = vColor;
    }
`;

// Inicjalizacja shaderów
function initShaderProgram(gl, vsSource, fsSource) {
    const vertexShader = loadShader(gl, gl.VERTEX_SHADER, vsSource);
    const fragmentShader = loadShader(gl, gl.FRAGMENT_SHADER, fsSource);

    const shaderProgram = gl.createProgram();
    gl.attachShader(shaderProgram, vertexShader);
    gl.attachShader(shaderProgram, fragmentShader);
    gl.linkProgram(shaderProgram);

    if (!gl.getProgramParameter(shaderProgram, gl.LINK_STATUS)) {
        alert('Nie udało się zainicjować shaderów: ' + gl.getProgramInfoLog(shaderProgram));
        return null;
    }

    return shaderProgram;
}

// Ładowanie pojedynczego shadera
function loadShader(gl, type, source) {
    const shader = gl.createShader(type);
    gl.shaderSource(shader, source);
    gl.compileShader(shader);

    if (!gl.getShaderParameter(shader, gl.COMPILE_STATUS)) {
        alert('Błąd podczas kompilacji shadera: ' + gl.getShaderInfoLog(shader));
        gl.deleteShader(shader);
        return null;
    }

    return shader;
}

// Inicjalizacja bufferów
function initBuffers(gl) {
    // Pozycje wierzchołków
    const positions = [
        // Trójkąt
        -0.5,  0.5,
        -0.8, -0.2,
        -0.2, -0.2,
        
        // Kwadrat
        0.2,  0.2,
        0.8,  0.2,
        0.2, -0.2,
        0.8, -0.2,
    ];

    const positionBuffer = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, positionBuffer);
    gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(positions), gl.STATIC_DRAW);

    // Kolory
    const colors = [
        // Trójkąt
        1.0, 0.0, 0.0, 1.0,
        0.0, 1.0, 0.0, 1.0,
        0.0, 0.0, 1.0, 1.0,
        
        // Kwadrat
        1.0, 0.0, 0.0, 1.0,
        0.0, 1.0, 0.0, 1.0,
        0.0, 0.0, 1.0, 1.0,
        1.0, 1.0, 0.0, 1.0,
    ];

    const colorBuffer = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, colorBuffer);
    gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(colors), gl.STATIC_DRAW);

    return {
        position: positionBuffer,
        color: colorBuffer,
    };
}

// Rysowanie sceny
function drawScene(gl, programInfo, buffers) {
    gl.clearColor(0.0, 0.0, 0.0, 1.0);
    gl.clear(gl.COLOR_BUFFER_BIT);

    const projectionMatrix = mat4.create();
    mat4.perspective(projectionMatrix, 45 * Math.PI / 180, gl.canvas.clientWidth / gl.canvas.clientHeight, 0.1, 100.0);

    const modelViewMatrix = mat4.create();
    mat4.translate(modelViewMatrix, modelViewMatrix, [0.0, 0.0, -6.0]);
    mat4.rotate(modelViewMatrix, modelViewMatrix, rotation, [0, 0, 1]);

    // Pozycje wierzchołków
    gl.bindBuffer(gl.ARRAY_BUFFER, buffers.position);
    gl.vertexAttribPointer(programInfo.attribLocations.vertexPosition, 2, gl.FLOAT, false, 0, 0);
    gl.enableVertexAttribArray(programInfo.attribLocations.vertexPosition);

    // Kolory
    gl.bindBuffer(gl.ARRAY_BUFFER, buffers.color);
    gl.vertexAttribPointer(programInfo.attribLocations.vertexColor, 4, gl.FLOAT, false, 0, 0);
    gl.enableVertexAttribArray(programInfo.attribLocations.vertexColor);

    gl.useProgram(programInfo.program);

    gl.uniformMatrix4fv(programInfo.uniformLocations.projectionMatrix, false, projectionMatrix);
    gl.uniformMatrix4fv(programInfo.uniformLocations.modelViewMatrix, false, modelViewMatrix);

    // Rysowanie trójkąta
    gl.drawArrays(gl.TRIANGLES, 0, 3);
    
    // Rysowanie kwadratu
    gl.drawArrays(gl.TRIANGLE_STRIP, 3, 4);
}

// Główna funkcja inicjalizująca
function main() {
    const canvas = document.querySelector("#glCanvas");
    gl = canvas.getContext("webgl");

    if (gl === null) {
        alert("Nie można zainicjować WebGL.");
        return;
    }

    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    gl.viewport(0, 0, canvas.width, canvas.height);

    shaderProgram = initShaderProgram(gl, vsSource, fsSource);

    const programInfo = {
        program: shaderProgram,
        attribLocations: {
            vertexPosition: gl.getAttribLocation(shaderProgram, 'aVertexPosition'),
            vertexColor: gl.getAttribLocation(shaderProgram, 'aVertexColor'),
        },
        uniformLocations: {
            projectionMatrix: gl.getUniformLocation(shaderProgram, 'uProjectionMatrix'),
            modelViewMatrix: gl.getUniformLocation(shaderProgram, 'uModelViewMatrix'),
        },
    };

    const buffers = initBuffers(gl);

    function render() {
        rotation += 0.01;
        drawScene(gl, programInfo, buffers);
        requestAnimationFrame(render);
    }
    requestAnimationFrame(render);
}

// Dodanie biblioteki gl-matrix
const script = document.createElement('script');
script.src = 'https://cdnjs.cloudflare.com/ajax/libs/gl-matrix/2.8.1/gl-matrix-min.js';
script.onload = main;
document.body.appendChild(script);
```

Ten przykład pokazuje:
1. Bezpośrednią pracę z WebGL
2. Shadery w GLSL
3. Bufory wierzchołków i kolorów
4. Transformacje macierzowe
5. Animację

Różnice między podejściami:
- WebGL jest najbardziej niskopoziomowy - masz pełną kontrolę, ale musisz napisać więcej kodu
- Three.js i Babylon.js są wysokopoziomowe - łatwiejsze w użyciu, ale mniej elastyczne
- WebGL wymaga znajomości shaderów i grafiki 3D na niższym poziomie

Chcesz, żebym wyjaśnił dokładniej jakąś część tego kodu? Na przykład shadery lub transformacje macierzowe?
