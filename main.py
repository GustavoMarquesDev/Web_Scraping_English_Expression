# type: ignore
from pathlib import Path
import requests
from bs4 import BeautifulSoup

# Configurações de pastas
ROOT_FOLDER = Path(__file__).parent
TEXT_FOLDER = ROOT_FOLDER / 'most_used_expressions.txt'

# URL do site
URL = 'https://www.ccaa.com.br/blog/expressoes-em-ingles/'
response = requests.get(URL)

# Verifique se a requisição foi bem-sucedida
if response.status_code == 200:
    raw_html = response.content.decode('utf-8')
    parsed_html = BeautifulSoup(raw_html, 'html.parser', from_encoding='utf-8')

    # Verifique se o seletor '.text-field' existe no HTML
    most_used_expressions = parsed_html.select_one('.text-field')

    if most_used_expressions:
        # Variável para acumular o texto formatado
        formatted_text = ""

        # Iterar sobre os filhos diretos
        for element in most_used_expressions.children:
            # Se for <h3>, adicionar como título
            if element.name == 'h3':  # type: ignore
                formatted_text += f"\n{element.text.strip()}\n"
            # Se for <p>, adicionar como descrição
            elif element.name == 'p':
                formatted_text += f"{element.text.strip()}\n"

        # Salvar no arquivo .txt
        with open(TEXT_FOLDER, "w", encoding="utf-8") as arquivo:
            arquivo.write(formatted_text)

        print(f"Texto salvo em: {TEXT_FOLDER}")
    else:
        print("Elemento com a classe '.text-field' não encontrado.")
else:
    print(f"Erro ao acessar a URL: {response.status_code}")
