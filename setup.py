from setuptools import setup, find_packages

with open("README.md", "r") as fp:
    long_description = fp.read()

setup(
    name="nyt_scraper",
    version="1.0.0",
    description="A scraping library for extracting data from the New York Times",
    author="Diego Arrechea",
    author_email="diego.arrechea.job@gmail.com",
    url="https://github.com/Diego-Arrechea/nytimes_scraper",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        # List of required dependencies
        "beautifulsoup4==4.11.2",
        "requests",
        "m3u8==3.5.0",
        "Pillow==10.0.0",  # Choose one version of Pillow (either 9.4.0 or 10.0.0)
    ],
)
