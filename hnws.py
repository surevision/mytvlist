import requests
import time
import hashlib

header_text = """#EXTM3U
#EXT-X-APP APTV
#EXT-X-APTV-TYPE remote
#EXT-X-SUB-URL https://192.168.0.108/hnws.txt

"""
if __name__=="__main__":
    timestamp = str(round(time.time()))
    data = f"6ca114a836ac7d73{timestamp}"
    sign = hashlib.sha256(data.encode('utf-8')).hexdigest()

    url = "https://pubmod.hntv.tv/program/getAuth/live/class/program/11/"
    headers = {
        "sign": sign,
        "timestamp": timestamp,
    }
    response = requests.get(url, headers=headers)
    
    print(header_text)
    with open("hnws.txt", "w") as f:
        f.write(header_text)
        for item in response.json():
            name = item.get("name")
            video = item.get("video_streams")[0]
            rem = f'#EXTINF:-1 tvg-id="{name}" tvg-name="{name}" tvg-logo="" group-title="{name}",{name}'
            info = f'{video}'
            print(rem)
            print(info)
            f.write(f"{rem}\n")
            f.write(f"{info}\n")

    