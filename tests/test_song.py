import unittest
from src.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.rock = Song("Thunderstruck", "AC/DC", 292, 1990, "Rock")

    def test_song_has_name(self):
        self.assertEqual("Thunderstruck", self.rock.name)

    