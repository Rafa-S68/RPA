import os
import subprocess

def garantir_pastas():
    os.makedirs("dados", exist_ok=True)
    os.makedirs("relatorios", exist_ok=True)

def executar_script(nome_arquivo):
    print(f" Executando: {nome_arquivo}")
    subprocess.run(["python", nome_arquivo], check=True)

def main():
    print("AP02 - RPA")
    nome = input("Digite seu nome completo: ").strip()

    garantir_pastas()

    # Parte 1
    executar_script("extracao_paises.py")

    # Parte 2
    executar_script("webscraping_livros.py")

    # Parte 3
    print(f" Executando: relatorio.py")
    subprocess.run(["python", "relatorio.py", nome], check=True)

    print("\n Relatório gerado com sucesso na pasta 'relatorios/'.")

if __name__ == "__main__":
    main()
