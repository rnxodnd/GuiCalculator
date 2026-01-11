import tkinter as tk
from calculator import calculator

cal = calculator()
cal.a = None
cal.b = None

window = tk.Tk()
window.title("계산기")

window.geometry("500x650")

label_frame = tk.Frame(window)
label_frame.pack(side="top", pady=20)


setted_a = tk.Label(label_frame,  text="a", fg="black" )
setted_a.pack(side="left", padx = 10)

divider = tk.Label(label_frame, text=" ")
divider.pack(side="left")

setted_b = tk.Label(label_frame, text="b", fg="black")
setted_b.pack(side="left", padx=10)

label = tk.Label(label_frame, text="result", fg="black")
label.pack(side="left", padx=10)

def on_click():
    cal.add() # 계산기 인스턴스의 값 변경
    new_value = cal.get_result() # 변경된 값 가져오기
    label.config(text=new_value) # Label의 텍스트 업데이트
    # log
    print(f"a={cal.a}, b={cal.b}, res={cal.result}")

button = tk.Button(window, padx=10, pady=10, text="1", command=lambda: print(cal.get_result()))
button.pack()

button10 = tk.Button(window, text="=", command=lambda: on_click())
button10.pack()

cal.set_b(0)
button_list = []

def set_num(n : int):
    num = n
    if cal.a == None:
        cal.set_a(num) 
        setted_a.config(text=num)
    else:
        cal.set_b(num)
        setted_b.config(text=num)
   

for i in range(10):
    but = tk.Button(window, text=f"{i}", 
                    command=lambda i=i: set_num(i))
    but.pack()
    button_list.append(but)


window.mainloop()