import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

// Podstawowa konfiguracja taka jak wcześniej...
const scene = new THREE.Scene();
scene.background = new THREE.Color(0x111111);
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
camera.position.z = 15; // Odsunięta kamera, żeby widzieć wszystkie obiekty
const renderer = new THREE.WebGLRenderer({ 
    canvas: document.querySelector('#canvas'),
    antialias: true 
});
renderer.setSize(window.innerWidth, window.innerHeight);
const controls = new OrbitControls(camera, renderer.domElement);

// Różne typy świateł
const pointLight = new THREE.PointLight(0xffffff, 1);
pointLight.position.set(5, 5, 5);
scene.add(pointLight);

const spotLight = new THREE.SpotLight(0xffffff, 1);
spotLight.position.set(-5, 5, 0);
spotLight.angle = Math.PI / 4;
spotLight.penumbra = 0.1;
scene.add(spotLight);

const directionalLight = new THREE.DirectionalLight(0xffffff, 0.5);
directionalLight.position.set(0, 5, -5);
scene.add(directionalLight);

const ambientLight = new THREE.AmbientLight(0x404040);
scene.add(ambientLight);

// Funkcja pomocnicza do tworzenia obiektów
function createObject(geometry, material, position) {
    const mesh = new THREE.Mesh(geometry, material);
    mesh.position.copy(position);
    scene.add(mesh);
    return mesh;
}

// Różne materiały i obiekty
const objects = [
    // Basic Material - najprostszy, nie reaguje na światło
    createObject(
        new THREE.BoxGeometry(),
        new THREE.MeshBasicMaterial({ color: 0xff0000 }),
        new THREE.Vector3(-8, 2, 0)
    ),

    // Lambert Material - matowy
    createObject(
        new THREE.BoxGeometry(),
        new THREE.MeshLambertMaterial({ color: 0x00ff00 }),
        new THREE.Vector3(-6, 2, 0)
    ),

    // Phong Material - błyszczący plastik
    createObject(
        new THREE.BoxGeometry(),
        new THREE.MeshPhongMaterial({ 
            color: 0x0000ff,
            shininess: 100
        }),
        new THREE.Vector3(-4, 2, 0)
    ),

    // Standard Material - fizyczny, metaliczny
    createObject(
        new THREE.BoxGeometry(),
        new THREE.MeshStandardMaterial({ 
            color: 0xffff00,
            metalness: 0.7,
            roughness: 0.3
        }),
        new THREE.Vector3(-2, 2, 0)
    ),

    // Physical Material - najbardziej realistyczny
    createObject(
        new THREE.BoxGeometry(),
        new THREE.MeshPhysicalMaterial({ 
            color: 0xff00ff,
            metalness: 0.5,
            roughness: 0.2,
            clearcoat: 1.0,
            clearcoatRoughness: 0.1
        }),
        new THREE.Vector3(0, 2, 0)
    ),

    // Toon Material - kreskówkowy
    createObject(
        new THREE.BoxGeometry(),
        new THREE.MeshToonMaterial({ color: 0x00ffff }),
        new THREE.Vector3(2, 2, 0)
    ),

    // Materiał z teksturą
    createObject(
        new THREE.SphereGeometry(0.5, 32, 32),
        new THREE.MeshStandardMaterial({ 
            color: 0xffffff,
            metalness: 0.5,
            roughness: 0.5,
            emissive: 0x222222
        }),
        new THREE.Vector3(4, 2, 0)
    ),

    // Materiał przezroczysty
    createObject(
        new THREE.BoxGeometry(),
        new THREE.MeshPhysicalMaterial({ 
            color: 0x88ff88,
            transparent: true,
            opacity: 0.5,
            metalness: 0.2,
            roughness: 0.1
        }),
        new THREE.Vector3(6, 2, 0)
    ),

    // Materiał z wirefreme
    createObject(
        new THREE.BoxGeometry(),
        new THREE.MeshBasicMaterial({ 
            color: 0xffffff,
            wireframe: true 
        }),
        new THREE.Vector3(8, 2, 0)
    )
];

// Dodajmy podłogę, żeby lepiej widzieć cienie
const floorGeometry = new THREE.PlaneGeometry(20, 10);
const floorMaterial = new THREE.MeshStandardMaterial({ 
    color: 0x808080,
    metalness: 0.2,
    roughness: 0.8
});
const floor = new THREE.Mesh(floorGeometry, floorMaterial);
floor.rotation.x = -Math.PI / 2;
floor.position.y = -2;
scene.add(floor);

// Włączmy cienie
renderer.shadowMap.enabled = true;
pointLight.castShadow = true;
spotLight.castShadow = true;
directionalLight.castShadow = true;
floor.receiveShadow = true;
objects.forEach(obj => {
    obj.castShadow = true;
    obj.receiveShadow = true;
});

// Animacja
function animate() {
    requestAnimationFrame(animate);
    objects.forEach(obj => {
        obj.rotation.x += 0.01;
        obj.rotation.y += 0.01;
    });
    controls.update();
    renderer.render(scene, camera);
}

animate();

// Dodajmy opis każdego materiału
const info = document.getElementById('info');
info.innerHTML = `
Three.js Demo - Materiały (od lewej):
Basic, Lambert, Phong, Standard, Physical, Toon, Tekstura, Przezroczysty, Wireframe
<br>
Kliknij i przeciągnij aby obrócić, scroll aby przybliżyć
`;