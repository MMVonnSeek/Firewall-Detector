import platform
import subprocess

def obter_regras_firewall():
    sistema = platform.system()

    if sistema == "Windows":
        comando = ["netsh", "advfirewall", "firewall", "show", "rule", "name=all"]
    elif sistema == "Linux":
        comando = ["sudo", "iptables", "-L"]
    else:
        return ["Sistema operacional não suportado"]

    try:
        resultado = subprocess.run(comando, capture_output=True, text=True)
        if resultado.returncode != 0:
            return [f"Erro: {resultado.stderr.strip()}"]
        if resultado.stdout:
            return resultado.stdout.splitlines()
        else:
            return ["Nenhuma saída obtida do comando."]
    except Exception as e:
        return [f"Erro ao obter regras: {e}"]
