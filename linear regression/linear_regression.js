<script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/0.8.0/p5.js"></script>

function setup() {
  createCanvas(400, 400);
}

var b = 0;
var m = 1;
let data = [];
let ymean = 0;

function mousePressed() {
  var x = map(mouseX, 0, width, 0, 1);
  var y = map(mouseY, 0, height, 1, 0);
  var point = createVector(x, y);
  data.push(point);
  // console.clear();
  console.log("X:"+x+" Y:"+y);
  console.log(ymean);
  console.log(data);
}

function linearRegression() {
  var xsum = 0;
  var ysum = 0;
  //Summerar den totala x och y
  for (let i = 0; i < data.length; i++) {
    xsum = data[i].x;
    ysum = data[i].y;
  }
  //Räknar ut medelvärdet
  var xmean = xsum / data.length;
  ymean = ysum / data.length;
  var numirator = 0;
  var denomirator = 0;
  //Räknar ut numirator och denomirator (x-xmedel * y- ymedel)
  //(x-xmedel x- xmedel (upphöjt till två))
  for (let u = 0; u < data.length; u++) {
    var x = data[u].x;
    var y = data[u].y;
    numirator += (x - xmean) * (y - ymean);
    denomirator += (x - xmean) * (x - xmean);
  }
  //m är lika med numiratorn / denomiratorn
  m = numirator / denomirator;
  //b = y medel - m * xmedel
  b = ymean - m * xmean;
}

function drawLine() {
  //x1 är början på x, x2 slutet. Y1 och y2 bestäms utifrån m*x+b
  var x1 = 0;
  var y1 = m * x1 + b;
  var x2 = 1;
  var y2 = m * x2 + b;

  x1 = map(x1, 0, 1, 0, width);
  y1 = map(y1, 0, 1, height, 0);
  x2 = map(x2, 0, 1, 0, width);
  y2 = map(y2, 0, 1, height, 0);

  stroke(255, 0, 255);
  line(x1, y1, x2, y2);
}

function draw() {
  background(51);
  
    //Rita ut varje datapunkt
  for (let i = 0; i < data.length; i++) {
    var x = map(data[i].x, 0, 1, 0, width);
    var y = map(data[i].y, 0, 1, height, 0);
    fill(255);
    stroke(255);
    ellipse(x, y, 8, 8)
  }
  //Om vi har mer än 1 punkt räkna ut och rita ut sträcket.
  if (data.length > 1) {
    linearRegression();
    drawLine();
  }
}