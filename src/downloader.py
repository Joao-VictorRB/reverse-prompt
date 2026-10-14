import yt_dlp
from pathlib import Path

def obter_pasta():

    pasta = Path.home() / "VideosTikTok"
    pasta.mkdir(exist_ok=True)
    return pasta

def downloader(url):

    pasta = obter_pasta()
    opcoes = {"outtmpl": str(pasta / "video.%(id)s.%(ext)s")}

    with yt_dlp.YoutubeDL(opcoes) as ydl:
        ydl.download([url])
