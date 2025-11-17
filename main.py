import pyautogui as py
import webbrowser as web


def copiar_colar():
    py.hotkey('ctrl', 'tab')
    py.press('right')
    py.hotkey('ctrl', 'c')
    py.sleep(1)

    py.hotkey('ctrl', 'tab')
    py.sleep(1)
    py.press('tab')
    py.hotkey('ctrl', 'v')
    py.sleep(1)


def preencher_form(turno_x, turno_y):
    # Copiar nome
    py.hotkey('ctrl', 'c')
    py.sleep(1)
    py.hotkey('ctrl', 'tab')
    py.sleep(1)

    # Campo do Nome
    py.click(813, 230)
    py.hotkey('ctrl', 'v')
    py.sleep(1)

    # E-mail, telefone e curso
    copiar_colar()
    copiar_colar()
    copiar_colar()

    # Turno
    py.click(turno_x, turno_y)

    # Meu nome
    py.press('tab')
    py.write("Pedro Simplicio", interval=0.2)
    py.sleep(2)

    # Enviar
    py.press('tab')
    py.press('enter')
    py.sleep(2)
    py.press('tab')
    py.press('enter')
    py.sleep(2)

    # Voltar para a planilha
    py.hotkey('ctrl', 'tab')
    py.sleep(2)

    # Voltar para o começo da linha
    for _ in range(3):
        py.press('left')
        py.sleep(0.2)

    py.press('down')
    py.sleep(2)


def turno_tarde():
    preencher_form(816, 552)


def turno_manha():
    preencher_form(818, 529)


def turno_noite():
    preencher_form(817, 572)


#  INÍCIO #

# Abrir planilha
web.open('https://docs.google.com/spreadsheets/d/1dFXu7slgDT5LGk2FLsPnZUe1HY30je9EV4LMPuwb8nU/edit?usp=sharing  ana.nogueira12@example.com')
py.sleep(2)

# Abrir formulário
web.open('https://forms.gle/4pf5FWSWxPH7A8rs6')
py.sleep(2)

# Zoom (afastando)
for _ in range(5):
    py.hotkey('ctrl', '-')
    py.sleep(0.2)

py.sleep(2)

# Voltar para planilha
py.hotkey('ctrl', 'tab')
py.sleep(2)

# Descer para primeira linha
py.press('down')

# Execução das funções
for _ in range(3):
    turno_tarde()
    py.sleep(2)

turno_noite()
py.sleep(2)

turno_tarde()
py.sleep(2)

for _ in range(2):
    turno_manha()
    py.sleep(2)

for _ in range(3):
    turno_noite()
    py.sleep(2)

turno_tarde()

print("Sucesso!")