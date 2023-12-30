const debug = false;




import * as THREE from '../lib/three.js/build/three.module.js';
import { OrbitControls } from './CustomOrbitControls.js'
import { OBJLoader } from './CustomOBJLoader.js'
import { MTLLoader } from './CustomMTLLoader.js'
import { GLTFLoader } from './CustomGLTFLoader.js'

let width = window.innerWidth;
let height = window.innerHeight;
let intersects = [];

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000); camera.position.z = 2;
const renderer = new THREE.WebGLRenderer();
const raycaster = new THREE.Raycaster();
let controls;
if (debug) {
controls = new OrbitControls(camera, renderer.domElement);
}
const mouse = new THREE.Vector2;
const objLoader = new OBJLoader();
const mtlLoader = new MTLLoader();
const gltfLoader = new GLTFLoader();
let gameObjects = [];
let gameUrls = [];
let currentObject = 0;

function checkInsersects()
{
    raycaster.setFromCamera(mouse, camera);
    intersects = raycaster.intersectObjects(scene.children, true);
}

function updateMouse(x, y) { mouse.set((x/width) * 2 -1, -(y / height) * 2 + 1); }
window.onmousemove =  (evt) => {updateMouse(evt.clientX, evt.clientY);};
window.onload = (evt) => {updateMouse(evt.clientX, evt.clientY);};
window.onclick = () => {
    if (debug)
    {

    checkInsersects();
    if (intersects.filter((object) => { return object.object.type != "GridHelper"; }).length == 0) return;

    for (let i = 0; i < intersects.length; i++)
    {
        if (intersects[i].object.type == "GridHelper") continue;
        intersects[i].object.material.wireframe = !intersects[i].object.material.wireframe;
        break;
    }
    }
}
window.onresize = () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();

    renderer.setSize( window.innerWidth, window.innerHeight );
}
window.onkeydown = (evt) => {

    if (evt.key == "ArrowLeft")
    {
        if (currentObject <= 0)
            currentObject = gameObjects.length-1;
        else
            currentObject--;


    }
    else if (evt.key == "ArrowRight")
    {
        if (currentObject >= gameObjects.length-1)
            currentObject = 0;
        else
            currentObject++;
    }
    else if (evt.key == "Enter")
    {
        location.replace(gameUrls[currentObject]);
    }


    for (let i = 0; i < gameObjects.length; i++)
    {
        if (i == currentObject)
        {
            gameObjects[i].scene.visable = true;
            gameObjects[i].scene.visible = true;
        }
        else
        {
            gameObjects[i].scene.visable = false;
            gameObjects[i].scene.visible = false;
        }
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
const light = new THREE.AmbientLight( 0xFFFFFF );
scene.add( light );


/* Add Grid */
const gridHelper = new THREE.GridHelper(250, 250);
scene.add(gridHelper);


/* Setup Renderer */
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

const textureLoader = new THREE.TextureLoader();
textureLoader.setPath("/static/img/");



/* Add pizza*/
console.log("Pizza Slice by Quaternius (https://poly.pizza/m/CA4HtaaMJn)")
let pizza = await loadGLTF('/static/objs/pizza.glb');
pizza.scene.rotation.x = 1.5;
gameObjects.push(pizza);
gameUrls.push("/game/");
scene.add(pizza.scene);

let ccube = await loadGLTF('/static/objs/ccube.glb');
gameObjects.push(ccube);
gameUrls.push("/game/dooklin_game/")
ccube.scene.visable = false;
ccube.scene.visible = false;
console.log(ccube.scene.scale);
ccube.scene.scale.x /= 2;
ccube.scene.scale.y /= 2;
ccube.scene.scale.z /= 2;
scene.add(ccube.scene);

/* Add Background */
scene.background = textureLoader.load("wallpaper.jpg");

let speed = 0.01;

if (debug) {
console.log(controls.keys);
controls.enabled = true;
}

function animate()
{
    requestAnimationFrame(animate);
    
    gameObjects[currentObject].scene.rotation.z += speed;

    renderer.render(scene, camera);

    if (debug) controls.update();
}

animate();
