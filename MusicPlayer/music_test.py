import music
import unittest

class MusicTests(unittest.TestCase):
	
	def setUp(self):
		self.song = music.Song(
			"Yeah",
			"Usher",
			"OMG", 
			"380",
			10000)
		self.song_two = music.Song(
			"Sorry",
			"Akon",
			"WTF", 
			"280",
			15000)
		self.play_list = music.PlayList("PlayListOne")

	def test_song_init(self):
		self.assertEqual(self.song.title, 'Yeah')
		self.assertEqual(self.song.artist, 'Usher')
		self.assertEqual(self.song.album, 'OMG')
		self.assertEqual(self.song.length, '380')
		self.assertEqual(self.song.bitrate, 10000)
		self.assertEqual(self.song.rating, None)
	def test_rate(self):
		self.song.rate(3)
		self.assertEqual(self.song.rating, 3)
	def test_invalid_rate(self):
		self.song.rate(6)
		self.assertEqual(self.song.rating, None)


 	# PLAYLIST TESTS
	def test_play_list_init(self):
		self.assertEqual(self.play_list.name, 'PlayListOne')

	def test_add_song(self):
		self.play_list.add_song(self.song)
		self.assertIn(self.song, self.play_list.songs)

	def test_remove_song(self):
		self.play_list.add_song(self.song)
		self.play_list.add_song(self.song_two)
		self.play_list.remove_song(self.song.title)
		self.assertNotIn(self.song, self.play_list.songs)

	def test_total_length(self):
		self.play_list.add_song(self.song)
		self.play_list.add_song(self.song_two)
		length = self.play_list.total_length()
		self.assertEqual(length, "660")

	def test_remove_disrated(self):
		self.song.rate(3)
		self.song_two.rate(1)
		self.play_list.add_song(self.song)
		self.play_list.add_song(self.song_two)
		self.play_list.remove_disrated()
		self.assertNotIn(self.song_two, self.play_list.songs)

	def test_remove_bad_quality(self):
		self.play_list.add_song(self.song)
		self.play_list.add_song(self.song_two)
		self.play_list.remove_bad_quality()
		self.assertNotIn(self.song, self.play_list.songs)

	def test_show_artists(self):
		self.play_list.add_song(self.song)
		self.play_list.add_song(self.song_two)
		artist_list = self.play_list.show_artists()
		self.assertEqual(len(artist_list), 2)

	def test_str(self):
		self.play_list.add_song(self.song)	
		self.play_list.add_song(self.song_two)	
		self.assertEqual(self.play_list.str(), "Usher Yeah 6:20\n Akon Sorry 4:40\n")
	def test_save(self):
		self.play_list.add_song(self.song)	
		self.play_list.add_song(self.song_two)	
		self.play_list.save("json.txt")

if __name__ == '__main__':
	unittest.main()