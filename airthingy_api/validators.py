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


def validate_choices(value, choices):
    """
    Validates the existence of a value in a list of Django-styled choice/name
    pairs.

    :param value: A choice
    :param choices: A Django-style list of choices
    :return: A valid choice or `None`
    """
    if value in [t[0] for t in choices]:
        return value
