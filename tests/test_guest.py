import unittest
from src.guest import Guest
from src.song import Song

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.thunderstruck = Song("Thunderstruck", "AC/DC", 292, 1990, "Rock")
        self.guest = Guest("Dave", 50, self.thunderstruck)
        
# testing Guest attributes
    def test_guest_has_name(self):
        self.assertEqual("Dave", self.guest.name)

    def test_guest_has_favourite_song(self):
        self.assertEqual(self.thunderstruck, self.guest.favourite_song)

    def test_guest_has_wallet(self):
        self.assertEqual(50, self.guest.wallet)

# test methods
    def test_guest_pays_for_item(self):
        self.guest.pay(5)
        self.assertEqual(45, self.guest.wallet)

    def test_favourite_song_is_on_playlist(self):
        playlist = [self.thunderstruck]
        self.assertEqual("YAAAASSSS!!!!, they've got Thunderstruck!", self.guest.woop_obnoxiously(playlist))

    def test_guest_can_afford_item(self):
        self.assertTrue(self.guest.can_afford_item(10))

    def test_guest_cannot_afford_item(self):
        self.assertFalse(self.guest.can_afford_item(50.01))
