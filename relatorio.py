import sqlite3
from openpyxl import Workbook
from datetime import datetime
import os

def obter_dados_paises():
    conn = sqlite3.connect("dados/paises.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM paises")
    colunas = [desc[0] for desc in cursor.description]
    dados = cursor.fetchall()
    conn.close()
    return colunas, dados

def obter_dados_livros():
    conn = sqlite3.connect("dados/livraria.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM livros")
    colunas = [desc[0] for desc in cursor.description]
    dados = cursor.fetchall()
    conn.close()
    return colunas, dados

def gerar_relatorio_excel(nome_aluno):
    wb = Workbook()

    
    ws_paises = wb.active
    ws_paises.title = "Paises"
    col_paises, dados_paises = obter_dados_paises()
    ws_paises.append(["Aluno:", nome_aluno, "", "Data:", datetime.today().strftime("%d/%m/%Y")])
    ws_paises.append([])  
    ws_paises.append(col_paises)
    for linha in dados_paises:
        ws_paises.append(list(linha))

    
    ws_livros = wb.create_sheet("Livros")
    col_livros, dados_livros = obter_dados_livros()
    ws_livros.append(col_livros)
    for linha in dados_livros:
        ws_livros.append(list(linha))

    os.makedirs("relatorios", exist_ok=True)
    caminho_saida = "relatorios/relatorio_final.xlsx"
    wb.save(caminho_saida)
    print(f" Relatório gerado com sucesso em '{caminho_saida}'")

if __name__ == "__main__":
    nome_aluno = input("Digite seu nome completo para o relatório: ")
    gerar_relatorio_excel(nome_aluno)
