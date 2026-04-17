import yt_dlp
import os

def download_mp3():
    url = input("Paste YouTube URL here: ")

    # I use 192kbps because the iPhone 5C hardware and older speakers won't benefit from anything higher
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': '%(title)s.%(ext)s',
        'ffmpeg_location': './ffmpeg.exe' 
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("\nDone. Check folder for the mp3.")
    except Exception as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    download_mp3()