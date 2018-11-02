from tools import strategy


def format(text, option=None):
    """Applies the formatting option to the input text"""
    if not option:
        return ""

    return strategy.format(option, text)


def get_formats():
    """Defines a dictionary of all possible formatting options"""
    formats = {
        "tabs_to_spaces": "Tabs to spaces",
        "remove_whitespace": "Remove whitespace",
        "reverse": "Reverse",
    }

    return formats
