from detector.regras import obter_regras_firewall
from detector.analise import simular_conexoes
from detector.utils import validar_ip, validar_porta


def iniciar_cli():
    conexoes = []
    print("==== Firewall Detector - Modo CLI ====")
    while True:
        ip = input("Digite o IP (ou 'sair'): ")
        if ip.lower() == 'sair':
            break
        if not validar_ip(ip):
            print("IP inválido.")
            continue

        porta = input("Digite a porta: ")
        if not validar_porta(porta):
            print("Porta inválida.")
            continue

        conexoes.append((ip, int(porta)))

    print("\n[!] Executando teste de conexões...")
    resultados = simular_conexoes(conexoes)
    for ip, porta, status in resultados:
        print(f"{ip}:{porta} - {status}")

    print("\n[!] Regras atuais do firewall:")
    for linha in obter_regras_firewall():
        print(linha)