from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='emoji2text',
    version='0.1',
    description='Can\'t handle emoji? Use this to treat them as plain strings, according to the description provided by unicode.',
    long_description=readme(),
    keywords='emoji convert text unicode plain',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Topic :: Text Processing :: General'
    ],
    url='http://github.com/samcb',
    author='Sam CB',
    author_email='s.cbird01@gmail.com',
    license='MIT',
    packages=['emoji2text'],
    zip_safe=False
)
