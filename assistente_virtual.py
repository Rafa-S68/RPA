import pyautogui
import pandas as pd
import time
from openpyxl import Workbook

def clicar (iconeNavegador):

    pyautogui.click(pyautogui.locateOnScreen(f'{iconeNavegador}.png'))

def digitar(texto):
    pyautogui.write(texto)

def pressionar_tecla(tecla):
    pyautogui.press(tecla)

def esperar(segundos):
    time.sleep(segundos)

def ler_arquivo(tarefas):
  
    return pd.read_csv(tarefas)

def executar_tarefas(df):
    tarefas_executadas = []
    for _, row in df.iterrows():
        tarefa = row['Tarefa']
        tipo = row['Tipo']
        dado = row['Dado']

        try:
            if tipo == 'click':
                clicar(dado)
            elif tipo == 'texto':
                digitar(dado) 
            elif tipo == 'tecla':
                pressionar_tecla(dado)
            elif tipo == 'espera':
                esperar(int(dado))

            status = 'Executada com sucesso'
        except Exception as e:
            status = f'Erro: {str(e)}'
        
        tarefas_executadas.append([tarefa, status, dado]) 
    return tarefas_executadas

def gerar_relatorio(tarefas_executadas):
    wb = Workbook()
    ws = wb.active
    ws.append(['Tarefa', 'Status', 'Tempo Estimado'])

    for tarefa in tarefas_executadas:
        ws.append(tarefa)

    wb.save("relatorio_tarefas.xlsx")

def main():
  
    df = ler_arquivo('tarefas.csv')
    
  
    tarefas_executadas = executar_tarefas(df)
    
  
    gerar_relatorio(tarefas_executadas)

if __name__ == "__main__":
    main()
