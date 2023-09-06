from setuptools import setup, find_packages

setup(
    name="nytimes_scraper",
    version="1.0.0",
    description="A scraping library for extracting data from the New York Times",
    author="Diego Arrechea",
    author_email="diego.arrechea.job@gmail.com",
    packages=find_packages(),
    install_requires=[
        # List of required dependencies
        "beautifulsoup4==4.11.2",
        "requests==2.31.0",
        "m3u8==3.5.0",
        "pandas==1.5.3",
        "Pillow==10.0.0",  # Choose one version of Pillow (either 9.4.0 or 10.0.0)
    ],
)
