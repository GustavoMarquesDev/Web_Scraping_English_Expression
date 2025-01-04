# Web Scraping Script

Este é um script simples para realizar raspagem de dados de uma página da web. Ele coleta informações específicas de uma URL fornecida e exibe ou salva os dados conforme necessário.

## Funcionalidades

- Faz requisições HTTP para páginas da web.
- Extrai informações específicas utilizando seletores de HTML.
- Salva os dados em um arquivo de texto.

## Requisitos

Antes de executar o script, certifique-se de que os seguintes requisitos estão instalados:

- Python 3.7 ou superior
- É recomendavel criar seu ambiente virtual:
  - python -m venv venv
  - .\venv\Scripts\activate
- Bibliotecas Python necessárias (instaladas via `pip`):
  - `requests`
  - `beautifulsoup4`

## Instalação

1. Clone este repositório ou copie os arquivos para o seu ambiente local:

   ```bash
   git clone https://github.com/GustavoMarquesDev/Web_Scraping_English_Expression
   cd Web_Scraping_English_Expression
   pip install -r requirements.txt

