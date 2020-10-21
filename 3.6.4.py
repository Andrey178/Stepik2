import requests
import json
import time
from pprint import pprint

token = "eyJhbGciOiJIUzI1NiJ9.eyJyb2xlcyI6ImFydHN5Iiwic3ViamVjdF9hcHBsaWNhdGlvbiI6IjVkNDA5OTZlNmU2MDQ5MDAwNzQ5MGZhMiIsImV4cCI6MTYwMzQxMDIyMywiaWF0IjoxNjAyODA1NDIzLCJhdWQiOiI1ZDQwOTk2ZTZlNjA0OTAwMDc0OTBmYTIiLCJpc3MiOiJHcmF2aXR5IiwianRpIjoiNWY4OGRlYWY4YmVlYmYwMDBkODExMWJlIn0.82THGzqzr0rX9upNTU3Ur1ERioWz0NE5wdiI9sHdkiM"
headers = {"X-Xapp-Token" : token}

list_artists = []
artist_info = {}

with open(r"D:\Programming\dataset_24476_4.txt") as inf:
    for line in inf:
        list_artists.append(line.rstrip())
#print(*list_artists)

for _ in list_artists:
    r = requests.get(f"https://api.artsy.net/api/artists/{_}", headers=headers)
    j = r.json()
    artist_info[j['sortable_name']] = j['birthday']
    time.sleep(0.2)

#print(artist_info)
with open(r"D:\Programming\fileout.txt", "w", encoding='utf-8') as outf:
    for _ in sorted(artist_info.items(), key=lambda x: (x[1], x[0])):
        print(_[0])
        outf.write(f"{_[0]}\n")

try:
#    pprint(j)
    pass
except TypeError:
    print("ops")
