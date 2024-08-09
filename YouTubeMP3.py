import yt_dlp
import os


# Note: Script won't work unless you have ffmpeg and ffprobe installed on your system

 
def YouTubeMP3():
    input_url = input("Enter YouTube Link: ")
    dest = "~/Desktop/Music/Samples"
    
    # Ensure the destination directory exists
    os.makedirs(dest, exist_ok=True)
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(dest, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '256'
        }],
    }   
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([input_url])
    
    print("Script Executed Successfully!")
    return 


YouTubeMP3()




    