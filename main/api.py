import urllib, json

def song_week():
    url = "http://zardify.tk/api_song.php"
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    return data

def posts(category):
    url = ("http://zardify.tk/api_posts.php?type=%s" % category)
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    return data