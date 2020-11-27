import unittest
import user


class TestUser(unittest.TestCase):

    def setUp(self):
        self.a_user = user.User("Uno123", "uno1998", "unb170@aubg.edu", "99674769")

    def test_get_username(self):
        self.assertEqual(self.a_user.get_username(), "Uno123")

    def test_get_password(self):
        self.assertEqual(self.a_user.get_password(), "uno1998")

    def test_get_email(self):
        self.assertEqual(self.a_user.get_email(), "unb170@aubg.edu")

    def test_get_phone_number(self):
        self.assertEqual(self.a_user.get_phone_number(), "99674769")

    def test_set_username(self):
        self.assertEqual(self.a_user.get_username(), "Uno123")
        self.a_user.set_username("Unu98")
        self.assertEqual(self.a_user.get_username(), "Unu98")

    def test_set_password(self):
        self.assertEqual(self.a_user.get_password(), "uno1998")
        self.a_user.set_password("uno98")
        self.assertEqual(self.a_user.get_password(), "uno98")

    def test_set_email(self):
        self.assertEqual(self.a_user.get_email(), "unb170@aubg.edu")
        self.a_user.set_email("unb171@aubg.edu")
        self.assertEqual(self.a_user.get_email(), "unb171@aubg.edu")

    def test_set_phone_number(self):
        self.assertEqual(self.a_user.get_phone_number(), "99674769")
        self.a_user.set_phone_number("99674770")
        self.assertEqual(self.a_user.get_phone_number(), "99674770")

    def test_set_username_wrong(self):
        self.assertRaises(ValueError, self.a_user.set_username, "man")
        self.assertRaises(ValueError, self.a_user.set_username, "tooLongUsernameForTheProgramToHandle")
        self.assertRaises(ValueError, self.a_user.set_username, ".HasDot")
        self.assertRaises(ValueError, self.a_user.set_username, "HasDot.")

    def test_set_password_wrong(self):
        self.assertRaises(ValueError, self.a_user.set_password, "man")
        self.assertRaises(ValueError, self.a_user.set_password, "tooLongPassword")
        self.assertRaises(ValueError, self.a_user.set_password, "NOLOWERCASE")
        self.assertRaises(ValueError, self.a_user.set_password, "NoDigits")

    def test_set_email_wrong(self):
        self.assertRaises(ValueError, self.a_user.set_email, "unb 170@aubg.edu")
        self.assertRaises(ValueError, self.a_user.set_email, "Some text")

    def test_set_phone_number_wrong(self):
        self.assertRaises(ValueError, self.a_user.set_phone_number, "12345678910")
        self.assertRaises(ValueError, self.a_user.set_phone_number, "SomeText")
        self.assertRaises(ValueError, self.a_user.set_phone_number, "1234")