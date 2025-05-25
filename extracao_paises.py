import requests
import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "dados", "paises.db")

def criar_tabela():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS paises (
            nome_comum TEXT,
            nome_oficial TEXT,
            capital TEXT,
            continente TEXT,
            regiao TEXT,
            sub_regiao TEXT,
            populacao INTEGER,
            area REAL,
            moeda_nome TEXT,
            moeda_simbolo TEXT,
            idioma TEXT,
            fuso_horario TEXT,
            url_bandeira TEXT
        )
    """)
    conn.commit()
    conn.close()

def limpar_tabela_paises():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM paises")
    conn.commit()
    conn.close()

def inserir_dados(pais):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO paises VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, pais)
    conn.commit()
    conn.close()

def buscar_dados_pais(nome):
    url = f"https://restcountries.com/v3.1/name/{nome}"
    response = requests.get(url)
    if response.status_code == 200:
        try:
            data = response.json()[0]

            nome_comum = data["name"]["common"]
            nome_oficial = data["name"]["official"]
            capital = data.get("capital", ["N/A"])[0]
            continente = data.get("continents", ["N/A"])[0]
            regiao = data.get("region", "N/A")
            sub_regiao = data.get("subregion", "N/A")
            populacao = data.get("population", 0)
            area = data.get("area", 0.0)
            moedas = list(data.get("currencies", {}).values())
            moeda_nome = moedas[0]["name"] if moedas else "N/A"
            moeda_simbolo = moedas[0]["symbol"] if moedas else "N/A"
            idiomas = list(data.get("languages", {}).values())
            idioma = idiomas[0] if idiomas else "N/A"
            fuso_horario = data.get("timezones", ["N/A"])[0]
            url_bandeira = data.get("flags", {}).get("png", "N/A")

            return (
                nome_comum, nome_oficial, capital, continente, regiao,
                sub_regiao, populacao, area, moeda_nome, moeda_simbolo,
                idioma, fuso_horario, url_bandeira
            )
        except Exception as e:
            print(f"Erro ao processar dados do país '{nome}': {e}")
    else:
        print(f"Erro ao buscar dados do país '{nome}': {response.status_code}")
    return None

def main():
    criar_tabela()
    limpar_tabela_paises()  
    
    print("Digite o nome de 3 países separados por vírgula (ex: Brasil, Japão, Alemanha):")
    entrada = input().strip()
    lista_paises = [p.strip() for p in entrada.split(",") if p.strip()]
    if len(lista_paises) < 3:
        print("Você deve informar pelo menos 3 países.")
        return
    lista_paises = lista_paises[:3]

    for nome_pais in lista_paises:
        dados = buscar_dados_pais(nome_pais)
        if dados:
            inserir_dados(dados)
            print(f"Dados de '{nome_pais}' inseridos com sucesso.\n")
        else:
            print(f"Não foi possível obter dados para '{nome_pais}'.\n")

if __name__ == "__main__":
    main()
