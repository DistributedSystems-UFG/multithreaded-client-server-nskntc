import subprocess
import time
import sys
import os
import signal

PYTHON = sys.executable
DIR = os.path.dirname(os.path.abspath(__file__))

def rodar_cenario(nome, servidor_script, cliente_script):
    """Inicia o servidor, roda o cliente, e retorna a saida."""
    print(f"\n{'='*60}")
    print(f"  CENARIO: {nome}")
    print(f"{'='*60}")

    # Inicia o servidor
    servidor = subprocess.Popen(
        [PYTHON, os.path.join(DIR, servidor_script)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    time.sleep(1)  # Aguarda servidor iniciar

    # Roda o cliente
    resultado = subprocess.run(
        [PYTHON, os.path.join(DIR, cliente_script)],
        capture_output=True,
        text=True,
        timeout=120
    )

    print(resultado.stdout)
    if resultado.stderr:
        print(f"Erros: {resultado.stderr}")

    # Encerra o servidor
    servidor.terminate()
    try:
        servidor.wait(timeout=3)
    except subprocess.TimeoutExpired:
        servidor.kill()

    time.sleep(1)  # Aguarda porta ser liberada
    return resultado.stdout

def main():
    print("BENCHMARK - Comparacao de desempenho")
    print("Single-thread vs Multithread")
    print(f"Python: {PYTHON}")

    # Cenario 1: Cliente ST + Servidor ST
    rodar_cenario(
        "Cliente single-thread + Servidor single-thread",
        "server_st.py",
        "client_st.py"
    )

    # Cenario 2: Cliente ST + Servidor MT
    rodar_cenario(
        "Cliente single-thread + Servidor multithread",
        "server_mt.py",
        "client_st.py"
    )

    # Cenario 3: Cliente MT + Servidor MT
    rodar_cenario(
        "Cliente multithread + Servidor multithread",
        "server_mt.py",
        "client_mt.py"
    )

    print(f"\n{'='*60}")
    print("  BENCHMARK CONCLUIDO")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
