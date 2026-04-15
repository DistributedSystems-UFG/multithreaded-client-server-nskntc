from socket import *
from constCS import *
from operacoes import processar_requisicao
import threading

def tratar_conexao(conn, addr):
    """Thread que trata uma conexao/requisicao do cliente."""
    data = conn.recv(4096)
    if data:
        msg = data.decode()
        resposta = processar_requisicao(msg)
        conn.send(resposta.encode())
    conn.close()

s = socket(AF_INET, SOCK_STREAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(50)
print(f"Servidor multithread escutando em {HOST}:{PORT}")

while True:
    conn, addr = s.accept()
    t = threading.Thread(target=tratar_conexao, args=(conn, addr))
    t.start()
