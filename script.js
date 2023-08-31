// script.js

document.addEventListener("DOMContentLoaded", function () {
  const albumTiles = document.querySelectorAll(".album-tile");
  const closeBtn = document.querySelector(".close-btn");

  const albumImagesMap = {




    // Add a default preview image for files without a preview
    "__default__": "video.jpg"
  };

  albumTiles.forEach(function (tile) {
    tile.addEventListener("click", function () {
      const albumTitle = tile.querySelector(".album-title").textContent;
      const albumImages = albumImagesMap[albumTitle];

      if (albumImages) {
        const imageLinks = albumImages.map((image) => {
          if (image.endsWith(".MOV")) {
            // Replace MOV files with default image
            return `<a href="${image}" target="_blank"><img src="${albumImagesMap['__default__']}" alt="${albumTitle}" class="album-image"></a>`;
          } else {
            return `<a href="${image}" target="_blank"><img src="${image}" alt="${albumTitle}" class="album-image"></a>`;
          }
        }).join("");

        const imageGrid = document.querySelector(".image-grid");
        imageGrid.innerHTML = imageLinks;

        const albumModal = document.querySelector(".album-modal");
        albumModal.style.display = "block";
      }
    });
  });

  closeBtn.addEventListener("click", function () {
    const albumModal = document.querySelector(".album-modal");
    albumModal.style.display = "none";

    const imageGrid = document.querySelector(".image-grid");
    imageGrid.innerHTML = "";
  });

  window.addEventListener("click", function (event) {
    const albumModal = document.querySelector(".album-modal");
    if (event.target === albumModal) {
      albumModal.style.display = "none";

      const imageGrid = document.querySelector(".image-grid");
      imageGrid.innerHTML = "";
    }
  });
});
