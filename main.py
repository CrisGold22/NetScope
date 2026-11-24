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

def determinarHost(red):
    if red.version == 4:
        if red.prefixlen == 31:
            return 2
        elif red.prefixlen == 32:
            return 1
        else:
            return red.num_addresses - 2
    elif red.version == 6:
        return red.num_addresses

def determinarRangoHost(red):
    if red.version == 4:
        if red.prefixlen == 31:
            return (red.network_address, red.broadcast_address)
        elif red.prefixlen == 32:
            return (red.network_address, red.network_address)
        else:
            primerHost = ipaddress.ip_address(int(red.network_address) + 1)
            ultimoHost = ipaddress.ip_address(int(red.broadcast_address) - 1)
            return (primerHost, ultimoHost)
    elif red.version == 6:
        primeraDireccion = red.network_address
        ultimaDireccion = red[-1]
        return (primeraDireccion, ultimaDireccion)

def analizarRed():
    entrada = input("Introduce una red con prefijo CIDR: ")

    try:
        red = ipaddress.ip_network(entrada, strict=False)

        print("Versión: IPv" + str(red.version))

        print("\n Descripcion General de la Red/Direccion")
        print("===============================================\n")

        direccion = ipaddress.ip_interface(entrada).ip
        print("Version:", red.version)
        
        clasificacion = determinarClasificacion(direccion)
        caracteristica = determinarCaracteristica(direccion)
        print("Clasificacion de la IP:", clasificacion)
        print("Caracteristica de la IP:", caracteristica)

        # Mostrar la dirección de red
        print("Direccion de la red:", red.network_address)
        # Mostrar la máscara de subred
        print("Mascara de subred:", red.netmask)
        # Mostrar el prefijo CIDR
        print("Prefijo CIDR:", red.prefixlen)
        # Mostrar el total de direcciones
        print("Total de direcciones:", red.num_addresses)
        print("Total de host utilizables:", determinarHost(red))
        # Llamar a determinarRangoHost(red)
        # y mostrar los dos valores obtenidos
        primeraIP, ultimaIP = determinarRangoHost(red)
        if red.version == 4:
            print("Primer Host:", primeraIP)
            print("Ultimo Host:", ultimaIP)
        else:
            print("Primer direccion:", primeraIP)
            print("Ultimo direccion:", ultimaIP)
        # Mostrar el broadcast solo si es IPv4
        if red.version == 4:
            print("Broadcast:", red.broadcast_address)

    except ValueError:
        print("Error: red o prefijo inválido")

analizarRed()