import base64
import jiosaavn
from pyDes import *


def format_song(data, lyrics):
    try:
        data['media_url'] = decrypt_url(data['encrypted_media_url'])
        if data['320kbps'] != "true":
            data['media_url'] = data['media_url'].replace(
                "_320.mp4", "_160.mp4")
        data['media_preview_url'] = data['media_url'].replace(
            "_320.mp4", "_96_p.mp4").replace("_160.mp4", "_96_p.mp4").replace("//aac.", "//preview.")
    except KeyError or TypeError:
        url = data['media_preview_url']
        url = url.replace("preview", "aac")
        if data['320kbps'] == "true":
            url = url.replace("_96_p.mp4", "_320.mp4")
        else:
            url = url.replace("_96_p.mp4", "_160.mp4")
        data['media_url'] = url

    data['song'] = format(data['song'])
    data['music'] = format(data['music'])
    data['singers'] = format(data['singers'])
    data['starring'] = format(data['starring'])
    data['album'] = format(data['album'])
    data["primary_artists"] = format(data["primary_artists"])
    data['image'] = data['image'].replace("150x150", "500x500")

    if lyrics:
        if data['has_lyrics'] == 'true':
            data['lyrics'] = jiosaavn.get_lyrics(data['id'])
        else:
            data['lyrics'] = None

    try:
        data['copyright_text'] = data['copyright_text'].replace("&copy;", "©")
    except KeyError:
        pass
    return data

def decrypt_url(url):
    des_cipher = des(b"38346591", ECB, b"\0\0\0\0\0\0\0\0",
                     pad=None, padmode=PAD_PKCS5)
    enc_url = base64.b64decode(url.strip())
    dec_url = des_cipher.decrypt(enc_url, padmode=PAD_PKCS5).decode('utf-8')
    dec_url = dec_url.replace("_96.mp4", "_320.mp4")
    return dec_url
