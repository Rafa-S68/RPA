import requests
from bs4 import BeautifulSoup
import sqlite3

def criar_tabela():
    conn = sqlite3.connect("dados/livraria.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS livros (
            titulo TEXT,
            preco TEXT,
            avaliacao TEXT,
            disponibilidade TEXT
        )
    """)
    conn.commit()
    conn.close()

def extrair_dados_livros():
    url = "https://books.toscrape.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    livros = soup.select("article.product_pod")[:10]
    lista_livros = []

    for livro in livros:
        titulo = livro.h3.a['title']
        preco = livro.select_one(".price_color").text
        disponibilidade = livro.select_one(".availability").text.strip()
        
        classe_avaliacao = livro.select_one("p.star-rating")["class"]
        estrelas = classe_avaliacao[1] if len(classe_avaliacao) > 1 else "N/A"

        lista_livros.append((titulo, preco, estrelas, disponibilidade))
    
    return lista_livros

def salvar_no_banco(livros):
    conn = sqlite3.connect("dados/livraria.db")
    cursor = conn.cursor()
    cursor.executemany("""
        INSERT INTO livros (titulo, preco, avaliacao, disponibilidade)
        VALUES (?, ?, ?, ?)
    """, livros)
    conn.commit()
    conn.close()

def main():
    criar_tabela()
    livros = extrair_dados_livros()
    salvar_no_banco(livros)
    print("Dados dos livros salvos com sucesso!")

if __name__ == "__main__":
    main()
