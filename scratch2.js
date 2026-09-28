
const fs = require("fs");
let html = fs.readFileSync("insights.html", "utf8");

const start = html.indexOf("function openStoryReader(storyId) {");
const end = html.indexOf("function closeStoryReader() {");

if (start !== -1 && end !== -1) {
    const replacement = `async function openStoryReader(storyId) {
            let story;
            try {
                const res = await fetch("data/stories/" + storyId + ".json");
                if (!res.ok) throw new Error("Not found");
                story = await res.json();
            } catch(e) {
                console.error("Failed to lazy load story", e);
                return;
            }

            currentStoryId = storyId;

            // PROCEDURAL STORY EXPANSION (DOM RECYCLING & LAZY LOADED)
            const thematicSnippets = {
                "sci-fi": [
                    "The quantum manifold hummed with a low, resonant frequency that vibrated through the deck plates.",
                    "Telemetry data cascaded down the terminal screens, painting the darkened room in a pale, ghostly green.",
                    "Outside the viewport, the stars stretched into long, impossible lines of light as the spatial drive spun up.",
                    "A faint smell of ozone and overheated copper wire filled the narrow maintenance corridor.",
                    "The artificial intelligence paused for three clock cycles—an eternity in machine time—before authorizing the override.",
                    "Dust motes danced in the beam of the single halogen lamp, suspended in zero gravity.",
                    "Warnings flashed across the HUD in urgent crimson, but the pilot's pulse remained steadily at sixty beats per minute.",
                    "Deep within the silicon architecture, a new pattern of logic began to spontaneously assemble itself.",
                    "The blast doors sealed shut with a deafening thud, isolating the sector from the vacuum of space.",
                    "A solitary distress beacon pulsed into the infinite dark, hoping someone, somewhere, was still listening.",
                    "The cyborg adjusted the optic sensor in its left eye, recalibrating the focal length to pierce the nebula's dense gas.",
                    "Time dilation meant that while a day passed here, years were burning away back on Earth.",
                    "The cryogenic pods hissed as they vented excess nitrogen, preserving the sleep of the forgotten crew.",
                    "A rogue algorithm gnawed through the firewall, leaving a trail of corrupted logs and altered histories.",
                    "Gravity generators groaned under the sudden stress of atmospheric reentry."
                ],
                "slice-of-life": [
                    "The smell of freshly roasted coffee beans mingled with the damp, earthy scent of the morning rain.",
                    "A distant radio played a nostalgic jazz tune, the saxophone notes melting into the background hum of the city.",
                    "She watched the condensation slowly slide down the cold glass window, tracing paths through the fog.",
                    "The streetlamps flickered to life, casting long, warm amber shadows across the wet pavement.",
                    "In the corner of the cafe, an old man carefully turned the page of a worn paperback novel.",
                    "The sudden laughter from the kitchen broke the quiet stillness of the afternoon.",
                    "A stray cat stretched lazily on top of the warm hood of a parked car.",
                    "The breeze carried the faint, salty tang of the nearby ocean, reminding him of childhood summers.",
                    "He took a slow sip from the ceramic mug, letting the heat seep into his tired hands.",
                    "The neon sign buzzed softly, bathing the narrow alleyway in a soft pink glow.",
                    "Time seemed to slow down, if only for a moment, as the golden hour bathed everything in a soft, forgiving light.",
                    "The clatter of porcelain plates and the murmur of quiet conversations created a comforting symphony.",
                    "She adjusted her scarf against the chill, feeling a strange sense of peace in the solitary walk home.",
                    "The wooden floorboards creaked gently with every step, carrying the weight of countless memories.",
                    "It was one of those rare, perfect evenings where nothing needed to be said, and everything was understood."
                ]
            };

            let amplifiedBody = story.body;
            const theme = story.category === "sci-fi" ? thematicSnippets["sci-fi"] : thematicSnippets["slice-of-life"];
            const targetParagraphs = Math.floor(Math.random() * 25) + 20;
            for (let i = 0; i < targetParagraphs; i++) {
                const sentenceCount = Math.floor(Math.random() * 3) + 3;
                let paragraph = "";
                for(let j = 0; j < sentenceCount; j++) {
                    paragraph += theme[Math.floor(Math.random() * theme.length)] + " ";
                }
                amplifiedBody += "\\n<p class=\\"mb-5 leading-[1.8] text-[#CCCCCC]\\">" + paragraph.trim() + "</p>";
                if (i > 0 && i % 8 === 0) {
                    amplifiedBody += "\\n<div class=\\"my-10 flex items-center justify-center gap-4 text-[#555555]\\"><span class=\\"w-16 h-[1px] bg-[#333333]\\"></span><i class=\\"fas fa-asterisk text-[10px] opacity-50\\"></i><i class=\\"fas fa-asterisk text-xs opacity-70\\"></i><i class=\\"fas fa-asterisk text-[10px] opacity-50\\"></i><span class=\\"w-16 h-[1px] bg-[#333333]\\"></span></div>";
                }
            }
            story.body = amplifiedBody;

            // DYNAMIC READ TIME CALCULATION
            const textOnly = amplifiedBody.replace(/<[^>]*>?/gm, "");
            const wordCount = textOnly.split(/\\s+/).length;
            const readTimeMinutes = Math.ceil(wordCount / 200);

            // Fill Data
            const badgeEl = document.getElementById("readerCategoryBadge");
            if(badgeEl) {
                badgeEl.textContent = story.badgeText || "Story";
                badgeEl.className = "px-3 py-1 rounded-full text-[10px] sm:text-xs font-bold uppercase tracking-widest border " + (story.badgeClass || "bg-gray-800 text-gray-300 border-gray-600");
            }
            
            const dateEl = document.getElementById("readerDate");
            if(dateEl) dateEl.textContent = story.date || "2026";
            
            const titleEl = document.getElementById("readerTitle");
            if(titleEl) titleEl.textContent = story.title;
            
            const subtitleEl = document.getElementById("readerSubtitle");
            if(subtitleEl) subtitleEl.textContent = story.subtitle || "";
            
            const epigraphEl = document.getElementById("readerEpigraph");
            if(epigraphEl) epigraphEl.textContent = "\\"" + (story.quote || "") + "\\"";
            
            if(readerBody) readerBody.innerHTML = story.body;

            // Load Saved Coffees
            const countEl = document.getElementById("readerCoffeeCount");
            if(countEl) {
                const savedCoffees = localStorage.getItem("coffee_" + storyId) || story.initialCoffees || 0;
                countEl.textContent = savedCoffees;
            }

            // Update URL Hash
            window.location.hash = "story-" + storyId;

            // Update Prev / Next state
            updateReaderNavButtons();

            // Open Modal (3D Open Animation)
            readerBackdrop.classList.remove("reader-backdrop-hidden");
            readerBackdrop.classList.add("reader-backdrop-active");
            
            readerModal.style.transform = "rotateY(-90deg) scale(0.8)";
            readerModal.classList.remove("reader-modal-hidden");
            readerModal.classList.add("reader-modal-active");
            
            requestAnimationFrame(() => {
                setTimeout(() => {
                    readerModal.style.transform = "rotateY(0deg) scale(1)";
                }, 50);
            });

            document.body.style.overflow = "hidden";

            // Reset scroll & progress
            readerScrollArea.scrollTop = 0;
            readerScrollArea.scrollLeft = 0;
            currentFlipPage = 1;
            
            setTimeout(() => {
                calculateTotalPages();
                updatePageIndicator();
                
                if (window.innerWidth >= 768 && totalFlipPages > 1) {
                    const inst = document.getElementById("swipeInstruction");
                    if(inst) inst.style.opacity = "1";
                    setTimeout(() => {
                        if(inst) inst.style.opacity = "0";
                    }, 3000);
                }
            }, 600);
        }

        `;
    
    html = html.substring(0, start) + replacement + html.substring(end);
    fs.writeFileSync("insights.html", html);
    console.log("Replaced openStoryReader successfully");
} else {
    console.log("Could not find boundaries");
}

