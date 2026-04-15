import math
import json

def fatorial(n):
    if n < 0:
        return "Erro: numero negativo"
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def is_primo(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def contar_primos(n):
    count = 0
    for i in range(2, n + 1):
        if is_primo(i):
            count += 1
    return count

def calculadora(a, b, op):
    if op == "add":
        return a + b
    elif op == "sub":
        return a - b
    elif op == "mul":
        return a * b
    elif op == "div":
        if b == 0:
            return "Erro: divisao por zero"
        return a / b
    else:
        return "Erro: operacao desconhecida"

def reverter_texto(texto):
    return texto[::-1]

def processar_requisicao(data):
    try:
        req = json.loads(data)
        operacao = req.get("operacao")

        if operacao == "fatorial":
            resultado = fatorial(int(req["parametro"]))
        elif operacao == "contar_primos":
            resultado = contar_primos(int(req["parametro"]))
        elif operacao == "is_primo":
            resultado = is_primo(int(req["parametro"]))
        elif operacao == "calculadora":
            resultado = calculadora(float(req["a"]), float(req["b"]), req["op"])
        elif operacao == "reverter":
            resultado = reverter_texto(str(req["parametro"]))
        else:
            resultado = "Erro: operacao desconhecida"

        resposta = {"status": "ok", "operacao": operacao, "resultado": str(resultado)}
    except Exception as e:
        resposta = {"status": "erro", "mensagem": str(e)}

    return json.dumps(resposta)
