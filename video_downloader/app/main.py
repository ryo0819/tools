import uvicorn
import re
from fastapi import FastAPI  # FastAPIを使うために必要
from pydantic import BaseModel  # リクエストbodyを定義するために必要
from yt_dlp import YoutubeDL

URL_PATTERN = re.compile(r'http.*')
ytdlp_opts = {"format": "mp4"}
app = FastAPI()


class get_yt(BaseModel):
    url: str


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/yt_download")
def download_yt_video(jsonbody: get_yt):
    try:
        download_link = jsonbody.url
        with YoutubeDL(ytdlp_opts) as ydl:
            if re.match(URL_PATTERN, download_link):
                ydl.download(download_link)
            else:
                raise Exception
    except Exception as e:
        print(e)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
