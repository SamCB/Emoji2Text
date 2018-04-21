from setuptools import setup
import unittest

def readme():
    try:
        import pypandoc
        return pypandoc.convert('README.md', 'rst')
    except:
        # Fall back to raw README
        with open('README.md') as f:
            return f.read()

# from https://stackoverflow.com/a/37033551
def my_test_suite():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('emoji2text/tests', pattern='test_*.py')
    return test_suite

setup(
    name='emoji2text',
    version='0.1.5',
    description='Can\'t handle emoji? Use this to treat them as plain strings, according to the description provided by unicode.',
    long_description=readme(),
    keywords='emoji convert text unicode plain',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Topic :: Text Processing :: General'
    ],
    url='https://github.com/SamCB/Emoji2Text',
    author='Sam CB',
    author_email='s.cbird01@gmail.com',
    license='MIT',
    packages=['emoji2text'],
    include_package_data=True,
    install_requires=[
        'grapheme'
    ],
    test_suite='setup.my_test_suite',
    zip_safe=False
)

