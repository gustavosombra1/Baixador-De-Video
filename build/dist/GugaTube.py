import PySimpleGUI as sg
from pytube import YouTube
from os import link
sg.theme('DarkPurple6') 
layout = [  
            [sg.Text('Cole a URL do vídeo que deseja baixar:'), sg.InputText(key='link')],            
            # [sg.Text('Onde deseja salvar o arquivo?')],
            [sg.Button('BAIXAR VÍDEO'), sg.Button('BAIXAR ÁUDIO'), sg.Text('',key='nome')],
            # [sg.FileSaveAs(target=(-1, 0),key='path')],         
            [sg.Button('Cancel')]                            
]
# sg.In(),
window = sg.Window('GugaTube', layout)
while True:          
    event, values = window.read()
   
    link = values['link']
    # path = values['path']    
    yt = YouTube(link)
    nome = yt.title 
            
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break 

    if event =='BAIXAR VÍDEO':

        ys = yt.streams.get_highest_resolution()
        ys.download()

    if event =='BAIXAR ÁUDIO':

        ys = yt.streams.get_audio_only()
        ys.download()
        window['nome'].update(f'{nome} baixado com sucesso!')

window.close()