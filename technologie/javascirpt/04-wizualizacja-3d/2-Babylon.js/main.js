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