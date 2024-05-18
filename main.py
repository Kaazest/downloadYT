from pytube import YouTube

# URL del video de YouTube que deseas descargar
video_url = input("Introduzca la url del video de Youtube")

# Crear un objeto YouTube
yt = YouTube(video_url)

# Seleccionar la mejor calidad disponible
video = yt.streams.get_highest_resolution()

# Descargar el video
video.download('home/Downloads')