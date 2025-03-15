# Mapa de Calor Interativo

## Descrição

Este é um aplicativo web desenvolvido com Streamlit que gera mapas de calor interativos a partir de dados fornecidos pelo usuário. Ele permite visualizar diferentes decks de uma estrutura e personalizar a paleta de cores para melhor interpretação dos dados.

## Funcionalidades

- Upload de arquivo Excel contendo os dados.

- Seleção de diferentes decks para visualização.

- Escolha da paleta de cores para o mapa de calor.

- Geração automática do mapa de calor com sobreposição de valores.

## Como Executar Localmente

### 1. Clone o Repositório

```git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio```

### 2. Crie e Ative um Ambiente Virtual

```python -m venv venv
# No Windows
venv\Scripts\activate
# No Linux/Mac
source venv/bin/activate```

### 3. Instale as Dependências

```pip install -r requirements.txt```

### 4. Execute a Aplicação

```streamlit run app.py```

## Como Usar

Acesse a aplicação através do navegador.

Faça o upload do arquivo Excel no formato esperado.

Escolha o deck desejado na barra lateral.

Selecione a paleta de cores para melhor visualização.

O mapa de calor será gerado automaticamente com os valores sobrepostos.

## Estrutura do Projeto

```/mapa-de-calor
│── app.py
│── requirements.txt
│── README.md
│── /data (se necessário para arquivos de exemplo)
└── /images (se necessário para mapas de fundo)```

## Deploy na Web

A aplicação pode ser hospedada no Streamlit Community Cloud seguindo os passos:

Publique o repositório no GitHub.

Acesse o Streamlit Community Cloud e conecte o repositório.

Configure o arquivo ```app.py``` como entrada.

Realize o deploy e compartilhe o link gerado.

## Tecnologias Utilizadas

- Python

- Streamlit

- Pandas

- Matplotlib

- NumPy

- Pillow

## Contribuição

Sugestões e melhorias são bem-vindas! Para contribuir, faça um fork do projeto, crie uma branch, implemente as alterações e envie um pull request.

## Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.
