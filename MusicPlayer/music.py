
import json

class Song:

	MAX_RATING = 5
	MIN_RATING = 1

	def __init__(self, title, artist, album, length, bitrate):
		self.title = title
		self.artist = artist
		self.album = album
		self.length = length
		self.bitrate = bitrate
		self.rating = None

	def rate(self, rating):
		if rating > Song.MAX_RATING or rating < Song.MIN_RATING:
			print ("Invalid rating choose between {} and {}".format(Song.MIN_RATING,Song.MAX_RATING))
			#raise ValueError("Invalid rating choose between {} and {}".format(Song.MIN_RATING,Song.MAX_RATING))
		else:	
			self.rating = rating
	def __repr__(self):
		return str(self.__dict__)

class PlayList:

	MIN_RATING = 3
	MIN_BITRATE = 11000
	SECONDS = 60

	def __init__(self, name):
		self.name = name
		self.songs = []

	def add_song(self, song):
		self.songs.append(song)

	def remove_song(self, song_title):
		for i,e in enumerate(self.songs):
			if self.songs[i].title == song_title:
				self.songs.pop(i)

	def total_length(self):
		length = 0
		for i in self.songs:
			song_length = int(i.length)
			length += song_length
		length = str(length)
		return length

	def remove_disrated(self):
		songs_to_remove = []
		for i in self.songs:
			if i.rating < PlayList.MIN_RATING:
				songs_to_remove.append(i)
		for y in songs_to_remove:
			self.songs.remove(y)

		print(self.songs[0].title)

	def remove_bad_quality(self):
		songs_to_remove = []
		for i in self.songs:
			if i.bitrate < PlayList.MIN_BITRATE:
				songs_to_remove.append(i)
		for y in songs_to_remove:
			self.songs.remove(y)

		print(self.songs[0].title)

	def show_artists(self):
		artists = []
		for i in self.songs:
			artists.append(i.artist)
		return set(artists)

	def to_minutes(self, secs):
		mins = 0
		secs = int(secs)
		while secs > PlayList.SECONDS:
			secs -= PlayList.SECONDS
			mins += 1

		return "{}:{}".format(mins,secs)


	def str(self):
		to_print = []
		for i in self.songs:
			to_print.append("{} {} {}\n".format(i.artist, i.title, self.to_minutes(i.length)))

		return " ".join(to_print)

	def save(self, file_name):
		songs = []
		for i in self.songs:
			songs.append(i.__dict__)
		data = {"name":"Play list", "songs":songs}	
		file = open(file_name, "w")
		file.write(json.dumps(data,  indent=4))
		file.close()