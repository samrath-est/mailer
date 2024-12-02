from setuptools import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "Readme_PyPi.md").read_text()

setup(
    name="mailify",
    version="1.0.6",
    license='MIT',
    description="Simple library to write python emails",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="EncoreSky Technologies",
    author_email='samrathpatidar@encoresky.com',
    url='https://github.com/samrath-est/mailer.git',
    packages=[
        "mailify"
    ],
    include_package_data=True,
    install_requires=[
        "beautifulsoup4==4.12.3"
        "pillow==11.0.0"
    ],
    dependency_links=[

    ],
    entry_points={

    }
)