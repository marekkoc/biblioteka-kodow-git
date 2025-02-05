Tak! W JavaScript mamy kilka popularnych bibliotek do wizualizacji 3D. Najważniejsze z nich to:

1. Three.js - najpopularniejsza biblioteka 3D w JS:
```javascript
// Prosty przykład Three.js
import * as THREE from 'three';

// Tworzymy scenę
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer();

// Dodajemy kostkę
const geometry = new THREE.BoxGeometry();
const material = new THREE.MeshBasicMaterial({ color: 0x00ff00 });
const cube = new THREE.Mesh(geometry, material);
scene.add(cube);

camera.position.z = 5;

// Animacja
function animate() {
    requestAnimationFrame(animate);
    cube.rotation.x += 0.01;
    cube.rotation.y += 0.01;
    renderer.render(scene, camera);
}
animate();
```

2. Babylon.js - zaawansowany silnik 3D:
- Świetny do gier
- Wbudowana fizyka
- Zaawansowane efekty wizualne

3. WebGL - niskopoziomowy dostęp do grafiki 3D:
- Działa bezpośrednio w przeglądarce
- Wymaga więcej kodu niż Three.js
- Daje pełną kontrolę

4. A-Frame - do VR/AR:
```html
<a-scene>
  <a-box position="-1 0.5 -3" rotation="0 45 0" color="#4CC3D9"></a-box>
  <a-sphere position="0 1.25 -5" radius="1.25" color="#EF2D5E"></a-sphere>
  <a-cylinder position="1 0.75 -3" radius="0.5" height="1.5" color="#FFC65D"></a-cylinder>
  <a-plane position="0 0 -4" rotation="-90 0 0" width="4" height="4" color="#7BC8A4"></a-plane>
  <a-sky color="#ECECEC"></a-sky>
</a-scene>
```

Chcesz zobaczyć praktyczny przykład z jedną z tych bibliotek? Mogę pokazać Ci jak stworzyć prostą scenę 3D z interaktywnymi obiektami używając Three.js.
