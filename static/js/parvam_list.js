document.addEventListener("DOMContentLoaded", function() {
    // Get the modal elements
    var modal = document.getElementById("imageModal");
    var modalTitle = document.getElementById("modalTitle");
    var modalContent = document.getElementById("modalContent");
    var closeButton = modal.querySelector(".close");

    // Function to open the modal with image title and content
    document.querySelectorAll('.scrolling-images img').forEach(image => {
        image.addEventListener("click", function() {
            modal.style.display = "block";
            modalTitle.innerText = this.getAttribute("data-title");
            modalContent.innerText = this.getAttribute("data-content");
        });
    });

    // Close modal when the close button is clicked
    closeButton.onclick = function() {
        modal.style.display = "none";
    };

    // Close modal when clicking outside the modal content
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    };
});

