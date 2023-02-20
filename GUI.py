import PySimpleGUI as sg
import pages.home as home


win1, win2 = home.home_page(), None

while True:
    window, event, values = sg.read_all_windows()

    #-----------window1----------------
    if window == win1 and event == sg.WIN_CLOSED:
        break

    elif window == win2 and event == sg.WIN_CLOSED:
        win2.close()
