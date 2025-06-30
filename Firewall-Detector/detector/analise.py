import socket

def testar_porta(ip, porta, timeout=2):
    try:
        with socket.create_connection((ip, porta), timeout=timeout):
            return True
    except Exception as e:
        print(f"[DEBUG] Falha em {ip}:{porta} -> {e}")
        return False


def simular_conexoes(lista):
    resultados = []
    for ip, porta in lista:
        status = testar_porta(ip, porta)
        resultados.append((ip, porta, "Permitido" if status else "Bloqueado"))
    return resultados
