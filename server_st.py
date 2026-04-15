from socket import *
from constCS import *
from operacoes import processar_requisicao

s = socket(AF_INET, SOCK_STREAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(5)
print(f"Servidor single-thread escutando em {HOST}:{PORT}")

while True:
    conn, addr = s.accept()
    print(f"Conexao de {addr}")
    while True:
        data = conn.recv(4096)
        if not data:
            break
        msg = data.decode()
        resposta = processar_requisicao(msg)
        conn.send(resposta.encode())
    conn.close()
    print(f"Conexao com {addr} encerrada")
