import ast
import re
import setuptools

version_re = re.compile(r'^__version_info__\s*=\s*(.*)$', re.M)
with open('afreeze', 'r') as file:
    version_info = version_re.search(file.read()).group(1)
    version = '.'.join(ast.literal_eval(version_info))
with open('README.md') as file:
    long_description = file.read()


setuptools.setup(
    name="afreeze",
    author="Alex Huszagh",
    author_email="ahuszagh@gmail.com",
    version=version,
    scripts=['afreeze'],
    extras_require = {
        'daemon': ['python-daemon>=2.2.0']
    },
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>3.7.0',
    description="Freeze alsa configuration settings.",
    license="Unlicense",
    keywords="alsa linux sound",
    url="https://github.com/Alexhuszagh/afreeze",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Operating System :: POSIX :: Linux',
        'Topic :: Multimedia :: Sound/Audio'
    ],
)
