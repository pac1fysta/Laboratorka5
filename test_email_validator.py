import unittest
from email_validator import is_valid_email

class TestEmailValidator(unittest.TestCase):

    def test_valid_emails(self):
        valid_emails = [
            "user@example.com",
            "test.name@domain.co",
            "user_name@domain.org",
            "user+filter@domain.ru",
            "user123@subdomain.domain.com",
            "my.email@domain.io"
        ]
        for email in valid_emails:
            with self.subTest(email=email):
                self.assertTrue(is_valid_email(email))

    def test_invalid_emails(self):
        invalid_emails = [
            "plainaddress",
            "missing@dot",
            "@missinglocal.com",
            "user@.com",
            "user@domain.",
            "user@domain..com",
            "user@domain.c",
            "user name@domain.com",
            "user@domain,com",
            ".user@domain.com",          # точка в начале локальной части
            "user.@domain.com",          # точка в конце локальной части
            "user@.domain.com",          # точка сразу после @
            "user@domain..com",          # две точки подряд
            "user@domain-.com",          # дефис перед точкой
            "user@-domain.com",          # дефис в начале домена
            "user@domain.c"              # слишком короткий домен
        ]
        for email in invalid_emails:
            with self.subTest(email=email):
                self.assertFalse(is_valid_email(email))

    def test_edge_cases(self):
        self.assertFalse(is_valid_email(""))
        self.assertFalse(is_valid_email(None))
        self.assertFalse(is_valid_email(123))

if __name__ == "__main__":
    unittest.main()