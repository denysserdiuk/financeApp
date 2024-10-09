// Show modal
function openModal() {
  document.getElementById("modal").style.display = "block";
}

// Close modal
function closeModal() {
  document.getElementById("modal").style.display = "none";
}

// Add event listeners to buttons
document.querySelector('.header__menu-item a[href="register"]').addEventListener('click', function (event) {
  event.preventDefault();
  openModal();
});

// Add this to close the modal when clicking outside of it
window.onclick = function(event) {
  const modal = document.getElementById("modal");
  if (event.target === modal) {
    closeModal();
  }
};

document
  .getElementById("registrationForm")
  .addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent the default form submission

    // Collect form data
      const formData = {
      username: document.getElementById("username").value,
      email: document.getElementById("email").value,
      password: document.getElementById("password").value,
    };

    // Send POST request to the backend
    fetch("/add_user", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(formData),
    })
      .then((response) => {
        if (response.ok) {
          window.location.href = "/successful_registration";
        } else {
          alert("Error registering user. Please try again.");
        }
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  });
