import tkinter as tk

window = tk.Tk()
window.title("tkinter 창 띄우기 예제")

window.geometry("300x300")

label = tk.Label(window, text="안녕하세요~")

button = tk.Button(window, text="버튼", command=lambda: print("버튼 클릭됨"))
button.pack()

window.mainloop()