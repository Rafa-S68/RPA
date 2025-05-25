# 📌 AP1 - RPA: Projeto de Automação com Python

## 🧠 Objetivo Geral

Este projeto tem como objetivo desenvolver um **assistente virtual automatizado** utilizando Python. O assistente é capaz de **ler tarefas de um arquivo**, interpretá-las e **executá-las automaticamente**, simulando ações humanas no computador — como cliques, digitação, comandos de teclado e pausas.

---

## ⚙️ Funcionalidades

- 📄 **Leitura de tarefas** a partir de um arquivo `.csv` ou `.xlsx`
- 🧠 **Interpretação de instruções** com base no tipo da tarefa (clique, digitação, tecla, espera, etc.)
- 🤖 **Automação de teclado e mouse** com `pyautogui`
- 🧩 **Código modularizado** com funções reutilizáveis
- 📊 **Geração de relatório em Excel** com resumo das tarefas executadas

---

## 🧪 Exemplo de Arquivo de Tarefas

```csv
Tarefa,Tipo,Dado
Abrir navegador,click,navegador_icone
Digitar site,texto,www.exemplo.com
Pressionar Enter,tecla,enter
Esperar,espera,5
```

---

## 📋 Relatório Gerado

Ao final da execução, é gerado automaticamente um **relatório em Excel**, contendo:

- ✅ Tarefa realizada
- 📌 Status (sucesso ou falha)
- ⏱️ Tempo estimado de execução

---

## 🛠️ Tecnologias Utilizadas

- [Python 3.x](https://www.python.org/)

- [`pyautogui`](https://pypi.org/project/PyAutoGUI/) — automação de teclado e mouse

- [`pandas`](https://pandas.pydata.org/) — leitura de arquivos CSV/Excel

- [`openpyxl`](https://openpyxl.readthedocs.io/) — geração de relatórios em Excel


## 📍 Observações

- O script simula ações reais, então **não mexa no computador** durante a execução.
- Use a função `pyautogui.position()` para capturar coordenadas dos elementos na tela.

---
