// // Preview uploaded image
// const plantInput = document.getElementById("plantInput");
// const previewImg = document.getElementById("previewImg");
// const diagnoseBtn = document.getElementById("diagnoseBtn");
// const resultText = document.getElementById("resultText");

// plantInput.addEventListener("change", function() {
//   const file = this.files[0];
//   if (file) {
//     const reader = new FileReader();
//     reader.onload = function(e) {
//       previewImg.src = e.target.result;
//       previewImg.style.display = "block";
//     };
//     reader.readAsDataURL(file);
//   }
// });

// // Fake diagnosis with animated popup effect
// diagnoseBtn.addEventListener("click", () => {
//   if (previewImg.src === "") {
//     resultText.textContent = "⚠️ Please upload an image first.";
//     return;
//   }

//   // Random diagnosis result
//   const diagnoses = [
//     "✅ Your plant looks healthy! Keep it hydrated 🌿",
//     "⚠️ Yellow spots detected - possible nutrient deficiency 🌱",
//     "🛑 Signs of fungal infection detected, take action soon 🍂",
//     "💧 Plant may be underwatered, increase watering frequency."
//   ];
  
//   const randomResult = diagnoses[Math.floor(Math.random() * diagnoses.length)];
  
//   resultText.textContent = randomResult;
//   resultText.classList.add("pop-result");

//   // Remove animation after it plays
//   setTimeout(() => {
//     resultText.classList.remove("pop-result");
//   }, 800);
// });

// // Popup animation
// const style = document.createElement("style");
// style.innerHTML = `
// .pop-result {
//   animation: pop 0.8s ease;
// }
// @keyframes pop {
//   0% { transform: scale(0.7); opacity: 0; }
//   50% { transform: scale(1.2); opacity: 1; }
//   100% { transform: scale(1); }
// }`;
// document.head.appendChild(style);
// Preview uploaded image
const plantInput = document.getElementById("plantInput");
const previewImg = document.getElementById("previewImg");
const diagnoseBtn = document.getElementById("diagnoseBtn");
const resultText = document.getElementById("resultText");

// 🛒 Shopping button (below result)
let shopBtn = document.createElement("a");
shopBtn.href = "https://www.iffcobazar.in/en/organic-fertilizers";
shopBtn.target = "_blank";
shopBtn.textContent = "🛒 Buy Fertilizers & Pesticides";
shopBtn.className =
  "mt-4 inline-block px-4 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700 transition hidden"; // hidden initially

// Insert shopping button after result text
if (resultText && resultText.parentNode) {
  resultText.parentNode.appendChild(shopBtn);
}

plantInput.addEventListener("change", function () {
  const file = this.files[0];
  if (file) {
    const reader = new FileReader();
    reader.onload = function (e) {
      previewImg.src = e.target.result;
      previewImg.style.display = "block";
    };
    reader.readAsDataURL(file);
  }
});

// Fake diagnosis with animated popup effect
diagnoseBtn.addEventListener("click", () => {
  if (previewImg.src === "") {
    resultText.textContent = "⚠️ Please upload an image first.";
    shopBtn.classList.add("hidden"); // hide shop button
    return;
  }

  // Random diagnosis result
  const diagnoses = [
    "✅ Your plant looks healthy! Keep it hydrated 🌿",
    "⚠️ Yellow spots detected - possible nutrient deficiency 🌱",
    "🛑 Signs of fungal infection detected, take action soon 🍂",
    "💧 Plant may be underwatered, increase watering frequency.",
  ];

  const randomResult = diagnoses[Math.floor(Math.random() * diagnoses.length)];

  resultText.textContent = randomResult;
  resultText.classList.add("pop-result");

  // Show shop button whenever a result is shown
  shopBtn.classList.remove("hidden");

  // Remove animation after it plays
  setTimeout(() => {
    resultText.classList.remove("pop-result");
  }, 800);
});

// Popup animation
const style = document.createElement("style");
style.innerHTML = `
.pop-result {
  animation: pop 0.8s ease;
}
@keyframes pop {
  0% { transform: scale(0.7); opacity: 0; }
  50% { transform: scale(1.2); opacity: 1; }
  100% { transform: scale(1); }
}`;
document.head.appendChild(style);
