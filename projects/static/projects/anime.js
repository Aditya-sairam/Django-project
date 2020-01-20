"use strict";

const particleCount = 1000;
const particlePropCount = 9;
const particlePropsLength = particleCount * particlePropCount;
const spawnRadius = rand(100) + 100;
const noiseSteps = 6;

let canvas;
let ctx;
let center;
let tick;
let simplex;
let particleProps;
let positions;
let velocities;
let speeds;
let lifeSpans;
let sizes;
let hues;

function setup() {
	tick = 0;
	center = [];
	createCanvas();
	createParticles();
	draw();
}

function createParticles() {
	simplex = new SimplexNoise();
	particleProps = new Float32Array(particlePropsLength);
	
	let i;
	
	for (i = 0; i < particlePropsLength; i += particlePropCount) {
		initParticle(i);
	}
}

function initParticle(i) {
	let iy, ih, rd, rt, cx, sy, x, y, s, rv, vx, vy, t, h, w, l, ttl;
	
	iy = i + 1;
	ih = 0.5 * i | 0;
	rd = rand(spawnRadius);
	rt = rand(TAU);
	cx = cos(rt);
	sy = sin(rt);
	x = center[0] + cx * rd;
	y = center[1] + sy * rd;
	rv = randIn(0.1, 1);
	s = randIn(1, 8);
	vx = rv * cx * 0.1;
	vy = rv * sy * 0.1;
	w = randIn(0.1, 2);
	h = randIn(160,260);
	l = 0;
	ttl = randIn(50, 200);
	
	particleProps.set([x, y, vx, vy, s, h, w, l, ttl], i);
}

function drawParticle(i) {
	let n, dx, dy, dl, c;
	
	let [x, y, vx, vy, s, h, w, l, ttl] = particleProps.get(i, particlePropCount);
	
	n = simplex.noise3D(x * 0.0025, y * 0.0025, tick * 0.0005) * TAU * noiseSteps;
	vx = lerp(vx, cos(n), 0.05);
	vy = lerp(vy, sin(n), 0.05);
	dx = x + vx * s;
	dy = y + vy * s;
	dl = fadeInOut(l, ttl);
	c = `hsla(${h},50%,60%,${dl})`;

	l++;

	ctx.a.save();
	ctx.a.lineWidth = dl * w + 1;
	ctx.a.strokeStyle = c;
	ctx.a.beginPath();
	ctx.a.moveTo(x, y);
	ctx.a.lineTo(dx, dy);
	ctx.a.stroke();
	ctx.a.closePath();
	ctx.a.restore();
	
	particleProps.set([dx, dy, vx, vy, s, h, w, l, ttl], i);

	(checkBounds(x, y) || l > ttl) && initParticle(i);
}

function checkBounds(x, y) {
	return(
		x > canvas.a.width ||
		x < 0 ||
		y > canvas.a.height ||
		y < 0
	);
}

function createCanvas() {
	canvas = {
		a: document.createElement("canvas"),
		b: document.createElement("canvas")
	};
	canvas.b.style = `
		position: absolute;
		top: 0;
		left: 0;
		width: 100%;
		height: 100%;
	`;
	document.body.appendChild(canvas.b);
	ctx = {
		a: canvas.a.getContext("2d"),
		b: canvas.b.getContext("2d")
	};
	resize();
}

function resize() {
	const { innerWidth, innerHeight } = window;
	
	canvas.a.width = innerWidth;
  canvas.a.height = innerHeight;

  ctx.a.drawImage(canvas.b, 0, 0);

	canvas.b.width = innerWidth;
  canvas.b.height = innerHeight;
  
  ctx.b.drawImage(canvas.a, 0, 0);

  center[0] = 0.5 * canvas.a.width;
  center[1] = 0.5 * canvas.a.height;
}

function draw() {
	tick++;
	ctx.a.clearRect(0,0,canvas.a.width,canvas.a.height);
	
	ctx.b.fillStyle = 'rgba(0,0,0,0.1)';
	ctx.b.fillRect(0,0,canvas.b.width,canvas.b.height);
	
	let i = 0;
	
	for (; i < particlePropsLength; i += particlePropCount) {
		drawParticle(i);
	}
	
	ctx.b.save();
	ctx.b.filter = 'blur(8px)';
	ctx.b.globalCompositeOperation = 'lighten';
	ctx.b.drawImage(canvas.a, 0, 0);
	ctx.b.restore();
	
	ctx.b.save();
	ctx.b.globalCompositeOperation = 'lighter';
	ctx.b.drawImage(canvas.a, 0, 0);
	ctx.b.restore();
	
	window.requestAnimationFrame(draw);
}

window.addEventListener("load", setup);
window.addEventListener("resize", resize);