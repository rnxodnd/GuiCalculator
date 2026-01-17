import tkinter as tk
from calculator import calculator

cal = calculator()
cal.a = None
cal.b = None
cal.op = None

window = tk.Tk()
window.title("계산기")
window.geometry("550x500")

# ===== 상단 표시 영역 =====
label_frame = tk.Frame(window)
label_frame.pack(side="top", pady=20)

setted_a = tk.Label(label_frame, text="a", fg="black")
setted_a.pack(side="left", padx=10)

divider = tk.Label(label_frame, text="+")
divider.pack(side="left")

setted_b = tk.Label(label_frame, text="b", fg="black")
setted_b.pack(side="left", padx=10)

label = tk.Label(label_frame, text="result", fg="black")
label.pack(side="left", padx=10)

# ===== 기능 =====
# 계산 후 a,b 초기화
def reset():
    cal.a = None
    cal.b = None
    cal.op = None
    setted_a.config(text="a")
    setted_b.config(text="b")
    divider.config(text = " ")

def set_op(new_op: str):
    cal.op = new_op
    divider.config(text=f"{cal.op}")

def reset_all():
    cal.a = None
    cal.b = None
    cal.op = None
    if hasattr(cal, "result"):
        cal.result = None

    setted_a.config(text="a")
    setted_b.config(text="b")
    label.config(text="result")

def set_num(n: int):
    if cal.a is None:
        cal.set_a(n)
        setted_a.config(text=str(n))
    else:
        cal.set_b(n)
        setted_b.config(text=str(n))

# ===== 버튼 영역 (grid) =====
btn_frame = tk.Frame(window)
btn_frame.pack(pady=20)

btn_opts = dict(width=10, height=3)

layout = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["초기화", "0", "=", "+"],
]

def on_button(text: str):
    if text.isdigit():
        set_num(int(text))
    elif text in {"+", "-", "*", "/"}:
        set_op(text)
    elif text == "=":
        on_click()
    elif text == "초기화":
        reset_all()

for r, row in enumerate(layout):
    for c, text in enumerate(row):
        tk.Button(
            btn_frame,
            text=text,
            command=lambda t=text: on_button(t),
            **btn_opts
        ).grid(row=r, column=c, padx=5, pady=5)

window.mainloop()