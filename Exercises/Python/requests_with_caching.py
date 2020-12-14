import requests_with_caching
import json

def get_movies_from_tastedive(str):
    query = {"q": str, "type": "movies", "limit": 5}
    req = requests_with_caching.get("https://tastedive.com/api/similar", params=query)
    data = json.loads(req.text)
    return data

def extract_movie_titles(dat):
    data = []
    for i in dat["Similar"]["Results"]:
        data.append(i["Name"])
    return data

def get_related_titles(lst):
    data = []
    call = ""
    for i in lst:
        calls = extract_movie_titles(get_movies_from_tastedive(i))
        for x in calls:
            if x not in data:
                data.append(x)
            else:
                continue
    return data


def get_movie_data(str):
    query = {"t": str, "r": "json"}
    req = requests_with_caching.get("http://www.omdbapi.com/", params=query)
    data = json.loads(req.text)
    return data

def get_movie_rating(dat):
    final = 0
    for i in dat["Ratings"]:
        if 'Rotten Tomatoes' in i.values():
            val = i["Value"]
            slp = val.split("%")
            final = final + int(slp[0])
    return final