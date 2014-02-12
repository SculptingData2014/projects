// Modify this per file saved from Python exploration:
String tableName = "values.csv";

Table table;
float[] xVals, yVals;
float minX, maxX, minY, maxY;
float plotX1, plotX2, plotY1, plotY2;

void setup() {
  size(720, 400);

  plotX1 = 20;
  plotX2 = width - plotX1;
  plotY1 = 30;
  plotY2 = height - plotY1;

  loadData();
  smooth();
}

void loadData() {
  table = loadTable(tableName, "header"); 
  int numRows = table.getRowCount();
  xVals = new float[numRows];
  yVals = new float[numRows];
  
  for (int row = 0; row < numRows; row++) {
    xVals[row] = table.getFloat(row, 0);
    yVals[row] = table.getFloat(row, 1);
  }
  
  minX = min(xVals);
  maxX = max(xVals);
  minY = min(yVals);
  maxY = max(yVals);
}

void draw() {
  background(224);   
  // Show the plot area as a white box.   
  fill(255);   
  rectMode(CORNERS);   
  noStroke();   
  rect(plotX1, plotY1, plotX2, plotY2);   
  
  strokeWeight(5);   
  stroke(#5679C1);   
  for (int row = 0; row < xVals.length; row++) {
     float x = map(xVals[row], minX, maxX, plotX1, plotX2);
     float y = map(yVals[row], minY, maxY, plotY1, plotY2);
     point(x, y);
  }   
}

