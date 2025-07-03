import time
import os
import sys
import subprocess
from threading import Thread

# 🎶 Ruta al archivo MP3
AUDIO_PATH = r"D:\Users\Usuario\Downloads\LYRICS\Coyote.mp3"

# 🛠️ Verifica e instala playsound automáticamente
try:
    from playsound import playsound
except ImportError:
    print("🔄 Instalando 'playsound' automáticamente...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "playsound==1.2.2"])
    from playsound import playsound

# 🎵 Letras con timestamps ajustados (en segundos desde el inicio)
timestamped_lyrics = [
  { "time": 37.0, "text": "Ask me why my heart's inside my throat" },
  { "time": 43.0, "text": "I've never been in love, I've been alone" },
  { "time": 47.5, "text": "Feel like I've been living life asleep" },
  { "time": 51.8, "text": "Love so strong it makes me feel so weak" },
  { "time": 56.0, "text": "Are you lonely? (Are you lonely?)" },
  { "time": 58.5, "text": "Our fingers dancing when they meet" },
  { "time": 61.5, "text": "You seem so lonely (Are you lonely?)" },
  { "time": 64.5, "text": "I'll be the only dream you seek" },
  { "time": 68.0, "text": "So if you're lonely, no need to show me" },
  { "time": 71.5, "text": "If you're lonely, come be lonely with me" },
  { "time": 75.0, "text": "Lonely (Are you lonely?)" },
  { "time": 77.5, "text": "Passion is crashing as we speak" },
  { "time": 80.5, "text": "You seem so lonely (Are you lonely?)" },
  { "time": 83.5, "text": "You're the ground my feet won't reach" },
  { "time": 87.0, "text": "So if you're lonely, darling, you're glowing" },
  { "time": 90.5, "text": "If you're lonely, come be lonely with me" },
  { "time": 94.0, "text": "Underneath the pale moonlight" },
  { "time": 97.0, "text": "Dreaming of a circus life" },
  { "time": 100.0, "text": "Carousels and Ferris heights" },
  { "time": 103.0, "text": "I'll be yours if you'll be mine" },
  { "time": 106.0, "text": "'Cause I'm lonely, I'm so lonely" },
  { "time": 109.0, "text": "If you hold me, I'll be your only" },
  { "time": 112.0, "text": "Are you lonely? (Are you lonely?)" },
  { "time": 114.5, "text": "Our fingers dancing when they meet" },
  { "time": 117.5, "text": "You seem so lonely (Are you lonely?)" },
  { "time": 120.5, "text": "I'll be the only dream you seek" },
  { "time": 124.0, "text": "So if you're lonely, no need to show me" },
  { "time": 127.5, "text": "If you're lonely, come be lonely with me" },
  { "time": 131.0, "text": "Are you lonely?" },
  { "time": 133.5, "text": "Passion is crashing as we speak" },
  { "time": 136.5, "text": "You seem so lonely" },
  { "time": 139.5, "text": "You're the ground my feet won't reach" },
  { "time": 143.0, "text": "So if you're lonely, darling, you're glowing" },
  { "time": 146.5, "text": "If you're lonely, come be lonely with me" }
]

# 🎨 Colores para variar visualmente
colors = ["\033[91m", "\033[92m", "\033[93m", "\033[94m", "\033[95m", "\033[96m", "\033[97m"]
reset_color = "\033[0m"

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def play_song():
    print("🎧 Reproduciendo:", AUDIO_PATH)
    playsound(AUDIO_PATH)

def show_lyrics():
    clear_terminal()
    start_time = time.time() + 1.2  # 🕒 retardo inicial para mejorar sincronización
    for i, lyric in enumerate(timestamped_lyrics):
        t = lyric["time"]
        line = lyric["text"]
        while time.time() < start_time + t:
            time.sleep(0.01)
        color = colors[i % len(colors)]
        for char in line:
            sys.stdout.write(color + char)
            sys.stdout.flush()
            time.sleep(0.06)  # ✨ tipo de aparición más lenta
        print(reset_color)

# 🚀 Ejecutar reproducción y letra sincronizada en paralelo
Thread(target=play_song).start()
show_lyrics()
