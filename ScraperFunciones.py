from bs4 import BeautifulSoup
import requests
import csv

from scrapM import limpiar_string_url
from scrapM import datear_url
from scrapM import tablear_url

# limpiar_strings_url toma unicamente
# los strings de una url
# y elimina algunos espacios vacios

# datear_url toma los valores de una
# url limpia ( desde limpiar_url_strings),
# filtra espacios vacios
# y los ordena en una lista

# tablear_url toman los valores de
# de una lista ( desde datear_url )
# y los tablea en un csv

# iterar_urls realiza este proceso, tableando
# todas las url requeridas

# Modo de uso:
# igualar nombre de csv tanto en este archivo como
# en el de origen
#

def iterar_urls():
    # Nombre del archivo al cual se quiere guardar datos
    with open('index.csv', 'a') as csv_file:
        # "a" sirva para appendear datos y no sobre escribirlos
        # por ejemplo si se fuese a pasar de nuevo por la lista
        # para agregar nuevos items
        file_writer = csv.writer(csv_file)

        # Si se vuelve a iterar por los datos, comentar este parrafo
        # file_writer.writerow(['Nombre', 'DNI', 'Carrera', 'E civil', 'Sexo', 'Fecha nac', 'Pais nac',
        #                       'Dom Dir', 'Dom Loc', 'Dom barrio', 'Dom cp', 'Telefono', 'Celular', 'Email', 'Colegio',
        #                       'Ingreso CBC', 'Egreso CBC',
        #                       'Lib CBC'])

    for x in range(0000, 7649):
        # Busca formularios en este rango
        url = ("https://www.urldeseada.com.ar?formu={}".format(x))
        w = limpiar_string_url(url)
        # Habia paginas con errores, se corrigió
        if w[0][1:13] != 'Server error':
            print(x)
            a = limpiar_string_url(url)
            b = datear_url(a)
            c = tablear_url(b)
    return


print(iterar_urls())

