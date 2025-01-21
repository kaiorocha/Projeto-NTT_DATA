Documentação do Workflow de CI - NTT DATA

Este documento descreve o fluxo de trabalho de integração contínua (CI) configurado no GitHub Actions para o projeto NTT DATA.

Visão Geral

O fluxo de trabalho automatiza as seguintes etapas:

 - Clonagem do repositório.
 - Configuração do ambiente Python.
 - Instalação das dependências.
 - Execução de testes.
 - Geração de artefatos de teste.
 - Implantação na plataforma Vercel.
 - Envio de notificação por e-mail em caso de falha.

Gatilhos

 - Este workflow é acionado quando há um push para a branch main.

  Name: CI - NTT DATA
  
  on:
    push:
      branches:
          - main

Jobs

 - O workflow é composto por três jobs principais: build, deploy e notify.

  build

 - Este job realiza a construção e testes do projeto.

Etapas:

Clonar o repositório:

  - name: Clonar o código
  - uses: actions/checkout@v2

Configurar o Python:

  - name: Configurar o python
  - uses: actions/setup-python@v2
   - with:
     - python-version: '3.9'

Instalar dependências:

  - name: Instalar as dependências
   - run: |
     - python -m pip install --upgrade pip
     - pip install -r requirements.txt

Executar testes:

  - name: Run tests
   - run: |
     - pytest

Gerar artefatos:

  - name: Criar artefato com resultados dos testes
   - run: |
     - mkdir -p artifact
     - pytest > artifact/test_results.log

Upload dos artefatos:
  
  - name: Fazer upload do artefato
   - uses: actions/upload-artifact@v3
   - with:
       - name: test-results-artifact
       - path: artifact/test_results.log

deploy

 - Este job realiza a implantação do projeto na Vercel após a execução bem-sucedida do job build.

Etapas:

 - Instalar o Vercel:

  - name: Instalando o vercel
   - run: npm install --global vercel

 - Realizar deploy:

  - name: Deploy
   - run: vercel deploy --yes --token=${{secrets.TOKEN_VERCEL}} --name my-project

notify

 - Este job é executado apenas em caso de falha nos jobs anteriores.

Etapas:

 - Enviar e-mail de notificação:

  - name: Enviar e-mail de notificação
   - uses: dawidd6/action-send-mail@v3
   - with:
     - server_address: smtp.gmail.com
     - server_port: 587
     - username: ${{ secrets.EMAIL_USERNAME }}
     - password: ${{ secrets.EMAIL_PASSWORD }}
     - subject: 'CI Pipeline Status'
     - body: 'CI Pipeline Failed'
     - to: ${{vars.VAR_EMAIL}}
     - from: 'ci-notifications@gmail.com'

Variáveis e Segredos

TOKEN_VERCEL: Token de autenticação para a Vercel.

EMAIL_USERNAME: Endereço de e-mail utilizado para envio de notificações.

EMAIL_PASSWORD: Senha do e-mail para envio.

VAR_EMAIL: Endereço de e-mail do destinatário das notificações.

Execução

Para executar este fluxo de trabalho, basta fazer um push na branch main do repositório. O GitHub Actions iniciará automaticamente os jobs definidos.

Caso ocorra uma falha, um e-mail será enviado para o destinatário especificado nas variáveis de ambiente.

Essa documentação fornece uma visão detalhada do pipeline de CI, garantindo que todos os envolvidos compreendam o fluxo de trabalho e os processos envolvidos.
Para executar este fluxo de trabalho, basta fazer um push na branch main do repositório. O GitHub Actions iniciará automaticamente os jobs definidos.

Caso ocorra uma falha, um e-mail será enviado para o destinatário especificado nas variáveis de ambiente.

Essa documentação fornece uma visão detalhada do pipeline de CI, garantindo que todos os envolvidos compreendam o fluxo de trabalho e os processos envolvidos.

