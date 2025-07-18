"""
main.py

Description:
    This script performs web scraping on the website 'Books to Scrape' to extract
    the titles of books that have a high user rating (4 or 5 stars). It iterates
    through all available pages of the catalog, parses the HTML content, and collects
    book titles meeting the rating criteria.

Author: Alejandro Orozco Romo
Created: 2025-07-04
Last Modified: 2025-07-04
Python Version: 3.12

Dependencies:
    - requests: for making HTTP requests to fetch web page content
    - bs4 (BeautifulSoup): for parsing and navigating HTML
    - lxml: parser used by BeautifulSoup for fast parsing

License:
    MIT License

Notes:
    - Make sure the website structure (class names) has not changed before running.
    - This script is intended for educational purposes only.
"""


import bs4
import requests

# crear url sin numero de pagina
url_base = 'https://books.toscrape.com/catalogue/page-{}.html'

# lista de titulos con 4 o 5 estrellas
titulos_rating_alto = []

# iterar paginas
for pagina in range(1, 51):

    # crear sopa en cada pagina
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

    # seleccionar datos de los libros
    libros = sopa.select('.product_pod')

    # iterar libros
    for libro in libros:

        # chequear que tengan 4 o 5 estrellas
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0:

            # guardar titulo en variable
            titulo_libro = libro.select('a')[1]['title']

            # agregar libro a la lista
            titulos_rating_alto.append(titulo_libro)

# ver libros 4 u 5 estrellas en consola
for t in titulos_rating_alto:
    print(t)
