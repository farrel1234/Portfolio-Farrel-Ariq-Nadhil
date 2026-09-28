
const fs = require("fs");
let html = fs.readFileSync("insights.html", "utf8");
const regex = /\/\/ STORIES DATABASE.*?(?=let currentStoryId = null;)/s;
const replacement = `// STORIES DATABASE NOW LAZY-LOADED VIA JSON
        // The storyKeys are dynamically extracted from the DOM to maintain next/prev navigation
        let storyKeys = [];
        document.addEventListener("DOMContentLoaded", () => {
            const cards = Array.from(document.querySelectorAll(".story-card"));
            storyKeys = cards.map(card => {
                const onclickAttr = card.getAttribute("onclick");
                if (onclickAttr) {
                    const match = onclickAttr.match(/'([^']+)'/);
                    return match ? match[1] : null;
                }
                return null;
            }).filter(k => k);
        });
        
        `;
if (regex.test(html)) {
    html = html.replace(regex, replacement);
    fs.writeFileSync("insights.html", html);
    console.log("Successfully replaced via regex");
} else {
    console.log("Regex did not match");
}

