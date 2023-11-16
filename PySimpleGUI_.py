import PySimpleGUI as sg

#exibe todos os temas
# sg.theme_previewer()

#define o tema
sg.theme('Python')

#criando o layout
LAYOUT = [
  [sg.Text('Hello World!')],
  [sg.Text('Digite seu nome:'), sg.Input('', key='input', size=(15,0))],
  [sg.Button('CLIQUE')]
]

#definindo a janela
WINDOW = sg.Window('Título', LAYOUT)

#para deixar o programa sempre aberto
while True:
  events, values = WINDOW.read()
  
  if events == 'CLIQUE':
    sg.popup(f"Bem vindo! {values['input'].title()}")
  
  if events == sg.WINDOW_CLOSED:
    break
  
#fechando a janela e encerrando o programa
WINDOW.close()
