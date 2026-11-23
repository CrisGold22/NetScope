import ipaddress

def determinarClasificacion(ip):
    if ip.is_loopback:
        return "Loopback"
    elif ip.is_multicast:
        return "Multicast"
    elif ip.is_link_local:
        return "Link-Local"
    elif ip.is_unspecified:
        return "No especificada"
    elif ip.is_reserved:
        return "Reservada"
    elif ip.is_private:
        return "Privada / No global"
    elif ip.is_global:
        return "Global"
    else:
        return "Otra categoría"

def determinarCaracteristica(ip):
    if ip.is_loopback:
        return "Interfaz Local"
    elif ip.is_multicast:
        return "Acceso Multicast"
    elif ip.is_link_local:
        return "Acceso Link-Local"
    elif ip.is_unspecified:
        return "Acceso No especificada"
    elif ip.is_reserved:
        return "Acceso Reservada"
    elif ip.is_private:
        return "Acceso Local"
    elif ip.is_global:
        return "Acceso Publico"
    else:
        return "Normal"

entrada = input("Introduce una dirección IP: ")

try:
    ip = ipaddress.ip_address(entrada)

    print("Dirección válida:", ip)
    print("Versión de la IP: IPv" + str(ip.version))

    clasificacion = determinarClasificacion(ip)
    print("Clasificación de la IP:", clasificacion)

    print("Loopback:", ip.is_loopback)

    caracteristica = determinarCaracteristica(ip)
    print("Característica de la IP:", caracteristica)

except ValueError:
    print("Error: dirección IP inválida")
