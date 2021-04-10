import unittest
from src.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.rock = Song("Thunderstruck", "AC/DC", 292, 1990, "Rock")

    def test_song_has_name(self):
        self.assertEqual("Thunderstruck", self.rock.name)

    def test_song_has_artist(self):
        self.assertEqual("AC/DC", self.rock.artist)

    def test_song_has_duration(self):
        self.assertEqual(292, self.rock.duration)

    def test_song_has_release_date(self):
        self.assertEqual(1990, self.rock.year)

    def test_song_has_genre(self):
        self.assertEqual("Rock", self.rock.genre)

    