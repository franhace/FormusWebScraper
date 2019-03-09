import requests
from bs4 import BeautifulSoup
import csv

# Vemos link en el navegador
# Hubo que copiar geckodriver al PATH
# driver = webdriver.Firefox()
# driver.get(url)

url = "https://www.urldeseada.com.ar/"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


# Funcion que devuelve una lista con todos los strings de la pagina
# Unicamente con texto, Con espacios vacios eliminados

def limpiar_string_url(a):
    x = []
    response = requests.get(a)
    soup = BeautifulSoup(response.text, 'html.parser')
    for string in soup.stripped_strings:
        x.append(repr(string))
    return x


# Funciones para conseguir exactamente los datos
# que queremos

datos = [] # Lista de todos los datos recabados
# No se usa mas


def nombre_completo(casilla):
    w = len(casilla) - 1
    target = (casilla[21:w])
    datos.append(target)
    return target


def dni_completo(casilla):
    w = len(casilla) - 1
    target = (casilla[7:w])
    datos.append(target)
    return target


def carrera_completo(casilla):
    w = len(casilla) - 1
    target = (casilla[10:w])
    datos.append(target)
    return target


def estado_civil_completo(casilla):
    w = len(casilla) - 1
    target = (casilla[15:w])
    datos.append(target)
    return target


def sexo_completo(casilla):
    w = len(casilla) - 1
    target = (casilla[7:w])
    datos.append(target)
    return target


def nac_completo(casilla):
    w = len(casilla) - 1
    target = (casilla[12:w])
    datos.append(target)
    return target


def pais_completo(casilla):
    w = len(casilla) - 2
    target = (casilla[22:w])
    datos.append(target)
    return target


def dom_completo(casilla):
    w = len(casilla) - 1
    target = (casilla[12:w])
    datos.append(target)
    return target


def dom_pcia_completo(casilla):
    w = len(casilla) - 1
    target = (casilla[7:w])
    datos.append(target)
    return target


def dom_loc_completo(casilla):
    w = len(casilla) - 1
    target = (casilla[12:w])
    datos.append(target)
    return target


def dom_cp_completo(casilla):
    w = len(casilla) - 1
    target = (casilla[13:w])
    datos.append(target)
    return target


def tel_completo(casilla):
    ce = (casilla.index('C'))
    target = (casilla[6:ce-1])
    datos.append(target)
    return target


def cel_completo(casilla):
    dospu = (casilla.index(':'))
    w = len(casilla) - 1
    target = (casilla[dospu+2:w])
    datos.append(target)
    return target


def email_completo(casilla):
    w = len(casilla) - 1
    target = (casilla[1:w])
    datos.append(target)
    return target


def secu_completo(casilla):
    w = len(casilla) - 1
    target = (casilla[13:w])
    datos.append(target)
    return target


def cbc_in(casilla):
    w = len(casilla) - 1
    target = (casilla[17:w])
    datos.append(target)
    return target


def cbc_out(casilla):
    w = len(casilla) - 1
    target = (casilla[17:w])
    datos.append(target)
    return target


def cbc_lib(casilla):
    w = len(casilla) - 1
    target = (casilla[36:w])
    datos.append(target)
    return target


# datear_url nuclea todos los datos que queremos
# Para esto toma los valores de una
# url limpia ( desde limpiar_url_strings),
# filtra espacios vacios
# y los ordena en una lista

def datear_url(w):
    x = w
    data = []
    casilla_nombre = x[11]
    data.append(nombre_completo(casilla_nombre))
    casilla_dni = x[12]
    data.append(dni_completo(casilla_dni))
    casilla_carrera = x[13]
    data.append(carrera_completo(casilla_carrera))
    casilla_estado_civil = x[14]
    data.append(estado_civil_completo(casilla_estado_civil))
    casilla_sexo = x[15]
    data.append(sexo_completo(casilla_sexo))
    casilla_nac = x[16]
    data.append(nac_completo(casilla_nac))
    casilla_pais = x[17]
    data.append(pais_completo(casilla_pais))
    casilla_dom = x[18]
    data.append(dom_completo(casilla_dom))
    casilla_dom_pcia = x[19]
    data.append(dom_pcia_completo(casilla_dom_pcia))
    casilla_dom_loc = x[20]
    data.append(dom_loc_completo(casilla_dom_loc))
    casilla_dom_cp = x[21]
    data.append(dom_cp_completo(casilla_dom_cp))
    casilla_tel = x[22]
    data.append(tel_completo(casilla_tel))
    casilla_cel = x[22]
    data.append(cel_completo(casilla_cel))
    casilla_email = x[23]
    data.append(email_completo(casilla_email))
    casilla_secu = x[24]
    data.append(secu_completo(casilla_secu))
    casilla_cbc_in = x[25]
    data.append(cbc_in(casilla_cbc_in))
    casilla_cbc_out = x[26]
    data.append(cbc_out(casilla_cbc_out))
    casilla_cbc_libreta = x[30]
    data.append(cbc_lib(casilla_cbc_libreta))

    return data


def server_error(uu):

    x = limpiar_string_url(uu)
    print(x[0][1:13])
    if x[0][1:13] == 'Server error':
        print("error!")


# print(datear_url(url))

# tablear_url toman los valores de
# de una lista ( desde datear_url )
# y los tablea en un csv

def tablear_url(x):
    # w = limpiar_string_url(url)
    dateas = x
    # Matchear el nombre del archivo, con el de RunScript
    with open('index.csv', 'a') as csv_file:
        file_writer = csv.writer(csv_file)
        # file_writer.writerow(['Nombre', 'DNI', 'Carrera', 'E civil', 'Sexo', 'Fecha nac', 'Pais nac',
        #                       'Dom Dir', 'Dom Loc', 'Dom barrio', 'Dom cp', 'Telefono', 'Email', 'Colegio',
        #                       'Ingreso CBC', 'Egreso CBC',
        #                       'Lib CBC'])
        file_writer.writerow(dateas)
    return dateas

