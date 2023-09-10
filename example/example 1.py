"""
Find first 1000 recipe in sort descent
and save in .csv
"""
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
nytimes_scraper_dir = os.path.join(current_dir, "..", "..")
sys.path.append(nytimes_scraper_dir)


import nyt_scraper
import time
from pprint import pprint
import pandas as pd

scraper = nyt_scraper.Scraper()
Search = scraper.search("restaurant", sort="newest", section="food", type_="article")

for x in range(99):
    Search.next()

data = [
    [
        "type",
        "url",
        "title",
        "summary",
        "authors",
        "section",
        "subsection",
        "published",
        "modified",
        "language",
    ]
]

for entry in Search.entries:
    print(entry.url)
    subsection = entry.subsection.displayName if entry.subsection else None
    section = entry.section.displayName if entry.section else None
    print(entry.authors)
    authors = (
        ", ".join([author.name for author in entry.authors]) if entry.authors else None
    )
    data.append(
        [
            entry.type,
            entry.url,
            entry.title,
            entry.summary,
            authors,
            section,
            subsection,
            entry.published,
            entry.modified,
            entry.language,
        ]
    )

df = pd.DataFrame(data[1:], columns=data[0])
nombre_archivo = "informacion.csv"
df.to_csv(nombre_archivo, index=False)
