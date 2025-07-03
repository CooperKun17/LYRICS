const audio = document.getElementById("player");
const lyricsContainer = document.getElementById("lyrics");
const progressBar = document.getElementById("progress-bar");

const lyrics = [
  { time: 37.0, text: "Ask me why my heart's inside my throat" },
  { time: 43.0, text: "I've never been in love, I've been alone" },
  { time: 47.5, text: "Feel like I've been living life asleep" },
  { time: 51.8, text: "Love so strong it makes me feel so weak" },
  { time: 56.0, text: "Are you lonely? (Are you lonely?)" },
  { time: 58.5, text: "Our fingers dancing when they meet" },
  { time: 61.5, text: "You seem so lonely (Are you lonely?)" },
  { time: 64.5, text: "I'll be the only dream you seek" },
  { time: 68.0, text: "So if you're lonely, no need to show me" },
  { time: 71.5, text: "If you're lonely, come be lonely with me" },
  { time: 75.0, text: "Lonely (Are you lonely?)" },
  { time: 77.5, text: "Passion is crashing as we speak" },
  { time: 80.5, text: "You seem so lonely (Are you lonely?)" },
  { time: 83.5, text: "You're the ground my feet won't reach" },
  { time: 87.0, text: "So if you're lonely, darling, you're glowing" },
  { time: 90.5, text: "If you're lonely, come be lonely with me" },
  { time: 94.0, text: "Underneath the pale moonlight" },
  { time: 97.0, text: "Dreaming of a circus life" },
  { time: 100.0, text: "Carousels and Ferris heights" },
  { time: 103.0, text: "I'll be yours if you'll be mine" },
  { time: 106.0, text: "'Cause I'm lonely, I'm so lonely" },
  { time: 109.0, text: "If you hold me, I'll be your only" },
  { time: 112.0, text: "Are you lonely? (Are you lonely?)" },
  { time: 114.5, text: "Our fingers dancing when they meet" },
  { time: 117.5, text: "You seem so lonely (Are you lonely?)" },
  { time: 120.5, text: "I'll be the only dream you seek" },
  { time: 124.0, text: "So if you're lonely, no need to show me" },
  { time: 127.5, text: "If you're lonely, come be lonely with me" },
  { time: 131.0, text: "Are you lonely?" },
  { time: 133.5, text: "Passion is crashing as we speak" },
  { time: 136.5, text: "You seem so lonely" },
  { time: 139.5, text: "You're the ground my feet won't reach" },
  { time: 143.0, text: "So if you're lonely, darling, you're glowing" },
  { time: 146.5, text: "If you're lonely, come be lonely with me" }
];

let lastLine = "";

// 🔁 Actualizar letra y progreso mientras se reproduce
audio.ontimeupdate = () => {
  const currentTime = audio.currentTime;
  const duration = audio.duration || 1;

  // 📊 Barra de progreso
  const percent = (currentTime / duration) * 100;
  progressBar.style.width = percent + "%";

  // 🎵 Letra actual
  const index = lyrics.findLastIndex(line => currentTime >= line.time);
  if (index !== -1) {
    const currentLine = lyrics[index].text;
    const previousLine = lyrics[index - 1]?.text || "";

    if (currentLine !== lastLine) {
      lyricsContainer.innerHTML = `
        <div style="opacity: 0.4; font-size: 1em;">${previousLine}</div>
        <div class="highlight">${currentLine}</div>
      `;
      lastLine = currentLine;
    }
  }
};

// ▶️ Activar audio al hacer clic
document.getElementById("start").addEventListener("click", () => {
  audio.play().then(() => {
    document.getElementById("start").style.display = "none";
  }).catch(() => {
    alert("El navegador bloqueó la reproducción automática. Haz clic nuevamente.");
  });
});