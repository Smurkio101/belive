document.addEventListener("DOMContentLoaded", function () {
  const menuBtn = document.getElementById("menuBtn");
  const menu = document.getElementById("menu");

  menuBtn.addEventListener("click", function () {
    // Toggle the menu's visibility
    menu.style.transition = "opacity 0.3s ease-in-out"; // Smooth transition effect
    menu.style.opacity = menu.style.opacity === "1" ? "0" : "1";

    // Close the menu after a short delay
    setTimeout(function () {
      menu.style.display = menu.style.display === "block" ? "none" : "block";
    }, 300); // Adjust the delay to match the transition duration
  });

  // Close the menu directly after clicking a menu link
  const menuLinks = document.querySelectorAll(".menu_link");
  menuLinks.forEach(function (link) {
    link.addEventListener("click", function () {
      menu.style.transition = "none"; // Disable transition for immediate closing
      menu.style.display = "none";
    });
  });

  // Close the menu if a click occurs outside the menu
  document.addEventListener("click", function (event) {
    if (!menu.contains(event.target) && event.target !== menuBtn) {
      menu.style.transition = "none"; // Disable transition for immediate closing
      menu.style.display = "none";
    }
  });
});