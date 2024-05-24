// script.js
console.log("Script loaded");

import * as THREE from 'https://cdn.jsdelivr.net/npm/three@0.164.1/build/three.module.js';
import { OrbitControls } from 'https://cdn.jsdelivr.net/npm/three@0.164.1/examples/jsm/controls/OrbitControls.js';
import { GLTFLoader } from 'https://cdn.jsdelivr.net/npm/three@0.164.1/examples/jsm/loaders/GLTFLoader.js';

console.log("Modules imported");
console.log("hellow world");

const w = window.innerWidth;
const h = window.innerHeight;
const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setSize(w, h);
document.body.appendChild(renderer.domElement);

const fov = 75;
const aspect = w / h;
const near = 0.1;
const far = 10;
const camera = new THREE.PerspectiveCamera(fov, aspect, near, far);
camera.position.set(0, 2, 5);

console.log("Camera setup");

const scene = new THREE.Scene();
const Spheregeo = new THREE.SphereGeometry(4, 50, 50);
const material = new THREE.MeshBasicMaterial({
    color: 0xccff,
});
const axishelper = new THREE.AxesHelper(5);
scene.add(axishelper);

console.log("Scene and helpers setup");

const sphere = new THREE.Mesh(Spheregeo, material);
sphere.position.set(2, 3, 5);
scene.add(sphere);

console.log("Sphere added to scene");

let step = 0;
const speed = 0.01;

function animate(time) {
    step += speed;
    sphere.position.y = 10 * Math.abs(Math.sin(step));
    renderer.render(scene, camera);
}

renderer.setAnimationLoop(animate);

console.log("Animation loop setup");
