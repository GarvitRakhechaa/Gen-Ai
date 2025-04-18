// app.js

const canvas = document.getElementById('drawingCanvas');
const ctx = canvas.getContext('2d');
const penToolBtn = document.getElementById('penTool');
const eraserToolBtn = document.getElementById('eraserTool');
const clearCanvasBtn = document.getElementById('clearCanvas');
const lineToolBtn = document.getElementById('lineTool');
const rectangleToolBtn = document.getElementById('rectangleTool');
const circleToolBtn = document.getElementById('circleTool');
const strokeColorInput = document.getElementById('strokeColor');
const lineWidthInput = document.getElementById('lineWidth');

let isDrawing = false;
let currentTool = 'pen';
let startX, startY, lastX, lastY;
let strokeColor = strokeColorInput.value;
let lineWidth = lineWidthInput.value;

let drawnShapes = [];

// Set initial canvas size
setCanvasSize();

// Resize canvas on window resize
window.addEventListener('resize', setCanvasSize);

// Function to set canvas size based on window size
function setCanvasSize() {
 canvas.width = window.innerWidth * 0.95;
 canvas.height = window.innerHeight * 0.90;

 // Scale the canvas context for high DPI screens
 const scale = window.devicePixelRatio || 1;
 ctx.scale(scale, scale);

 // Adjust the canvas style size to the unscaled dimensions
 canvas.style.width = (canvas.width / scale) + 'px';
 canvas.style.height = (canvas.height / scale) + 'px';

 redrawShapes();
}


// Function to clear the canvas
function clearCanvas() {
 ctx.clearRect(0, 0, canvas.width, canvas.height);
 drawnShapes = []; // Clear the stored shapes as well
}

// Function to redraw all stored shapes
function redrawShapes() {
 const scale = window.devicePixelRatio || 1;
 ctx.clearRect(0, 0, canvas.width * scale, canvas.height * scale);
 drawnShapes.forEach(shape => {
 drawShape(shape);
 });
}

// Function to handle tool selection
function handleToolSelection(tool) {
 currentTool = tool;
 redrawShapes(); // Redraw the canvas when tool is selected
}

// Add event listeners to the toolbar buttons
penToolBtn.addEventListener('click', () => handleToolSelection('pen'));
eraserToolBtn.addEventListener('click', () => handleToolSelection('eraser'));
clearCanvasBtn.addEventListener('click', () => {
 clearCanvas();
});
lineToolBtn.addEventListener('click', () => handleToolSelection('line'));
rectangleToolBtn.addEventListener('click', () => handleToolSelection('rectangle'));
circleToolBtn.addEventListener('click', () => handleToolSelection('circle'));

// Add event listeners for color and size changes
strokeColorInput.addEventListener('change', () => {
 strokeColor = strokeColorInput.value;
});

lineWidthInput.addEventListener('change', () => {
 lineWidth = lineWidthInput.value;
});

// Function to get mouse position relative to the canvas
function getMousePos(canvas, event) {
 const rect = canvas.getBoundingClientRect();

 return {
 x: event.clientX - rect.left,
 y: event.clientY - rect.top
 };
}

// Function to start drawing
function startDrawing(event) {
 isDrawing = true;
 const pos = getMousePos(canvas, event);
 startX = pos.x;
 startY = pos.y;
 lastX = pos.x;
 lastY = pos.y;

 // Store initial mouse position
 lastX = pos.x;
 lastY = pos.y;

 event.preventDefault(); // Prevent scrolling on touch devices
}

// Function to draw
function draw(event) {
 if (!isDrawing) return;
 const pos = getMousePos(canvas, event);

 switch (currentTool) {
 case 'pen':
 drawLine(pos.x, pos.y);
 break;
 case 'eraser':
 erase(pos.x, pos.y);
 break;
 case 'line':
 case 'rectangle':
 case 'circle':
 // For line, rectangle, and circle, the drawing happens on mouseup
 break;
 }
 lastX = pos.x;
 lastY = pos.y;

 event.preventDefault(); // Prevent scrolling on touch devices
}

// Function to draw a line
function drawLine(x, y) {
 ctx.beginPath();
 ctx.moveTo(lastX, lastY);
 ctx.lineTo(x, y);
 ctx.strokeStyle = strokeColor;
 ctx.lineWidth = lineWidth;
 ctx.stroke();

 lastX = x;
 lastY = y;
}

// Function to erase
function erase(x, y) {
 ctx.clearRect(x - 5, y - 5, 10, 10);
}

function drawShape(shape) {
 switch (shape.tool) {
 case 'line':
 drawLineShape(shape.startX, shape.startY, shape.endX, shape.endY);
 break;
 case 'rectangle':
 drawRectangleShape(shape.startX, shape.startY, shape.endX, shape.endY);
 break;
 case 'circle':
 drawCircleShape(shape.startX, shape.startY, shape.endX, shape.endY);
 break;
 }
}

function drawLineShape(startX, startY, endX, endY) {
 ctx.beginPath();
 ctx.moveTo(startX, startY);
 ctx.lineTo(endX, endY);
 ctx.strokeStyle = strokeColor;
 ctx.lineWidth = lineWidth;
 ctx.stroke();
}

function drawRectangleShape(startX, startY, endX, endY) {
 ctx.beginPath();
 ctx.rect(startX, startY, endX - startX, endY - startY);
 ctx.strokeStyle = strokeColor;
 ctx.lineWidth = lineWidth;
 ctx.stroke();
}

function drawCircleShape(startX, startY, endX, endY) {
 const radius = Math.sqrt(Math.pow(endX - startX, 2) + Math.pow(endY - startY, 2));
 ctx.beginPath();
 ctx.arc(startX, startY, radius, 0, 2 * Math.PI);
 ctx.strokeStyle = strokeColor;
 ctx.lineWidth = lineWidth;
 ctx.stroke();
}

// Function to stop drawing
function stopDrawing() {
 if (!isDrawing) return;
 isDrawing = false;

 const pos = getMousePos(canvas, event);

 if (currentTool === 'line' || currentTool === 'rectangle' || currentTool === 'circle') {
 drawnShapes.push({
 tool: currentTool,
 startX: startX,
 startY: startY,
 endX: pos.x,
 endY: pos.y
 });
 drawShape(drawnShapes[drawnShapes.length - 1]);
 }
}

// Add event listeners for mouse events
canvas.addEventListener('mousedown', startDrawing);
canvas.addEventListener('mouseup', stopDrawing);
canvas.addEventListener('mouseout', stopDrawing);
canvas.addEventListener('mousemove', draw);

// Add event listeners for touch events
canvas.addEventListener('touchstart', startDrawing);
canvas.addEventListener('touchend', stopDrawing);
canvas.addEventListener('touchcancel', stopDrawing);
canvas.addEventListener('touchmove', draw);
