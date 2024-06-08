from pytube import YouTube
from difflib import get_close_matches
import os

def download_yt(link: str):
    yt = YouTube(link)
    stream_list = yt.streams
    res720p = stream_list.get_highest_resolution()
    res1080p = stream_list.filter(adaptive=True, file_extension='mp4', res="1080p").first()
    audio = stream_list.filter(only_audio=True).order_by("abr").first()
    if res1080p:
        res1080p.download(output_path = "Download/", filename = "video.mp4")
        audio.download(output_path = "Download/", filename = "audio.mp4")
        os.chdir("d:/Doccuments/VSCode/VideoDownloadBot/VideoThumbnailsMaker/FFmpeg/x64/")
        name = yt.title + ".mp4" #.replace(" ", "_")
        if not os.path.isfile("../../../Download/" + name):
            os.system(f"ffmpeg -i ../../../Download/audio.mp4 -i ../../../Download/video.mp4 -c copy ../../../Download/output.mp4")
            os.rename("../../../Download/output.mp4", f"../../../Download/{name}")
            os.chdir("d:/Doccuments/VSCode/VideoDownloadBot/")
            return f"./Download/{name}", "1080p"
        else:
            os.chdir("d:/Doccuments/VSCode/VideoDownloadBot/")
            return f"./Download/{name}", "Already download"
            
    else:
        res720p.download(output_path = "Download/", filename = f"{yt.title}.mp4")
        os.chdir("d:/Doccuments/VSCode/VideoDownloadBot/")
        return f"./Download/{yt.title}.mp4", "less1080p"


def makeThumbnail(Video_path: str):
    os.chdir("d:/Doccuments/VSCode/VideoDownloadBot/VideoThumbnailsMaker/")
    os.system(f'VideoThumbnailsMaker.exe "../{Video_path}" /silent')
    os.chdir("d:/Doccuments/VSCode/VideoDownloadBot/")
    return f"{Video_path}.jpg"

def download_video_PH(Video_URL, Video_name):
    os.chdir("d:/Doccuments/VSCode/VideoDownloadBot/PHDownloader")
    os.system(f'python phdler.py custom {Video_URL}')
    os.chdir("d:/Doccuments/VSCode/VideoDownloadBot/")

    closest = get_close_matches(Video_name, [i if i[-4:] == '.mp4' else "" for i in os.listdir("./Download/handpicked")])
    if not closest: 
        return -1
    Video_path = "Download/handpicked/" + closest[0]
    return Video_path