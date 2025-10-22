document.addEventListener("DOMContentLoaded", () => {
  const randomColorButton = document.getElementById("random-color-button");
  const body = document.body;

  function setRandomColor() {
    fetch("/api/random-color")
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        body.style.backgroundColor = data["random_color"];
      });
  }

  randomColorButton.addEventListener("click", setRandomColor);
});
