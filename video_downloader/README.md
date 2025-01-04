# video_downloader

## 概要
- FastAPIを使用して、URLを受け付けるAPIを作成
- URLをGETメソッドに引数で渡すことで、対象の動画をファイルとしてダウンロードする
- エンドポイントは`/yt_download`でリクエストボディにjson形式で動画のリンクを指定する

## 使用方法
- (docker環境構築済みでない場合)
    - docker-composeできる準備を行う(MacユーザーなのでMacだけ書きますmm)
        - brewでインストールします
        - https://formulae.brew.sh/formula/docker-compose
1. コンテナ起動
    ```
    docker-compose up --build -d
    ```
1. localhostに向けてcurlを実行する
    ```
    # リクエストボディにダウンロードしたい動画のリンクを指定してリクエスト
    curl -vX "GET" "http://localhost:8080/yt_download" -d "{\"url\": \"https://www.example.com\"}" -H 'Content-Type: application/json'
    ```
1. appディレクトリ配下にリクエストした動画が保存される
