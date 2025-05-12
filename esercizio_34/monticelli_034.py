import yt_dlp

# URL del video che vuoi scaricare
video_url = 'https://www.youtube.com/watch?v=x72_8aGtgII'

# Opzioni di download
ydl_opts = {
    'format': 'best',  # Scarica il miglior formato disponibile
    'outtmpl': '%(title)s.%(ext)s',  # Nome del file di output
}

# Funzione per scaricare il video
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])
