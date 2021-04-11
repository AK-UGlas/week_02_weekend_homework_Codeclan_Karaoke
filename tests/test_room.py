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
            Song("Livin' on a prayer", "Bon Jovi", (60 * 4) + 11, 1986, "classic rock")
        ]

        self.large = Room("Party room", 15)
        self.medium = Room("Beats room", 10)
        self.small = Room("Chillout room", 5)

        self.acdc_fan = Guest("Allen", 50, self.playlist[0])

        self.party = [
            Guest("John", 50, self.playlist[0]),
            Guest("Paul", 30, self.playlist[1]),
            Guest("George", 80, self.playlist[2]),
            Guest("Ringo", 25, self.playlist[3]),
            Guest("Stuart", 20, self.playlist[4])                
        ]

        self.forgotten_beatle = Guest("Pete", 4.50, self.playlist[0])

    # Test room attributes
    def test_room_has_name(self):
        self.assertEqual("Party room", self.large.name)

    def test_room_has_capacity(self):
        self.assertEqual(15, self.large.capacity)

    def test_room_guest_list_empty(self):
        self.assertEqual(0, len(self.large.guest_list))

    def test_room_song_list_empty(self):
        self.assertEqual(0, len(self.large.songs))

    def test_room_has_fee(self):
        self.assertEqual(5, self.large.room_fee)

    # Test room methods
    # 1: checking guests in
    def test_check_in_guest_to_room(self):
        self.assertEqual("Allen checked in to Party room", 
                         self.large.check_in(self.acdc_fan))

    def test_guest_is_already_in_room(self):
        self.large.check_in(self.acdc_fan)
        self.assertEqual("Allen has already checked in", self.large.check_in(self.acdc_fan))
        self.assertEqual(1, len(self.large.guest_list))

    def test_room_is_at_capacity(self):
        for guest in self.party:
            self.small.check_in(guest)

        self.assertEqual("Cannot add guest: Room is full", self.small.check_in(self.acdc_fan))
            
    # 2: checking guests out
    def test_guest_check_out_of_room(self):
        self.large.check_in(self.acdc_fan)
        self.assertEqual("Allen has left Party room", 
                         self.large.check_out(self.acdc_fan))

    def test_guest_not_in_room(self):
        self.large.check_in(self.acdc_fan)
        self.assertFalse(self.large.guest_in_room(self.party[0]))

    def test_guest_in_room(self):
        self.large.check_in(self.acdc_fan)
        self.assertTrue(self.large.guest_in_room(self.acdc_fan))

    # 3: adding songs
    def test_add_song_to_room(self):
        self.large.add_song(self.playlist[0])
        self.assertEqual(1, len(self.large.songs))

    def test_song_already_added(self):
        self.large.add_song(self.playlist[0])
        self.assertTrue(len(self.large.songs) == 1)

    # Integration test
    def test_run_karaoke_room(self):
        pass





                
                                

