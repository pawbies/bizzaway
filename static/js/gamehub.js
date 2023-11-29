import * as THREE from '../lib/three.js/build/three.module.js';
import { OrbitControls } from './CustomOrbitControls.js'
import { OBJLoader } from './CustomOBJLoader.js'
import { MTLLoader } from './CustomMTLLoader.js'
import { GLTFLoader } from './CustomGLTFLoader.js'

let width = window.innerWidth;
let height = window.innerHeight;
let intersects = [];

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000); camera.position.z = 5;
const renderer = new THREE.WebGLRenderer();
const raycaster = new THREE.Raycaster();
const controls = new OrbitControls(camera, renderer.domElement);
const mouse = new THREE.Vector2;
const objLoader = new OBJLoader();
const mtlLoader = new MTLLoader();
const gltfLoader = new GLTFLoader();

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
    if (intersects.filter((object) => { return object.object.type != "GridHelper"; }).length == 0) return;

    for (let i = 0; i < intersects.length; i++)
    {
        if (intersects[i].object.type == "GridHelper") continue;
        intersects[i].object.material.wireframe = !intersects[i].object.material.wireframe;
        break;
    }
}

async function loadGLTF(path)
{
    return new Promise((resolve, reject) => {
    gltfLoader.load(
        path,

        ( gltf ) => {
            //scene.add(gltf.scene);
            resolve(gltf);
        },
        (xhr) => {console.log( ( xhr.loaded / xhr.total * 100 ) + '% loaded');},
        (error) => {console.log(error); reject(error);}
    );
    });
}

async function loadObj(objPath, mtlPath)
{
    return new Promise((resolve, reject) => {
    mtlLoader.load(mtlPath, 
    function( materials )
    {
            materials.preload();

            objLoader.setMaterials(materials);
            objLoader.load(
                objPath,
                ( object ) => {
                    //scene.add(object);
                    resolve(object);
                },
                (xhr) => {console.log( ( xhr.loaded / xhr.total * 100 ) + '% loaded');},
                (error) => {console.log(error);}
            );
        },
        (xhr) => {console.log( ( xhr.loaded / xhr.total * 100 ) + '% loaded');},
        (error) => {console.log(error); reject(error);}
    )
    });
}


/* Add Light */
const light = new THREE.AmbientLight( 0xF0F0F0 );
scene.add( light );


/* Add Grid */
const gridHelper = new THREE.GridHelper(250, 250);
scene.add(gridHelper);

/* Setup Renderer */
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);


/* Add Pizza Cube */
const geometry = new THREE.BoxGeometry(1, 1, 1);
const textureLoader = new THREE.TextureLoader();
textureLoader.setPath("/static/img/");
const textureCube = textureLoader.load("game1_thumb.png");
const material = new THREE.MeshBasicMaterial({color: 0xffffff, map: textureCube});
const cube = new THREE.Mesh(geometry, material);
scene.add(cube);


/* Add Cube*/
let ccube = await loadGLTF('/static/objs/ccube.glb');
scene.add(ccube.scene);

/* Add Background */
scene.background = textureLoader.load("wallpaper.jpg");

let speed = 0.1;

function animate()
{
    requestAnimationFrame(animate);

    cube.rotation.x += 0.01;
    cube.rotation.y += 0.01;

    if (cube.position.z < -200 || cube.position.z > 200)
        speed *= -1;
    cube.position.z += speed;
    

    renderer.render(scene, camera);
    controls.update();
}

animate();
