#!/usr/bin/python3

# GeoTrackerIP By JRIC2002.
# Modificado por @Ux4hack

import requests
import json
import sys

class Color:

    reset = "\033[0m"
    bold = "\033[1m"
    dark = "\033[2m"
    italic = "\033[3m"
    underline = "\033[4m"
    reverse = "\033[7m"
    hidden = "\033[8m"
    black= "\033[30m"
    gray = "\033[1;30m"
    red= "\033[31m"
    green = "\033[32m"
    yellow = "\033[33m"
    blue = "\033[34m"
    magenta = "\033[35m"
    cyan = "\033[36m"
    white = "\033[37m"

color = Color()

class Start:

    def __init__(self):
        """ Variables de instancia. """
        pass

start = Start()

class Functions:
    
    def __init__(self):
        pass

    def geolocation_ip(self, ip):
        """ Geolocaliza un dominio """

        #Datos
        try:
            while True:
                if "http://" in ip:
                    ip = ip[7:]
                elif "www." in ip:
                    ip = ip[4:]
                elif "https://" in ip:
                    ip = ip[8:]
                else:
                    break

            api_url = "http://ip-api.com/json/{}?fields=status,message,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,mobile,proxy,query".format(ip)
            res = requests.get(api_url)
            datos = json.loads(res.content)

            target = ip
            direccion_ip = datos['query']
            status = datos['status']
            asn = datos['as']
            ciudad = datos['city']
            pais = datos['country']
            codigo_pais = datos['countryCode']
            isp = datos['isp']
            latitud = datos['lat']
            longitud = datos['lon']
            organizacion = datos['org']
            codigo_region = datos['region']
            region = datos['regionName']
            timezone = datos['timezone']
            codigo_zip = datos['zip']
            mobile = datos['mobile']
            proxy = datos['proxy']
            google_maps = "https://www.google.com/maps/search/?api=1&query={},{}".format(latitud, longitud)

            #Imprime los resultados obtenidos
            print("")
            print("{}[{}*{}] {}Estado:{} {}".format(color.green, color.white, color.green, color.white, color.green, status))
            print("{}[{}*{}] {}IP:{} {}".format(color.green, color.white, color.green, color.white, color.green, direccion_ip))
            print("{}[{}*{}] {}ASN:{} {}".format(color.green, color.white, color.green, color.white, color.green, asn))
            print("{}[{}*{}] {}Ciudad:{} {}".format(color.green, color.white, color.green, color.white, color.green, ciudad))
            print("{}[{}*{}] {}Country:{} {}".format(color.green, color.white, color.green, color.white, color.green, pais))
            print("{}[{}*{}] {}Country Code:{} {}".format(color.green, color.white, color.green, color.white, color.green, codigo_pais))
            print("{}[{}*{}] {}ISP:{} {}".format(color.green, color.white, color.green, color.white, color.green, isp))
            print("{}[{}*{}] {}Latitud:{} {}".format(color.green, color.white, color.green, color.white, color.green, latitud))
            print("{}[{}*{}] {}Longitud:{} {}".format(color.green, color.white, color.green, color.white, color.green, longitud))
            print("{}[{}*{}] {}Organización:{} {}".format(color.green, color.white, color.green, color.white, color.green, organizacion))
            print("{}[{}*{}] {}Codigo de región:{} {}".format(color.green, color.white, color.green, color.white, color.green, codigo_region))
            print("{}[{}*{}] {}Nombre de region:{} {}".format(color.green, color.white, color.green, color.white, color.green, region))
            print("{}[{}*{}] {}Zona horaria:{} {}".format(color.green, color.white, color.green, color.white, color.green, timezone))
            print("{}[{}*{}] {}Codigo Zip:{} {}".format(color.green, color.white, color.green, color.white, color.green, codigo_zip))
            print("{}[{}*{}] {}Móbil:{} {}".format(color.green, color.white, color.green, color.white, color.green, mobile))
            print("{}[{}*{}] {}Proxy:{} {}".format(color.green, color.white, color.green, color.white, color.green, proxy))
            print("{}[{}*{}] {}Google Maps:{} {}".format(color.green, color.white, color.green, color.white, color.green, google_maps))
            print("{}".format(color.reset))
        except Exception:
            print("")
            print("{}  ERROR:\033[37m Dominio inválido o inexistente...{}".format(color.red, color.reset))

#Instancia de la clase Functions
functions = Functions()

if len(sys.argv) == 1:
    start.help_menu()
elif len(sys.argv) == 3:
    if sys.argv[1] == "-t" or sys.argv[1] == "--target":
        functions.geolocation_ip(sys.argv[2])
