import unittest

from main import EnvironmentType


class TestEnvironmentType(unittest.TestCase):
    def test_environment_type_values(self):
        self.assertEqual(EnvironmentType.LOCAL, "local")
        self.assertEqual(EnvironmentType.DEVELOPMENT, "development")
        self.assertEqual(EnvironmentType.PRODUCTION, "production")

    def test_environment_type_enum(self):
        self.assertTrue(isinstance(EnvironmentType.LOCAL, EnvironmentType))
        self.assertTrue(isinstance(EnvironmentType.DEVELOPMENT, EnvironmentType))
        self.assertTrue(isinstance(EnvironmentType.PRODUCTION, EnvironmentType))


if __name__ == "__main__":
    unittest.main()
