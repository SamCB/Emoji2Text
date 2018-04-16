from os import path
import re

EMOJI_FILE = path.join(path.dirname(__file__), 'emoji-test.txt')

def init_emoji_conversion(emoji_file=EMOJI_FILE):
    def generate_pairs(lines):
        pattern = re.compile(r'^\s([^\w\s]+)\s(\w.*)$')

        for line in f.readlines():
            if line.startswith('#') or len(line) == 0:
                continue

            # lines are broken up like:
            #     CodePoints ; Status # Emoji EmojiName
            # so everything we need is after the #
            _, comparison = line.split('#')
            match = pattern.match(comparison)
            yield match.group(1), match.group(2)


    with open(EMOJI_FILE) as f:
        return {k: v for k, v in generate_pairs(f.readlines())}

DEFAULT_MAPPING = init_emoji_conversion()

def emoji2text(*_, mapping=None):
    if mapping is None:
        mapping = DEFAULT_MAPPING


