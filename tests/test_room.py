import unittest
from src.room import Room
from src.song import Song
from src.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.playlist = [
                    Song("Thunderstruck", "AC/DC", 292, 1990, "rock"),
                    Song("We will rock you)", "Queen", 122, 1977, "classic rock"), 
                    Song("I'm gonna be (500 miles)", "The Proclaimers", 217, 1988, "folk rock"),
                    Song("It's raining men", "The Weather Girls", (60 * 5) + 24, 1982, "post-disco"),
                    Song("Livin' on a prayer", "Bon Jovi", (60 * 4) + 11, 1986, "classic rock"),
                    Song("Thunderstruck", "AC/DC", 292, 1990, "rock")
        ]

        self.large = Room("Party room", 15)
        self.medium = Room("Beats room", 10)
        self.small = Room("Chillout room", 5)

    # Test room attributes
    def test_room_has_name(self):
        self.assertEqual("Party room", self.large.name)

    def test_room_has_capacity(self):
        self.assertEqual(15, self.large.capacity)





                
                                

