import * as THREE from './lib/three.js/build/three.module.js';
import { OrbitControls } from './lib/three.js/examples/jsm/controls/OrbitControls.js'

let width = window.innerWidth;
let height = window.innerHeight;
let intersects = [];

function checkInsersects()
{
    raycaster.setFromCamera(mouse, camera);
    intersects = raycaster.intersectObjects(scene.children, true);
}

function updateMouse(x, y) { mouse.set((x/width) * 2 -1, -(y / height) * 2 + 1); }
window.onmousemove =  (evt) => {updateMouse(evt.clientX, evt.clientY);};
window.onload = (evt) => {updateMouse(evt.clientX, evt.clientY);};
window.onclick = () => {
    checkInsersects();
    if (intersects.length == 0) return;
    console.log("yay");
    intersects[0].object.material.wireframe = !intersects[0].object.material.wireframe;
}

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer();
const raycaster = new THREE.Raycaster();
//const controls = new THREE.OrbitControls(camera, renderer.domElement);
const mouse = new THREE.Vector2;

renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);


const geometry = new THREE.BoxGeometry(1, 1, 1);
const loader = new THREE.TextureLoader();
loader.setPath("/static/img/");
const textureCube = loader.load("game1_thumb.png");
const material = new THREE.MeshBasicMaterial({color: 0xffffff, map: textureCube});
const cube = new THREE.Mesh(geometry, material);

scene.add(cube);

camera.position.z = 5;

let speed = 1;

function animate()
{
    requestAnimationFrame(animate);

    cube.rotation.x += 0.01;
    cube.rotation.y += 0.01;

    if (cube.position.z < -200 || cube.position.z > 0)
        speed *= -1;
    cube.position.z += speed
    

    renderer.render(scene, camera);

    console.log(cube.rotation.x, cube.rotation.y);
}
animate();