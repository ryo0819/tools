import pyautogui as pag

ad_png_path = "ad1.png"

# 同時押しのhotkeyメソッドでは、ウィンドウの切り替えができなかったので人間の動きを再現
pag.keyDown("command")
pag.press("tab")
pag.keyUp("command")

while True:
    try:
        if pag.locateOnScreen(ad_png_path, confidence=0.8) is None:
            continue
        else:
            # 広告位置にカーソル移動&スキップ
            icon_loc = pag.locateOnScreen(ad_png_path, confidence=0.8)
            x, y = pag.center(icon_loc)
            # x,yともに2で割らないと正しい座標をクリックできない(mac環境だけらしい)
            pag.click(x / 2, y / 2)
    except KeyboardInterrupt:
        exit("強制終了しました。(正常)")
    except:
        pass
