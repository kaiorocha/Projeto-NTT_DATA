Descrição do WorkFlow:

Este arquivo é um workflow do GitHub Actions para um processo de CI/CD. Ele é acionado sempre que há um push na branch main, conforme solicitado na tarefa.O workflow foi divido em três jobs: build, deploy e notify.

Principais definições:

name: CI - NTT DATA

on:
 push:
   branches:
       - main

name: CI - NTT DATA
Descrição: Este é o nome do workflow.

on: push: branches: - main
Descrição: O workflow é acionado sempre que há um push (commit) na branch main.

Jobs:

jobs:
 build:
   runs-on: ubuntu-latest


Job: build
Descrição: Este job é responsável pela construção e validação do código.
runs-on: ubuntu-latest
Descrição: O job será executado em um ambiente Ubuntu com a versão mais recente
steps:
   - name: Clonar o código
     uses: actions/checkout@v2


   - name: Configurar o python
     uses: actions/setup-python@v2
     with:
       python-version: '3.9'



actions/checkout@v2
Descrição: Este passo usa a ação checkout para clonar o repositório e obter os arquivos necessários para o pipeline.
actions/setup-python@v2
Descrição: Esse passo configura a versão do python 3.9 no ambiente do runner. Ele usa a ação setup-python para garantir que a versão correta do Python esteja disponível.
- name: Instalar as dependêcias
     run: |
       python -m pip install --upgrade pip
       pip install -r requirements.txt


   - name: Run tests
     run: |
       pytest

run: |
    python -m pip install --upgrade pip
    pip install -r requirements.txt

Descrição: Aqui, o pip é atualizado para a versão mais recente e as dependências do projeto são instaladas a partir do arquivo requirements.txt, que lista as bibliotecas necessárias para o projeto Python.

run: |
    pytest

Descrição: Esse passo executa os testes do projeto usando o pytest, que é uma ferramenta de testes para Python. Ele irá garantir que o código não quebre e que tudo esteja funcionando corretamente.

- name: Criar artefato com resultados dos testes
     run: |
       mkdir -p artifact
       pytest > artifact/test_results.log
    
   - name: Fazer upload do artefato
     uses: actions/upload-artifact@v3
     with:
         name: test-results-artifact
         path: artifact/test_results.log

run: |
    mkdir -p artifact
    pytest > artifact/test_results.log

Descrição: O comando pytest é executado novamente, mas dessa vez com a saída redirecionada para o arquivo test_results.log. Este arquivo será usado como artefato.

uses: actions/upload-artifact@v3
  with:
      name: test-results-artifact
      path: artifact/test_results.log

Descrição: Aqui, o arquivo test_results.log é carregado como um artefato usando a ação upload-artifact. Isso permite que o arquivo de resultados dos testes seja preservado e acessado depois.

Deploy

deploy:
   runs-on: ubuntu-latest
   needs: build


runs-on: ubuntu-latest:

Descrição: O job também é executado em um ambiente Ubuntu.

needs: build:

O job deploy depende do sucesso do job build. Ou seja, o deploy só será executado se o job de build for concluído com sucesso.

