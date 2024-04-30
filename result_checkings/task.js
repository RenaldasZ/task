const fs = require("fs");
const text = fs.readFileSync("./data.txt").toString('utf-8');
const data = text.split("\r\n");
const processedData = [];

data.forEach(e => {
 processedData.push(e.split(","));
});

function formatTime(seconds) {
    const hours = Math.floor(seconds / 3600);
    const minutes = Math.floor((seconds % 3600) / 60);
    const remainingSeconds = seconds % 60;
 
    const formattedHours = String(hours).padStart(2, '0');
    const formattedMinutes = String(minutes).padStart(2, '0');
    const formattedSeconds = String(remainingSeconds).padStart(2, '0');
 
    return `${formattedHours}:${formattedMinutes}:${formattedSeconds}`;
 
}

//

let counterRed = 0;
let counterYellow = 0;
let counterGreen = 0

for (let i = 0; i<processedData.length; i++) {
        counterRed = processedData[i][0] == 1 ? counterRed + 1 : counterRed;
        counterYellow = processedData[i][1] == 1 ? counterYellow + 1 : counterYellow;
        counterGreen = processedData[i][2] == 1 ? counterGreen + 1 : counterGreen;
}

console.log("Red",counterRed,"Yellow",counterYellow,"Green",counterGreen);

//

let redTimeArray = [];
let yellowTimeArray = [];
let greenTimeArray = [];

for (let i = 0; i < processedData.length; i++) { 
    if (processedData[i][0] == 1 && processedData[i][1] != 1 && processedData[i][2] != 1) {
        redTimeArray.push(parseInt(processedData[i][3]))
    }
    if (processedData[i][1] == 1 && processedData[i][2] != 1 && processedData[i][0] != 1) {
        yellowTimeArray.push(parseInt(processedData[i][3]))
    }
    if (processedData[i][2] == 1 && processedData[i][1] != 1 && processedData[i][0] != 1) {
        greenTimeArray.push(parseInt(processedData[i][3]))
    }
}

const sumRed = redTimeArray.reduce((acc, cur) => acc + cur, 0);
const sumYellow = yellowTimeArray.reduce((acc, cur) => acc + cur, 0);
const sumGreen = greenTimeArray.reduce((acc, cur) => acc + cur, 0);

console.log("red", formatTime(sumRed),"yellow", formatTime(sumYellow),"green", formatTime(sumGreen));
