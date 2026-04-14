const words = ['Welcome', 'To', 'FloraFix'];
const typeSpeed = 150;
const eraseSpeed = 100;
const delayBetweenWords = 1000;

let wordIndex = 0;
let charIndex = 0;
let isDeleting = false;

const typewriter = document.getElementById('typewriter');

function type() {
  const currentWord = words[wordIndex];
  if (isDeleting) {
    typewriter.textContent = currentWord.substring(0, charIndex--);
    if (charIndex < 0) {
      isDeleting = false;
      wordIndex = (wordIndex + 1) % words.length;
      setTimeout(type, 300);
    } else {
      setTimeout(type, eraseSpeed);
    }
  } else {
    typewriter.textContent = currentWord.substring(0, charIndex++);
    if (charIndex > currentWord.length) {
      isDeleting = true;
      setTimeout(type, delayBetweenWords);
    } else {
      setTimeout(type, typeSpeed);
    }
  }
}

document.addEventListener('DOMContentLoaded', () => {
  type();
});