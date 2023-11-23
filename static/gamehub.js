import * as THREE from './lib/three.js/build/three.module.js';

let width = window.innerWidth;
let height = window.innerHeight;
let intersects = [];

function updateMouse(x, y) { mouse.set((x/width) * 2 -1, -(y / height) * 2 + 1); }
window.onmousemove =  (evt) => {updateMouse(evt.clientX, evt.clientY);};
window.onload = (evt) => {updateMouse(evt.clientX, evt.clientY);};

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer();
const raycaster = new THREE.Raycaster();
const mouse = new THREE.Vector2;

renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);


const geometry = new THREE.BoxGeometry(1, 1, 1);
const material = new THREE.MeshBasicMaterial({color: 0x00ff00, wireframe: true});
const cube = new THREE.Mesh(geometry, material);

scene.add(cube);

camera.position.z = 5;



function animate()
{
    requestAnimationFrame(animate);

    cube.rotation.x += 0.01;
    cube.rotation.y += 0.01;

    raycaster.setFromCamera(mouse, camera);
    intersects = raycaster.intersectObjects(scene.children, true);

    if (intersects.length > 0)
    {
        console.log("hit");
    }

    renderer.render(scene, camera);
}
animate();

