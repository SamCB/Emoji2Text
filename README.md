# Emoji2Text

Take a string with emoji in it. Convert them into their text based names.

```python
from emoji2text import emoji2text

emoji2text("""
Take a 🎁 of emoji like 🥑, 😞 or 🤮
and convert them to 🔠 🔡
and you'll be feeling all
🙌🏾 💪🏻 👩‍🔬 👨‍💻 💯 🎊!
""")
# Take a wrapped gift of emoji like avocado, disappointed face or face vomiting
# and convert them to input latin uppercase input latin lowercase
# and you'll be feeling all
# raising hands: medium-dark skin tone flexed biceps: light skin tone woman scientist man technologist hundred points confetti ball!
```

You can also wrap them to help differenciate each emoji like so:

```python
emoji2text("😀😂😂😎", ":")
# :grinning face::face with tears of joy::face with tears of joy::smiling face with sunglasses:

emoji2text("😀😂😂😎", "<", ">")
# <grinning face><face with tears of joy><face with tears of joy><smiling face with sunglasses>
```

Only supports Python 3 and emoji version 5.0 (2017).
If someone is interested in increasing support I'd be happy to look at any PR.

If you spot any errors, please create an issue with a failing input and expected result.

Only possible thanks to the very helpful [grapheme](https://github.com/alvinlindstam/grapheme) module.
