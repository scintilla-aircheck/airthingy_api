import unittest


class ValidateSlugUnitTestCase(unittest.TestCase):

    def test_validate_slug_returns_valid_slugs(self):
        from ..validators import validate_slug
        valid_slugs = (
            'SPEC_SO2_20PPM',
            'MICS-6814',
            'DHT22',
            'SDS-021')
        for slug in valid_slugs:
            result = validate_slug(slug)
            self.assertEqual(slug, result)

    def test_validate_slug_returns_none_for_invalid_slugs(self):
        from ..validators import validate_slug
        invalid_slugs = (
            'Inovafit SDS-021',
            'MiCS-6814')
        for invalid_slug in invalid_slugs:
            result = validate_slug(invalid_slug)
            self.assertIsNone(result)
