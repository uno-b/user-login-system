import unittest

import database
import user


class TestUser(unittest.TestCase):

    def setUp(self):
        self.a_user = user.User("Test123", "test1234", "test@test.edu", "11111111")

    def test_add_user(self):
        self.assertFalse(database.check_if_user_exists(self.a_user))
        database.add_user(self.a_user)
        self.assertTrue(database.check_if_user_exists(self.a_user))
        database.delete_user(self.a_user.get_username())

    def test_delete_user(self):
        database.add_user(self.a_user)
        self.assertTrue(database.check_if_user_exists(self.a_user))
        database.delete_user(self.a_user.get_username())
        self.assertFalse(database.check_if_user_exists(self.a_user))

    def test_add_note(self):
        database.add_user(self.a_user)
        database.add_note("101a", "Heyy~!", self.a_user.get_username())
        self.assertTrue(database.check_if_note_exists("101a"))
        database.delete_user(self.a_user.get_username())
        database.delete_note("101a")

    def test_delete_note(self):
        database.add_note("101a", "Heyy~!", self.a_user.get_username())
        self.assertTrue(database.check_if_note_exists("101a"))
        database.delete_note("101a")
        self.assertFalse(database.check_if_note_exists("101a"))
        database.delete_user(self.a_user.get_username())

    def test_login_verify(self):
        database.add_user(self.a_user)
        self.assertTrue(database.login_verify(self.a_user.get_username(), self.a_user.get_password()))
        database.delete_user(self.a_user.get_username())

    def test_login_verify_wrong(self):
        database.add_user(self.a_user)
        self.assertFalse(database.login_verify("WrongUsername", "WrongPassword"))
        database.delete_user(self.a_user.get_username())

    def test_get_notes(self):
        database.add_user(self.a_user)
        database.add_note("101a", "Test", self.a_user.get_username())
        database.add_note("101b", "Test", self.a_user.get_username())

        notes = database.get_notes(self.a_user.get_username())
        self.assertEqual(len(notes), 2)

        database.delete_note("101a")
        database.delete_note("101b")
        database.delete_user(self.a_user.get_username())

    def test_get_user_data(self):
        database.add_user(self.a_user)
        result = database.get_user_data("Test123")

        self.assertEqual(result[1], "test1234")
        self.assertEqual(result[2], "test@test.edu")
        self.assertEqual(result[3], "11111111")

        database.delete_user(self.a_user.get_username())
