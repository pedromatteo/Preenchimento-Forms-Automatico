# Preenchimento de Forms Automático (PyAutoGUI + Planilha → Formulário Online)

Este projeto automatiza o preenchimento de um formulário online usando Python e PyAutoGUI. O script lê uma planilha com os dados necessários e os insere automaticamente no formulário, simulando interações humanas de teclado e mouse.

## 📌 Objetivo do Projeto

Automatizar tarefas repetitivas e reduzir erros manuais ao preencher formulários online. Útil para cadastros, listas de presença, inscrições e qualquer processo que tenha grande volume de dados.

## 🚀 Funcionalidades

* Leitura automática de uma planilha (Excel ou CSV)
* Navegação até o formulário online
* Preenchimento automático dos campos: nome, e-mail, telefone, curso, turno etc.
* Simulação de teclas e cliques com PyAutoGUI
* Delay configurado para compatibilidade com computadores mais lentos

## 🛠 Tecnologias Utilizadas

* **Python 3**
* **PyAutoGUI** — Automação da interface gráfica
* **Webbrowser**
* **Google Sheets** (fonte dos dados)
* **Google Forms** (destino dos dados)

## 📂 Estrutura do Projeto

```
/Projeto-Forms-Automatico
│
├── main.py        # Script principal de automação
└── README.md      # Este arquivo
```

- Funções separadas para cada turno:
  - `turno_tarde()` → Preenche o formulário para o turno da tarde
  - `turno_manha()` → Preenche o formulário para o turno da manhã
  - `turno_noite()` → Preenche o formulário para o turno da noite


## 📥 Pré-requisitos

Certifique-se de ter instalado:

```bash
pip install pyautogui
```

## ▶️ Como Usar

1. Abra a planilha e preencha os dados corretamente.
2. Coloque o link do formulário no código.
3. Execute o script:

```bash
python main.py
```

4. Não mova o mouse durante a automação.

## ⚠️ Observações Importantes

* Ajuste os intervalos de tempo (sleep) conforme a velocidade do seu PC.
* Mantenha o navegador sem zoom (100%) para evitar erros de posição.
* Execute em tela cheia para resultados mais consistentes.

## 📚 Aprendizado

Este projeto foi desenvolvido como forma de estudo em:

* Automação básica com Python
* Organização de código
* Melhores práticas de iniciantes
* Manipulação de planilhas e formulários

📝 Notas

Algumas partes do código foram refatoradas com ajuda de IA para fins de estudo e boas práticas.

## 📄 Licença

Este projeto é de uso livre para estudo e melhorias.

Pedro Simplicio.