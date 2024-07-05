import requests
import api
import helper
import json
from traceback import print_exc


def search_for_song(query, lyrics, songdata, page):
    if query.startswith('http') and 'saavn.com' in query:
        id = get_song_id(query)
        return get_song(id, lyrics)
    #search_base_url = endpoints.search_base_url+query
    search_base_url = api.long_base_url+"&p="+page+"&q="+query
    response = requests.get(
        search_base_url).text.encode().decode('unicode-escape')
    response = json.loads(response)
    #song_response = response['songs']['data']
    song_response = response['results']
    if not songdata:
        return song_response
    songs = []
    for song in song_response:
        id = song['id']
        song_data = get_song(id, lyrics)
        if song_data:
            songs.append(song_data)
        
    return songs


def get_song(id, lyrics):
    try:
        song_details_base_url = api.song_details_base_url+id
        song_response = requests.get(
            song_details_base_url).text.encode().decode('unicode-escape')
        song_response = json.loads(song_response)
        song_data = helper.format_song(song_response[id], lyrics)
        if song_data:
            return song_data
    except:
        return None


def get_song_id(url):
    res = requests.get(url, data=[('bitrate', '320')])
    try:
        return(res.text.split('"pid":"'))[1].split('","')[0]
    except IndexError:
        return res.text.split('"song":{"type":"')[1].split('","image":')[0].split('"id":"')[-1]



def get_lyrics(id):
    url = api.lyrics_base_url+id
    lyrics_json = requests.get(url).text
    lyrics_text = json.loads(lyrics_json)
    return lyrics_text['lyrics']
