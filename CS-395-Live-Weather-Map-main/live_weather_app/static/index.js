async function initMap() {
  const { Map } = await google.maps.importLibrary("maps");

  const map = new Map(document.getElementById("map"), {
    center: { lat: 38, lng: -77 },
    zoom: 8,
  });
}

document.addEventListener("DOMContentLoaded", () => {
  initMap();
});