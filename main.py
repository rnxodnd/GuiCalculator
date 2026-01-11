from calculator import calculator

def main():
    cal = calculator()
    a = int(input())
    b = int(input())
    cal.set_a(a)
    cal.set_b(b)
    cal.add()
    print(cal.get_result())

if __name__ == '__main__':
    main()