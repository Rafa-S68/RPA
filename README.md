# AP02 – Extração de Dados, Armazenamento e Relatório

Este projeto é parte da Avaliação Prática 02 da disciplina de Robotic Process Automation (RPA). Ele realiza extração de dados de uma API, scraping de um site de livros e geração de um relatório em Excel com os dados processados.

## 🧩 Funcionalidades

- ✅ Extração de dados de países via [REST Countries API](https://restcountries.com)
- ✅ Web scraping de dados de livros no site [Books to Scrape](https://books.toscrape.com)
- ✅ Armazenamento dos dados em banco de dados SQLite
- ✅ Geração de relatório final em Excel com:
  - Dados dos países
  - Dados dos livros
  - Nome do aluno e data
  - Tabelas bem formatadas

---

## 🔧 Tecnologias utilizadas

- Python 3.11+
- Requests
- BeautifulSoup (bs4)
- SQLite3
- Openpyxl

## 📁 Estrutura

- 📁 dados/
  
├── paises.db
└── livraria.db

- 📁 relatorios/
└── relatorio_final.xlsx

- main.py
- extracao_paises.py
- webscraping_livros.py
- relatorio.py
- requirements.txt



---

## ▶️ Como Executar

1. Clone o repositório:

```bash

git clone https://github.com/Rafa-S68/RPA.git
cd RPA

 ## Instale os pacotes necessários:

 pip install -r requirements.txt

## Ou Execute o script principal: 

python main.py


📌 Observações

O relatório gerado será salvo automaticamente em relatorios/relatorio_final.xlsx.

Certifique-se de ter conexão com a internet para a extração via API.

Os dados extraídos do site são apenas para fins didáticos.

