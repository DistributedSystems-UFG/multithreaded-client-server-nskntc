from socket import *
from constCS import *
import json
import random
import time

def gerar_requisicao():
    """Gera uma requisicao aleatoria."""
    opcao = random.randint(0, 4)
    if opcao == 0:
        return {"operacao": "fatorial", "parametro": random.randint(1, 20)}
    elif opcao == 1:
        return {"operacao": "contar_primos", "parametro": random.randint(100, 1000)}
    elif opcao == 2:
        return {"operacao": "is_primo", "parametro": random.randint(2, 10000)}
    elif opcao == 3:
        ops = ["add", "sub", "mul", "div"]
        return {"operacao": "calculadora", "a": random.uniform(1, 100), "b": random.uniform(1, 100), "op": random.choice(ops)}
    else:
        palavras = ["sistemas", "distribuidos", "computacao", "rede", "servidor", "cliente"]
        texto = " ".join(random.choices(palavras, k=random.randint(2, 5)))
        return {"operacao": "reverter", "parametro": texto}

def enviar_requisicao(requisicao):
    """Abre conexao, envia requisicao, recebe resposta, fecha conexao."""
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((HOST, PORT))
    msg = json.dumps(requisicao)
    s.send(msg.encode())
    data = s.recv(4096)
    resposta = json.loads(data.decode())
    s.close()
    return resposta

def main():
    NUM_REQUISICOES = 200

    print(f"Cliente single-thread - enviando {NUM_REQUISICOES} requisicoes...")
    inicio = time.time()

    for i in range(NUM_REQUISICOES):
        req = gerar_requisicao()
        resp = enviar_requisicao(req)

    fim = time.time()
    tempo_total = fim - inicio
    print(f"Tempo total: {tempo_total:.4f} segundos")
    print(f"Media por requisicao: {tempo_total/NUM_REQUISICOES*1000:.2f} ms")

if __name__ == "__main__":
    main()
