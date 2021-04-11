import unittest
from src.guest import Guest
from src.song import Song

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.thunderstruck = Song("Thunderstruck", "AC/DC", 292, 1990, "Rock")
        self.guest = Guest("Dave", self.thunderstruck)

# testing Guest attributes
    def test_guest_has_name(self):
        self.assertEqual("Dave", self.guest.name)

    def test_guest_has_favourite_song(self):
        self.assertEqual(self.thunderstruck, self.guest.favourite_song)


