import time
# from tkinter import *  # коллизия имён!!!
import tkinter
import threading

slider_widget = None


def start():
    slider_value = 1
    global slider_widget
    if slider_widget is not None:
        slider_value = slider_widget.get()
    for i in range(slider_value):
        print(f"Файл №{i+1} сохранен")
        file = open(f"tmp/file_{i+1}.txt", 'w')
        file.write(f"File number {i+1}")
        file.close()
        time.sleep(0.1)
    quit()


def start_thread():
    new_thread = threading.Thread(target=start)
    new_thread.start()

    # with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
    #     executor.submit(start)


def create_ui():
    tkinter_ui_window = tkinter.Tk()
    label_time = tkinter.Label(tkinter_ui_window, text="HW30", fg="#eee", bg="#333")
    label_time.place(x=0, y=0)
    btn_start = tkinter.Button(tkinter_ui_window, text="GO", fg='blue', command=start_thread)
    btn_start.place(x=0, y=50)
    # btn_reset = tkinter.Button(tkinter_ui_window, text="reset", fg='yellow', command=reset)
    # btn_reset.place(x=0, y=100)
    # btn_pause = tkinter.Button(tkinter_ui_window, text="pause", fg='green', command=pause)
    # btn_pause.place(x=0, y=150)
    slider = tkinter.Scale(tkinter_ui_window, from_=1, to=1000, orient=tkinter.HORIZONTAL, length=500)
    slider.place(x=0, y=100)

    global slider_widget
    slider_widget = slider

    print(slider.get())

    # lbl = Label(window, text="This is Label widget", fg='red', font=("Helvetica", 16))
    # lbl.place(x=60, y=50)
    # txtfld = Entry(window, bd=5)
    # txtfld.place(x=80, y=150)
    tkinter_ui_window.title('HW30')
    tkinter_ui_window.geometry("640x480+10+10")
    tkinter_ui_window.mainloop()


if __name__ == '__main__':
    create_ui()
    # start()
