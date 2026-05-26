# # 클래스(객체를 만들기 위한 틀(설계도)) 문법

# # 붕어빵 클래스
# class FishBread:        # 클래스 선언 # 클래스명은 첫 글자 대문자로 하자!
#     # 속성(affribute)
#     def __init__(self, f, b):     # __init__은 클래스로부터 객체를 생성해주는 메소드, 약속이자 원칙(객체 초기화) 첫번째 매개변수를 self로 하자.
#         self.flour = f            # self는 객체 메모리 안의 변수로 만들어주기 위해 쓰는 것
#         self.bean = b             # ex) flour와 bean은 FishBread 꺼야!

#     # 기능(function, method)
#     def makeFishBread(self):      # FishBread 자체 기능이라고 정의하기 위해 self를 매개변수로 쓴다.
#         print('붕어빵 제조')

# # 붕어빵 클래스로부터 객체를 만들기. (객체 생성)
# myFishBread = FishBread('팥', '밀가루')     # 붕어빵 안에는 팥이 있고 반죽은 밀가루이다. (기본값 입력)
# friendFishBread = FishBread('슈크림', '쌀') # 친구 붕어빵 안에는 슈크림이 있고 반죽은 쌀반죽이다. 같은 클래스여도 객체가 분리되어있음 형은 형이고 나는 나.
# hisFishBread = FishBread('팥슈 반반', '밀가루')

# print(f'내 붕어빵의 속 내용물: {myFishBread.flour}')
# print(f'내 붕어빵의 반죽: {myFishBread.bean}')
# print(f'친구 붕어빵의 속 내용물: {friendFishBread.flour}')
# print(f'친구 붕어빵의 반죽: {friendFishBread.bean}')
# print(f'아저씨의 속 내용물: {hisFishBread.flour}')
# print(f'아저씨의 반죽: {hisFishBread.bean}')

# # 계산기 클래스
# class Calculator:
#     # 속성
#     def __init__(self, n1, n2):
#         self.num1 = n1
#         self.num2 = n2

#     # 기능(function, method)
#     def add(self):
#         print(f'add: {self.num1 + self.num2}')

#     def sub(self):
#         print(f'sub: {self.num1 - self.num2}')

#     def mul(self):
#         print(f'mul: {self.num1 * self.num2}')

#     def div(self):
#         print(f'div: {self.num1 / self.num2}')

# myCalculator = Calculator(10, 20)
# friendCalculator = Calculator(100, 200)

# myCalculator.add()
# myCalculator.sub()
# myCalculator.mul()
# myCalculator.div()

# friendCalculator.add()
# friendCalculator.sub()
# friendCalculator.mul()
# friendCalculator.div()

# # 인간 클래스:
# class Human:
#     # 속성
#     def __init__(self, height, weight):      # height, weight 매개변수
#         self.height = height                 # self.height, self.weight (객체 속성에 할당된 것)
#         self.weight = weight
    
#     # 기능(function, method)
#     def walk(self):
#         print('걷자!')

#     def run(self):
#         print('달리자!')

#     def printMyInfo(self):
#         print(f'나의 신장: {self.height}')
#         print(f'나의 체중: {self.weight}')

# human1 = Human(188, 87)
# human2 = Human(165, 49)

# human1.printMyInfo()
# human2.printMyInfo()

# human1 = human2
# human1.printMyInfo()    # human2를 할당 human2의 데이터가 조회됨, human1의 데이터는 사라짐.

# human1.height = 200
# human1.weight = 39

# human2.printMyInfo()     # 200, 39

# 배달 주문 클래스(Order)
class Order:
    # 속성
    def __init__(self, menu, price):
        self.menu = menu
        self.price = price
    
    # 기능 1: 주문 정보 출력
    def showInfo(self):
        print(f'선택하신 메뉴는 [{self.menu}]이며, 1인분 가격은 {self.price}원 입니다.')
    
    # 기능 2: 수량에 따른 총 결제 금액 계산
    def calculateTotal(self, count):
        total = self.price * count
        print(f'{self.menu} {count}개 주문 시 총 금액은 {total}원입니다.')

# 객체 생성 및 사용 예시
myOrder = Order('짜장면', 7000)
myOrder.showInfo()
myOrder.calculateTotal(3)

print('-' * 20)

friendOrder = Order('치킨', 20000)
friendOrder.showInfo()
friendOrder.calculateTotal(2)
        
# RPG 게임 캐릭터 클래스(Character)
class Character:
    # 속성
    def __init__(self, name, job, hp):
        self.name = name
        self.job = job
        self.hp = hp

    # 기능 1: 캐릭터 상태 확인
    def status(self):
        print(f'[{self.name}] 직업: {self.job} / 현재 HP: {self.hp}')
    
    # 기능 2: 데미지를 입었을 때
    def takeDamage(self, damage):
        self.hp -= damage
        print(f'{self.name}이(가) {damage}의 피해를 입었습니다! (남은 HP: {self.hp})')