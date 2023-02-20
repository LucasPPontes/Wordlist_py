import PySimpleGUI as sg

def home_page():

    sg.theme("Black")

    layout = [
        [sg.Image(filename="img/capa.png",size=(500,300))],
        [sg.Button("Gerar wordlist",key="wordlist"),sg.Button("Criptografar um arquivo",key="criptografia"),sg.Button("Coletar ip de um site",key="pegar_ip")]
    ]
    return sg.Window("Hacker Tools", layout=layout, finalize=True, size=(550,500))
