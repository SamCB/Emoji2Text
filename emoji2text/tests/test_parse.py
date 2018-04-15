from unittest import TestCase
import re

import emoji2text

TEST_STRING = """Foo Bar Baz """

TEST_TARGETS = [
    (u'\U0001F468\U0001F3FD\U0000200D\U0001F4BB', 'man technologist: medium skin tone'),
    (u'\U0001F469\U0001F3FD\U0000200D\U0001F4BB', 'woman technologist: medium skin tone'),
    (u'\U0001f44d', 'thumbs up')
]

class TestParse(TestCase):
    def test_converts_all_emoji(self):
        with open('../emoji-test.txt') as f:
            # Use the document we use for building our converter.
            #  it contains every emoji
            emoji_test = f.read()

        result = emoji2text.emoji2text(emoji_test, ':')

        for original, update in zip(emoji_test.split('\n'), result.split('\n')):
            if original.beginswith('#') or len(original) == 0:
                self.assertEqual(original, update, "Boring line, should be identical")

            original_start, original_end = original.split('#')
            update_start, update_end = update.split('#')

            self.assertEqual(original_start, update_start, "No emoji here, should be identical")

            f = re.findall(r'(\w.*)', original_end)
            self.assertGreater(len(f), 0, 'something went wrong with parsing the original')

            original_emoji_name = f[0]

            self.assertEqual(
                update, ' :%: %' % (original_emoji_name, original_emoji_name),
                'Deconvert emoji'
            )

    def test_default_wrap(self):
        result = emoji2text.emoji2text(
            ''.join('Foo ', TEST_TARGETS[0][0], 'bar', TEST_TARGETS[1][0], TEST_TARGETS[2][0], 'baz')
        )
        self.assertEqual(
            result,
            ''.join('Foo ', TEST_TARGETS[0][1], 'bar', TEST_TARGETS[1][1], TEST_TARGETS[2][1], 'baz')
        )

    def test_adds_wrap_properly(self):
        result = emoji2text.emoji2text(
            ''.join('Foo ', TEST_TARGETS[0][0], 'bar', TEST_TARGETS[1][0], TEST_TARGETS[2][0], 'baz'),
            ':'
        )
        self.assertEqual(
            result,
            ''.join('Foo :', TEST_TARGETS[0][1], ':bar:', TEST_TARGETS[1][1], '::', TEST_TARGETS[2][1], ':baz')
        )

    def test_adds_double_wrap_properly(self):
        result = emoji2text.emoji2text(
            ''.join('Foo ', TEST_TARGETS[0][0], 'bar', TEST_TARGETS[1][0], TEST_TARGETS[2][0], 'baz'),
            '<', '>'
        )
        self.assertEqual(
            result,
            ''.join('Foo <', TEST_TARGETS[0][1], '>bar<', TEST_TARGETS[1][1], '><', TEST_TARGETS[2][1], '>baz')
        )
