# 계산기 class 만들기
# 멤버 변수: 정수 a와 b, 이전 계산 결과 변수
# 멤버 메서드: 사칙연산 4개 하나씩, 이전 결과 반환 함수

class calculator:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.result = 0

    def add(self):
        self.result = self.a + self.b
    
    def minus(self):
        self.result = self.a - self.b

    def mul(self):
        self.result = self.a * self.b

    def div(self):
        self.result = self.a / self.b

    def get_result(self):
        return self.result
    
    def set_a(self, a):
        self.a = a

    def set_b(self, b):
        self.b = b



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

