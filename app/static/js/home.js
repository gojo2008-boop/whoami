// Set up the canvas and context
const canvas = document.getElementById('visuals');
const ctx = canvas.getContext('2d');

// Set canvas size to window size
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

// Bokeh effect configuration
const bokehCount = 30;
const bokehSizeRange = [30, 100];

// Create an array to store bokeh circles
let bokehCircles = [];

// Curated dreamy shades of red, blue, and purple
const bokehPalette = [
  'rgba(255, 102, 178, OPACITY)',  // soft pink-red
  'rgba(204, 102, 255, OPACITY)',  // lavender purple
  'rgba(102, 153, 255, OPACITY)',  // soft blue
  'rgba(255, 153, 204, OPACITY)',  // blush
  'rgba(153, 102, 255, OPACITY)',  // deeper purple
  'rgba(102, 204, 255, OPACITY)',  // baby blue
  'rgba(255, 128, 170, OPACITY)',  // rose
  'rgba(178, 102, 255, OPACITY)',  // vibrant violet
];

// Generate random bokeh circles
function generateBokehCircles() {
  bokehCircles = [];

  for (let i = 0; i < bokehCount; i++) {
    let size = Math.random() * (bokehSizeRange[1] - bokehSizeRange[0]) + bokehSizeRange[0];
    let x = Math.random() * canvas.width;
    let y = Math.random() * canvas.height;
    let opacity = Math.random() * 0.3 + 0.15;
    let colorBase = bokehPalette[Math.floor(Math.random() * bokehPalette.length)];
    let color = colorBase.replace('OPACITY', opacity.toFixed(2));
    let vx = (Math.random() - 0.5) * 0.4;
    let vy = (Math.random() - 0.5) * 0.4;

    bokehCircles.push({ x, y, size, color, opacity, vx, vy });
  }
}

// Animate bokeh circles
function animateBokeh() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  bokehCircles.forEach(circle => {
    let gradient = ctx.createRadialGradient(circle.x, circle.y, 0, circle.x, circle.y, circle.size);
    gradient.addColorStop(0, circle.color);
    gradient.addColorStop(1, 'rgba(0, 0, 0, 0)');

    ctx.beginPath();
    ctx.arc(circle.x, circle.y, circle.size, 0, Math.PI * 2, false);
    ctx.fillStyle = gradient;
    ctx.fill();

    // Update position
    circle.x += circle.vx;
    circle.y += circle.vy;

    // Bounce at edges
    if (circle.x < 0 || circle.x > canvas.width) circle.vx *= -1;
    if (circle.y < 0 || circle.y > canvas.height) circle.vy *= -1;
  });

  requestAnimationFrame(animateBokeh);
}

// Init
window.onload = () => {
  generateBokehCircles();
  animateBokeh();
};

window.onresize = () => {
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
  generateBokehCircles();
};






















