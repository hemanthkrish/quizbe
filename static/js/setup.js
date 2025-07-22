document.addEventListener("DOMContentLoaded", () => {
    const topicDropdown = document.getElementById("topicDropdown");
    const slabDropdown = document.getElementById("slabDropdown");
    const output = document.getElementById("output");

    // --- Function to update the slab dropdown based on the selected topic ---
    function updateSlabDropdown() {
        // Get the selected topic's configuration from its data attributes
        const selectedOption = topicDropdown.options[topicDropdown.selectedIndex];
        const totalQuestions = parseInt(selectedOption.getAttribute('data-total-questions'), 10);
        const slabSize = parseInt(selectedOption.getAttribute('data-slab-size'), 10);
        
        // Clear previous slab options
        slabDropdown.innerHTML = '';

        if (isNaN(totalQuestions) || totalQuestions === 0) {
            const option = document.createElement("option");
            option.textContent = "No questions available";
            slabDropdown.appendChild(option);
            slabDropdown.disabled = true;
            return;
        }

        slabDropdown.disabled = false;
        const totalSlabs = Math.ceil(totalQuestions / slabSize);

        // Generate new slab options
        for (let i = 0; i < totalSlabs; i++) {
            const start = i * slabSize + 1;
            const end = Math.min((i + 1) * slabSize, totalQuestions);
            const option = document.createElement("option");
            option.value = `${start - 1},${end}`; // Use 0-based index for the API
            option.textContent = `Questions ${start} - ${end}`;
            slabDropdown.appendChild(option);
        }

        // Trigger a change event on the slab dropdown to fetch the first slab
        slabDropdown.dispatchEvent(new Event("change"));
    }

    // --- Function to handle changes in the slab selection ---
    function handleSlabChange() {
        const [start, end] = slabDropdown.value.split(",").map(Number);
        const topic = topicDropdown.value;
        
        output.textContent = `Selected: ${start + 1} to ${end}`;

        // Call the global function in script.js to fetch the questions
        if (typeof window.fetchAndUpdateQuestions === "function") {
            window.fetchAndUpdateQuestions(topic, start, end);
        }
    }

    // --- Event Listeners ---
    topicDropdown.addEventListener("change", updateSlabDropdown);
    slabDropdown.addEventListener("change", handleSlabChange);

    // --- Initial setup ---
    // Populate the slab dropdown for the default selected topic on page load
    updateSlabDropdown();
});
