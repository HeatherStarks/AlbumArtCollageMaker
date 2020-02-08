import PySimpleGUI as sg
from funcs import *

ratio_vals = [(1,1),(5,6),(4,5),(3,4),(1,2),(2,3),(9,16),(8,11)]

frame_layout = [
                  [sg.Checkbox("Perfect Ratio",key="perfect",enable_events=True), sg.Checkbox("Reverse Ratio",key="reverse",enable_events=True), sg.Text("Desired Ratio:"), sg.Combo(ratio_vals,default_value=ratio_vals[0],key="ratio")],
                  [sg.Radio('Stretch',1,disabled=True, key="stretch",enable_events=True), sg.Radio('Fill Spaces',1,disabled=True, key="fill", default=True,enable_events=True)],
                  [sg.Text("Color Sort Method:"),sg.Radio('RGB',2, key="RGB",default=True,enable_events=True), sg.Radio('HSV',2, key="HSV",enable_events=True)],
                  [sg.Text("Subimage Size (px):"),sg.Slider(range = (1,500), key="subsize", orientation="horizontal",disable_number_display=True,enable_events=True), sg.InputText("001",key="sizeread")]
               ]

layout = [[sg.FolderBrowse("Browse Input Folder"), sg.Input(key='FilePathIn',default_text="C:\\")],
          [sg.FolderBrowse("Browse Output Folder"), sg.Input(key='FilePathOut',default_text="C:\\")],
          [sg.Text("Output File Name (No Extention):"), sg.InputText("untitled", key="name")],
          [sg.Text("Output Format:"), sg.Radio('PNG',3, key="PNG",default=True,enable_events=True), sg.Radio('JPG',3, key="JPG",enable_events=True)],
          [sg.Frame("Options", frame_layout)],
          [sg.Button('Run'), sg.Button('Exit')]]

window = sg.Window('Collage Maker', layout)

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        break
    if event == 'perfect':
        if values['perfect']:
            window.FindElement("stretch").Update(disabled=True) # change back to Falsw when stretch is working
            window.FindElement("fill").Update(disabled=False)
        elif not values['perfect']:
            window.FindElement("stretch").Update(disabled=True)
            window.FindElement("fill").Update(disabled=True)
    if event == 'subsize':
        window.FindElement("sizeread").Update(str(int(values["subsize"])))
    
    # Read Data:
    if values['RGB'] == True:
        SORT_METHOD = "RGB"
    else:
        SORT_METHOD = "HSV"

    if values['stretch'] == True:
        RATIO_METHOD = "stretch"
    else:
        RATIO_METHOD = "fill"

    if values['JPG'] == True:
        FORMAT = "JPG"
    else:
        FORMAT = "PNG"

    SUB_SIZE = int(values['subsize'])

    RATIO = tuple(values['ratio'])

    if values["reverse"] == True:
        temp = RATIO[0]
        RATIO[0] = RATIO[1]
        RATIO[1] = temp

    INPUT_FOLDER = values['FilePathIn']

    OUTPUT_FOLDER = values['FilePathOut']

    NAME = values['name']
    
    PERFECT = values['perfect']


    # Run:

    if event == 'Run':
        create_image(INPUT_FOLDER,OUTPUT_FOLDER,NAME,SORT_METHOD,RATIO,PERFECT,RATIO_METHOD,SUB_SIZE,FORMAT)



window.close()