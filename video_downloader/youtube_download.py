from yt_dlp import YoutubeDL
import re

URL_PATTERN = re.compile(r'http.*')
ytdlp_opts = {"format": "mp4"}
url = input("ダウンロードしたい動画のURLを入力してください。：")

try:
    with YoutubeDL(ytdlp_opts) as ydl:
        if re.match(URL_PATTERN, url):
            res = ydl.download(url)
        else:
            raise Exception
except Exception as e:
    print(e)
