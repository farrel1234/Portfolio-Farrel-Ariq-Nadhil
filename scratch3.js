
const fs = require("fs");
let html = fs.readFileSync("insights.html", "utf8");

html = html.replace("if (storiesData[storyId]) {", "if (storyKeys.includes(storyId)) {");
fs.writeFileSync("insights.html", html);
console.log("Replaced hash check");

