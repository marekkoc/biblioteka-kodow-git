Przygotuję dwa oddzielne projekty: jeden z Three.js i jeden z Babylon.js.

PROJEKT 1: Three.js
Struktura folderów:
```
three-project/
  ├── index.html
  ├── styles.css
  └── main.js
```

1. `index.html`:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Three.js Demo</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div id="info">Three.js Demo - Kliknij i przeciągnij aby obrócić</div>
    <canvas id="canvas"></canvas>
    <script type="importmap">
        {
            "imports": {
                "three": "https://unpkg.com/three@0.160.0/build/three.module.js",
                "three/addons/": "https://unpkg.com/three@0.160.0/examples/jsm/"
            }
        }
    </script>
    <script type="module" src="main.js"></script>
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

#canvas {
    width: 100vw;
    height: 100vh;
    display: block;
}
```

3. `main.js`:
```javascript
import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

// Scena
const scene = new THREE.Scene();
scene.background = new THREE.Color(0x000000);

// Kamera
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
camera.position.z = 5;

// Renderer
const renderer = new THREE.WebGLRenderer({ canvas: document.querySelector('#canvas') });
renderer.setSize(window.innerWidth, window.innerHeight);

// Kontrole
const controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping = true;

// Światło
const light = new THREE.PointLight(0xffffff, 1, 100);
light.position.set(0, 0, 10);
scene.add(light);

// Obiekty
const geometry = new THREE.BoxGeometry();
const material = new THREE.MeshPhongMaterial({ color: 0x00ff00 });
const cube = new THREE.Mesh(geometry, material);
scene.add(cube);

const sphereGeometry = new THREE.SphereGeometry(0.5, 32, 32);
const sphereMaterial = new THREE.MeshPhongMaterial({ color: 0xff0000 });
const sphere = new THREE.Mesh(sphereGeometry, sphereMaterial);
sphere.position.x = 2;
scene.add(sphere);

// Animacja
function animate() {
    requestAnimationFrame(animate);
    cube.rotation.x += 0.01;
    cube.rotation.y += 0.01;
    controls.update();
    renderer.render(scene, camera);
}

// Responsywność
window.addEventListener('resize', () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
});

animate();
```

PROJEKT 2: Babylon.js
Struktura folderów:
```
babylon-project/
  ├── index.html
  ├── styles.css
  └── main.js
```

1. `index.html`:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Babylon.js Demo</title>
    <link rel="stylesheet" href="styles.css">
    <script src="https://cdn.babylonjs.com/babylon.js"></script>
</head>
<body>
    <div id="info">Babylon.js Demo - Kliknij i przeciągnij aby obrócić</div>
    <canvas id="renderCanvas"></canvas>
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

#renderCanvas {
    width: 100vw;
    height: 100vh;
    touch-action: none;
}
```

3. `main.js`:
```javascript
window.addEventListener('DOMContentLoaded', function() {
    const canvas = document.getElementById('renderCanvas');
    const engine = new BABYLON.Engine(canvas, true);

    const createScene = function() {
        // Scena
        const scene = new BABYLON.Scene(engine);
        scene.clearColor = new BABYLON.Color3(0, 0, 0);

        // Kamera
        const camera = new BABYLON.ArcRotateCamera("camera", 
            0, Math.PI / 3, 10, 
            BABYLON.Vector3.Zero(), 
            scene
        );
        camera.attachControl(canvas, true);

        // Światło
        const light = new BABYLON.HemisphericLight("light", 
            new BABYLON.Vector3(0, 1, 0), 
            scene
        );

        // Sześcian
        const box = BABYLON.MeshBuilder.CreateBox("box", {}, scene);
        box.position.x = -2;
        const boxMaterial = new BABYLON.StandardMaterial("boxMaterial", scene);
        boxMaterial.diffuseColor = new BABYLON.Color3(0, 1, 0);
        box.material = boxMaterial;

        // Sfera
        const sphere = BABYLON.MeshBuilder.CreateSphere("sphere", {
            diameter: 2
        }, scene);
        sphere.position.x = 2;
        const sphereMaterial = new BABYLON.StandardMaterial("sphereMaterial", scene);
        sphereMaterial.diffuseColor = new BABYLON.Color3(1, 0, 0);
        sphere.material = sphereMaterial;

        // Animacja
        scene.registerBeforeRender(function() {
            box.rotation.y += 0.01;
            box.rotation.x += 0.01;
        });

        return scene;
    }

    const scene = createScene();

    engine.runRenderLoop(function() {
        scene.render();
    });

    window.addEventListener('resize', function() {
        engine.resize();
    });
});
```

Aby uruchomić każdy z projektów:
1. Utwórz oddzielne foldery dla każdego projektu
2. Skopiuj odpowiednie pliki do każdego folderu
3. Uruchom lokalny serwer w folderze projektu (możesz użyć np. Live Server w VS Code)
4. Otwórz stronę w przeglądarce

Każdy projekt pokazuje:
- Podstawową scenę 3D
- Interaktywną kamerę (możesz obracać scenę myszką)
- Animowane obiekty 3D
- Oświetlenie
- Responsywność (dostosowuje się do rozmiaru okna)

Chcesz, żebym pokazał jak dodać więcej interaktywnych elementów do któregoś z tych projektów?
