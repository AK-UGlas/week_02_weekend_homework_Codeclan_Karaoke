import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.rock_song = Song("Thunderstruck", "AC/DC", 292, 1990, "Rock")
