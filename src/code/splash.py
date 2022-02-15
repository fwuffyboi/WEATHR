def splash():
    import PySimpleGUI as sg
    from PIL import Image
    import os, io

    sg.theme('Black')
    layout = [
        [sg.Image("", key="-SSI-", data="", enable_events=True, size=("720", "480"))],
        [sg.Button("Quit", key="-QT-", button_color="black", size=("50", "480"))],
    ]

    window = sg.Window('Loading WEATHR', layout, grab_anywhere=True, no_titlebar=True, keep_on_top=True)
    imgNo = 1

    while True:  # Event Loop
        event, values = window.read(timeout=20)
        
        dontShowEOVList = ["__TIMEOUT__" or "" or ""]
        
        if event or values not in dontShowEOVList:
            print(f"EVENT://  {event}")
            print(f"VALUES:// {values}\n\n")


        if event in (sg.WIN_CLOSED, 'Exit', 'Esc'):
            break

        elif event == "-SSI-":
            print("User event on button/image, breaking...")
            break

        filepath = str((os.getcwd() + "\png\\" + str(imgNo) + ".jpg"))
        image = Image.open(fp=rf"I:\PROGRAMMING\currentProjects\wthr2\src\logos\pngs\frame{imgNo}.png")
        image.thumbnail((720, 480))
        bio = io.BytesIO()
        image.save(bio, format="PNG")
        window["-SSI-"].update(data=bio.getvalue())
        imgNo += 1

        if imgNo == 75:
            imgNo = 1

    window.close()


splash()
