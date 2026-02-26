# genesis_entrypoint.py para o Agente Gênesis

import os

if __name__ == '__main__':
    print("--------------------------------------------------")
    print("Agente Gênesis Iniciado!")
    print("--------------------------------------------------")
    print(f"Diretório de Trabalho: {os.getcwd()}")
    print("Pronto para criar e gerenciar outros agentes.")
    print("Para parar o Gênesis, use Ctrl+C ou docker stop.")
    # Aqui viria a lógica principal do Agente Gênesis
    # Por exemplo, um loop para receber comandos, criar sub-agentes, etc.
    while True:
        try:
            # Manter o agente rodando para que o contêiner não saia imediatamente
            # Esta lógica será expandida quando o Gênesis for implementado de fato
            pass
        except KeyboardInterrupt:
            print("Agente Gênesis encerrado por comando do usuário.")
            break
        except Exception as e:
            print(f"Erro no Agente Gênesis: {e}")
        time.sleep(5) # Evitar que o loop consuma 100% da CPU sem fazer nada
