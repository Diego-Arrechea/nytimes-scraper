# NYTimes Scraper
Bienvenido al README de mi proyecto. Si prefieres leer esta documentación en ingles, puedes acceder desde aquí. [here](README.md).
## Introducción

Esta biblioteca de Python, NYTimes Scraper, está diseñada para obtener e interactuar con datos del sitio web de The New York Times. Proporciona clases y funciones para extraer varios tipos de información, incluyendo artículos, videos, audios, paidpost, etc.

# Tabla de contenidos
- [Instalación](#instalación)
- [Funcionalidades](#funcionalidades)
- [Clases](#clases)
- [Uso](#uso)

## Instalación

Instala la biblioteca NYTimes Scraper usando pip:

```bash
pip install nyt-scraper
```

## Funcionalidades
- ## Función de Búsqueda
  - Realiza búsquedas de cualquier palabra utilizando una palabra clave.
  - Ordena la información por "newest" "oldest" o "best".
  - Filtra los resultados por tipo o sección.

- ## Versatilidad
  - Accede a información de varios tipos de contenido, incluyendo artículos, videos, audio, presentaciones de diapositivas, recetas, contenido interactivo y publicaciones pagadas, utilizando solo la URL.
  - Obtain profiles of persons by providing their URL.

- ## Descarga de multimedia
  - Descarga videos e imágenes en diferentes calidades.

## Clases

### `Scraper`

La clase Scraper es la interfaz principal para interactuar con el sitio web de The New York Times. Proporciona métodos para realizar búsquedas, obtener artículos, recetas y demas entradas.


- `search(keyword, sort="newest", type_="", section="")`
    - Realiza una búsqueda en la base de datos de The New York Times.
    - `keyword` (str): El término de búsqueda.
    - `sort` (str, optional): Orden de clasificación ("newest", "oldest", "best").
    - `type_` (str, optional): Tipo de contenido para filtrar. ('article', 'recipe', 'video', 'etc')
    - `section` (str, optional): Sección para filtrar. ('food', 'arts', 'travel', 'business', 'etc')

- `search_person(url)`
    - Searches for information about a person based on their URL.
    - `url` (str): URL of the person.

- `search_suggest(query)`
    - Obtiene sugerencias de búsqueda para una consulta dada.
    - `query` (str): URL de la persona.

- `get_article(url)`
    - Obtiene un artículo basado en su URL.
    - `query` (str): URL de la persona.

- `get_video(url)`
    - Obtiene un video basado en su URL.
    - `query` (str): URL de la persona.

- `get_audio(url)`
    - Obtiene un audio basado en su URL.
    - `query` (str): URL de la persona.

- `get_slideshow(url)`
    - Obtiene un slideshow basado en su URL.
    - `query` (str): URL de la persona.

- `get_recipe(url)`
    - Obtiene una receta basado en su URL.
    - `query` (str): URL de la persona.

- `get_interactive(url)`
    - Obtiene un interactive basado en su URL.
    - `query` (str): URL de la persona.

- `get_paidpost(url)`
    - Obtiene un paidpost basado en su URL.
    - `query` (str): URL de la persona.

## Uso
#### `Inicialización`
```python
import nyt_scraper
scraper = nyt_scraper.Scraper()
```
#### `Search`
Puedes realizar búsquedas en la base de datos de The New York Times utilizando la función de búsqueda.
##### Methods
- `next(self)`: Recupera las siguientes 10 entradas en cada llamada y devuelve una lista de entradas que representan los nuevos resultados. También actualiza la lista de Search.entries. Ten en cuenta que un máximo de 1000 entradas se pueden obtener de una búsqueda.
# Ejemplo
```python
results = scraper.search(keyword="restaurant", sort="oldest", type_="article", section="food")
print(results)
#output: Search(entries, sections, types, totalEntries)
print(results.totalEntries)
#output: 14386
print(results.entries)
#output: Entries(10 entries)
first_entry_result = results.entries[0]
print(first_entry_result)
#output: Article(type, url, title, summary, authors, language, published, modified, section, subsection, alteration)

for entry in results.entries:
    print(entry.type)
    print(entry.title)

print("Length entries search")
print(len(results))  # 10
results.next()
print(len(results))  # 20
results.next()
print(len(results))  # 30
```

#### `Video`
Recupera un objeto de Video para una URL específica
 ##### Ejemplo

 ```python
video = scraper.get_video(url="https://www.nytimes.com/video/world/asia/100000008963375/china-barbecue-restaurant-explosion.html")

print(video)
# salida: Video(type, url, title, summary, authors, language, section, subsection, published, modified, duration, transcript, renditions, keyword, tags)

print(video.title)  # salida: Explosion Kills Dozens at Barbecue Restaurant in China
print(video.duration)  # salida: 29429

# Descarga la mejor calidad de video
video.download(path="local_path.mp4")

# Para seleccionar una calidad diferente o un formato de archivo diferente, puedes usar video.renditions
```

#### `Renditions`
La clase Renditions representa una colección de diferentes versiones de un video. Estas versiones pueden variar en calidad, tamaño y formato de archivo de video.
Esto es iterable. Es útil para acceder a detalles específicos sobre cada versión, puedes recorrer las "versiones" e imprimir información como "width", "height" y "type_" para cada versión. Esto te permite inspeccionar las características de cada versión disponible antes de seleccionar una para descargar.

##### Methods
- `download(self, path)`: Descarga la mejor calidad de video disponible entre las versiones y la guarda en la ubicación especificada por la ruta. Devuelve True si la descarga fue exitosa.
  - `path (str)`: la ubicación o directorio donde se debe guardar un archivo.

- `find(self, width=None, height=None, type_=None)`: Busca una versión específica dentro de la colección de versiones. Puedes especificar los siguientes criterios de búsqueda:
  - `width (int, optional)`: Ancho de la versión en píxeles.
  - `height (int, optional)`: Altura de la versión en píxeles.
  - `type_ (str, optional)`: Tipo de archivo de video ("mp4", "mov", "etc").
Devuelve la primera versión que coincida con los criterios de búsqueda o None si no se encuentra ninguna coincidencia.

##### Ejemplo

 ```python
video = scraper.get_video(url="https://www.nytimes.com/video/world/asia/100000008963375/china-barbecue-restaurant-explosion.html")

# Accede a las versiones disponibles
renditions = video.renditions

# Descarga la mejor calidad de video (por defecto: mp4)
renditions.download(path="local_path.mp4")

for rendition in renditions:
    print('----------------------------')
    print('width: ', rendition.width)
    print('height: ', rendition.height)
    print('type: ', rendition.type)

rendition_480 = renditions.find(width=480, height=480, type_="webm")
print(rendition_480) # output: Rendition(url, width, height, type, bitrate, aspectRatio)
rendition_480.download("video_480.webm")
```

#### `Images`
La clase Images representa una colección de imágenes. Te permite trabajar con múltiples imágenes de manera eficiente, proporcionando métodos para encontrar imágenes según criterios como el nombre y el tipo (typename).

##### Methods
- `download(self, path)`: Descarga la mejor resolución de imagen disponible y la guarda en la ubicación especificada por la ruta. Devuelve True si la descarga fue exitosa.
  - `path (str)`: la ubicación o directorio donde se debe guardar un archivo.

- `find(self, name=None, typename=None)`: Este método busca una imagen específica dentro de la colección de imágenes en función de los criterios proporcionados:

  - `name` (str, optional).
  - `typename` (str, optional).

  Devuelve la primera imagen que coincida con los criterios especificados o None si no se encuentra ninguna coincidencia.

##### Ejemplo
```python
# Accede a las imágenes disponibles
person = scraper.get_person(url="https://www.nytimes.com/by/axel-boada")
images = person.photos

# Descarga la mejor resolución de la imagen
images.download(path="best_resolution.jpg")

# imprimo informacion sobre todas las imagenes
for image in images:
    print('----------------------------')
    print('name: ', image.name)
    print('typename: ', image.typename)
    print('size: ', image.size)

# Encuentra una imagen específica por nombre y tipo
image = images.find(name="articleLarge", typename="ImageRendition")
print(image)  # Output: Image(url, name, typename, width, height, size)
image.download("articleLarge.jpg") # descarga imagen específica
```

# Todas las clases en plural funcionan de la misma manera: se pueden iterar para obtener las clases en singular y sus respectivos atributos, los cuales pueden verse al imprimir la clase.
### - Sections -> Section
### - Subsections -> Sections
### - Types -> Type
### - Images -> Image
### - Persons -> Person

MIT License
Copyright (c) 2023 Diego-Arrechea