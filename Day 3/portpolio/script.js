console.log('Portfolio script loaded!');

// Update footer with current year
document.addEventListener('DOMContentLoaded', function() {
    const footer = document.querySelector('footer');
    const currentYear = new Date().getFullYear();
    footer.innerHTML = '<p>&copy; ' + currentYear + ' Garvit Rakhecha</p>';

    // Three.js Scene
    const canvas = document.getElementById('three-canvas');
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, canvas.offsetWidth / canvas.offsetHeight, 0.1, 1000);

    const renderer = new THREE.WebGLRenderer({ canvas: canvas });
    renderer.setSize(canvas.offsetWidth, canvas.offsetHeight);

    // Neural Network Visualization
    const layerCount = 3; // Number of layers
    const neuronCounts = [5, 3, 1]; // Neurons in each layer
    const layerSpacing = 2;
    const neuronSpacing = 1;

    const layers = [];

    for (let i = 0; i < layerCount; i++) {
        const layer = new THREE.Group();
        layers.push(layer);
        const neuronCount = neuronCounts[i];

        for (let j = 0; j < neuronCount; j++) {
            const geometry = new THREE.SphereGeometry(0.2, 32, 32);
            const material = new THREE.MeshBasicMaterial({ color: 0xffffff });
            const neuron = new THREE.Mesh(geometry, material);

            neuron.position.x = (j - (neuronCount - 1) / 2) * neuronSpacing;
            neuron.position.y = 0;
            neuron.position.z = 0;

            layer.add(neuron);
        }

        layer.position.x = 0;
        layer.position.y = 0;
        layer.position.z = (i - (layerCount - 1) / 2) * layerSpacing;
        scene.add(layer);
    }

    // Connect the neurons (crude approximation)
    for (let i = 0; i < layerCount - 1; i++) {
        const currentLayer = layers[i];
        const nextLayer = layers[i + 1];

        for (let j = 0; j < currentLayer.children.length; j++) {
            for (let k = 0; k < nextLayer.children.length; k++) {
                const material = new THREE.LineBasicMaterial({ color: 0xaaaaaa });
                const geometry = new THREE.Geometry();

                geometry.vertices.push(currentLayer.children[j].position.clone().add(currentLayer.position));
                geometry.vertices.push(nextLayer.children[k].position.clone().add(nextLayer.position));

                const line = new THREE.Line(geometry, material);
                scene.add(line);
            }
        }
    }

    camera.position.z = 5;

    function animate() {
        requestAnimationFrame(animate);
        renderer.render(scene, camera);
    }

    animate();
});