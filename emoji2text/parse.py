from os import path

import grapheme

EMOJI_FILE = path.join(path.dirname(__file__), 'emoji-test.txt')

def init_emoji_conversion(emoji_file=EMOJI_FILE):
    def generate_pairs(lines):
        for line in lines:
            line = line.strip()
            if line.startswith('#') or len(line) == 0:
                continue

            # lines are broken up like:
            #     CodePoints ; Status # Emoji EmojiName
            # so everything we need is after the #
            _, comparison = line.split('#', 1)
            comparison = comparison.strip()

            # grapheme breaks strings down by unicode character so we just need
            # to get the first one
            emoji = grapheme.slice(comparison, end=1)
            name = grapheme.slice(comparison, start=2)
            yield emoji, name

    with open(EMOJI_FILE) as f:
        return {k: v for k, v in generate_pairs(f.readlines())}

DEFAULT_MAPPING = init_emoji_conversion()

def emoji2text(msg, wrap='', other_wrap=None, mapping=None):
    if mapping is None:
        mapping = DEFAULT_MAPPING

    if other_wrap is None:
        l_wrap = wrap
        r_wrap = wrap
    else:
        l_wrap = wrap
        r_wrap = other_wrap

    def generate_message(msg, mapping):
        for c in grapheme.graphemes(msg):
            try:
                yield '{l}{m}{r}'.format(m=mapping[c], l=l_wrap, r=r_wrap)
            except KeyError:
                yield c

    return ''.join(generate_message(msg, mapping))

