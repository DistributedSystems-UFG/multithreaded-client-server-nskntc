[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/yQPZ0SBC)

# Cliente-Servidor Multithread (ASR 05)

Nícolas Santana Kruger - 2022200545

## Descricao

Sistema cliente-servidor TCP com versoes single-thread e multithread para comparacao de desempenho.

### Operacoes do servidor

1. **Calculadora** - Operacoes aritmeticas (add, sub, mul, div)
2. **Fatorial** - Calcula fatorial de N
3. **Contar primos** - Conta primos ate N
4. **Verificar primo** - Verifica se N eh primo
5. **Reverter texto** - Inverte uma string

### Arquivos

| Arquivo | Descricao |
|---------|-----------|
| `constCS.py` | Constantes HOST e PORT |
| `operacoes.py` | Funcoes de processamento compartilhadas |
| `server_st.py` | Servidor single-thread |
| `server_mt.py` | Servidor multithread (1 thread por requisicao) |
| `client_st.py` | Cliente single-thread (requisicoes sequenciais) |
| `client_mt.py` | Cliente multithread (requisicoes em paralelo) |
| `benchmark.py` | Script de benchmark comparativo |

### Arquitetura

- **Servidor multithread**: a thread principal aceita conexoes. Ao receber uma conexao, dispara uma nova thread para processar a requisicao e enviar a resposta.
- **Cliente multithread**: cada requisicao eh enviada por uma thread diferente, permitindo envio em paralelo. As requisicoes sao geradas automaticamente com dados aleatorios.

### Como executar

**Teste manual:**
```
python server_mt.py          # Terminal 1
python client_mt.py          # Terminal 2
```

**Benchmark completo (3 cenarios):**
```
python benchmark.py
```

### Cenarios de benchmark

1. Cliente single-thread + Servidor single-thread
2. Cliente single-thread + Servidor multithread
3. Cliente multithread + Servidor multithread
