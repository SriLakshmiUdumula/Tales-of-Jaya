document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".like-button").forEach(button => {
        button.addEventListener("click", function () {
            const storyId = this.getAttribute("data-story-id");
            const likeCountSpan = document.getElementById(`like-count-${storyId}`);

            fetch(`/like/${storyId}/`, {
                method: "GET",
                headers: { "X-Requested-With": "XMLHttpRequest" }
            })
            .then(response => response.json())
            .then(data => {
                if (data.likes !== undefined) {
                    likeCountSpan.textContent = data.likes; // Update like count
                } else {
                    console.error("Invalid response:", data);
                }
            })
            .catch(error => console.error("Error:", error));
        });
    });
});
