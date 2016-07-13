import re


_SLUG_REGEX = re.compile(r'[^A-Z0-9_-]+')


def validate_slug(value):
    """
    Validates a url slug.

    :param value: A url slug
    :return: A valid url slug or `None`
    """
    if not _SLUG_REGEX.search(value):
        return value
