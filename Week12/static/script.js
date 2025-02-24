document.getElementById("aboutBtn").addEventListener("click", () => {
  window.location.href = "/about/Isabel/6";
});

document.getElementById("alertBtn").addEventListener("click", () => {
  alert("Hello from JavaScript!");
});

document.getElementById("fileInput").addEventListener("change", (event) => {
  const file = event.target.files[0];
  const reader = new FileReader();

  reader.onload = function (e) {
    document.getElementById("preview").src = e.target.result;
  };
  reader.readAsText(file);
});
