def validar_ip(ip):
    partes = ip.split('.')
    if len(partes) != 4:
        return False
    try:
        return all(0 <= int(parte) <= 255 for parte in partes)
    except:
        return False


def validar_porta(porta):
    return porta.isdigit() and 0 < int(porta) <= 65535