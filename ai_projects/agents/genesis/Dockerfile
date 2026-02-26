# Dockerfile para o Agente Gênesis

# Usar uma imagem base oficial do Python para Ubuntu
FROM python:3.12-slim-bookworm

# Definir diretório de trabalho no contêiner
WORKDIR /app

# Copiar os arquivos do agente para o contêiner
COPY . /app

# Instalar as dependências do Python
# Nossos agentes usarão o OpenClaw, então instalaremos (exemplo)
# Futuras dependências específicas do Gênesis virão aqui
# Instalar build-essential e outras ferramentas necessárias para compilação caso haja dependências binárias
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir openclaw

# Comando padrão a ser executado quando o contêiner iniciar
# Isso pode ser um script Python que inicializa o agente
CMD ["python", "genesis_entrypoint.py"]
