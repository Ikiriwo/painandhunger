# Nova funcionalidade: Contador de visitas
visitas = 0

def saudacao():
    global visitas
    visitas += 1
    print(f"Olá, mundo! Bem-vindo ao meu software. Você é o visitante número {visitas}.")

def despedida():
    print("Tchau, mundo! Volte sempre.")