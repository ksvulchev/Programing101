import json

a = {"title": "Panda song" , "artist": "Pandio"}
print(a)
print(json.dumps(a))


b = [1 ,2 ,3]

a["masiva"] = b


print(json.dumps(a))


song1 = {"title": " Panda Song", "author": "Pandio"}
song2 = {"title": " Panda Song2", "author": "Pandio2"}

songs_arr = [song1, song2]

playlist = {"name": "My Playlist", "songs": songs_arr}

print(json.dumps(playlist, indent=4))

			#song["title"] = i.title
			#song["artist"] = i.artist

			#song["album"] = i.album
			#song["length"] = self.to_minutes(i.length)
			#song["bitrate"] = i.bitrate