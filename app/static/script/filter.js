function applyFilters() {
    // Fetch selected values from the filter dropdowns and checkboxes
    const selectedGenre = document.getElementById("genre").value;
    const selectedRating = document.getElementById("rating").value;
    const selectedLanguage = document.getElementById("language").value;
    const recentlyUpdated = document.getElementById("recently-updated").checked;
  
    // Perform filtering logic based on selected values
    // You can replace this with your actual filtering mechanism
  
    // Example: Fetch anime based on the selected filters
    const filteredAnime = getFilteredAnime(selectedGenre, selectedRating, selectedLanguage, recentlyUpdated);
  
    // Display the filtered anime
    displayAnime(filteredAnime);
  }
  
  function getFilteredAnime(genre, rating, language, recentlyUpdated) {
    // Replace this with your actual logic to fetch anime based on filters
    // Example: Fetch anime from an API based on selected genre, rating, language, and recentlyUpdated
    // const apiUrl = `https://example.com/anime?genre=${genre}&rating=${rating}&language=${language}&recentlyUpdated=${recentlyUpdated}`;
    // const response = await fetch(apiUrl);
    // const anime = await response.json();
    // return anime;
  
    // For now, returning dummy data
    return [
      { title: "Anime 1", genre: "Action", rating: 4, language: "Japanese", updated: "2023-01-01" },
      { title: "Anime 2", genre: "Comedy", rating: 3, language: "English", updated: "2023-02-15" },
      // Add more anime objects as needed
    ];
  }
  
  function displayAnime(anime) {
    const animeResultsContainer = document.getElementById("anime-results");
    // Clear previous results
    animeResultsContainer.innerHTML = "";
  
    // Display each anime in a card
    anime.forEach(anime => {
      const animeCard = document.createElement("div");
      animeCard.className = "anime-card";
      animeCard.textContent = `${anime.title} - Genre: ${anime.genre}, Rating: ${anime.rating}, Language: ${anime.language}, Updated: ${anime.updated}`;
      animeResultsContainer.appendChild(animeCard);
    });
  }