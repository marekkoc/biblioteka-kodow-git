import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

// Scena
const scene = new THREE.Scene();
scene.background = new THREE.Color(0x111111);

// Kamera
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
camera.position.z = 5;

// Renderer z włączonym antyaliasingiem
const renderer = new THREE.WebGLRenderer({ 
    canvas: document.querySelector('#canvas'),
    antialias: true  // dodaje wygładzanie krawędzi
});
renderer.setSize(window.innerWidth, window.innerHeight);

// Kontrole
const controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping = true;

// Światła - dodajemy kilka źródeł światła
const pointLight = new THREE.PointLight(0xffffff, 1, 100);
pointLight.position.set(5, 5, 5);
scene.add(pointLight);

const pointLight2 = new THREE.PointLight(0xffffff, 0.5, 100);
pointLight2.position.set(-5, -5, -5);
scene.add(pointLight2);

// Światło ambientowe dla lepszego wypełnienia cieni
const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
scene.add(ambientLight);

// Obiekty z lepszymi materiałami
const geometry = new THREE.BoxGeometry();
const material = new THREE.MeshStandardMaterial({ 
    color: 0x00ff00,
    metalness: 0.3,    // stopień metaliczności
    roughness: 0.2,    // stopień chropowatości
    emissive: 0x072300 // delikatna poświata
});
const cube = new THREE.Mesh(geometry, material);
scene.add(cube);

const sphereGeometry = new THREE.SphereGeometry(0.5, 32, 32);
const sphereMaterial = new THREE.MeshStandardMaterial({ 
    color: 0xff0000,
    metalness: 0.3,
    roughness: 0.2,
    emissive: 0x230707
});
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