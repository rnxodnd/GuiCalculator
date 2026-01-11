import tkinter as tk
from calculator import calculator

cal = calculator()
cal.set_a(1)
cal.set_b(3)

window = tk.Tk()
window.title("계산기")

window.geometry("500x650")

label = tk.Label(window, text="안녕하세요", fg="black" )
label.pack()

setted_a = tk.Label(window,  text="a", fg="black" )
setted_a.pack(side = "top")

setted_b = tk.Label(window, text="b", fg="black")
setted_b.pack(side = "top")
#label 가로 배치

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