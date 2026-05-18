goods = {
    '새우깡': 1200,
    '비비빅': 400,
    '초코파이': 500,
    '맛동산': 1500,
}

totalPrice = 0

def shrimpCrackersPrice():
    global totalPrice
    totalPrice += goods["새우깡"] * shrimpCrackers
    print(f'새우깡 구매 금액: {goods["새우깡"] * shrimpCrackers}원')

def bibibigsPrice():
    global totalPrice
    totalPrice += goods["비비빅"] * bibibigs
    print(f'비비빅 구매 금액: {goods["비비빅"] * bibibigs}원')

def chocopisPrice():
    global totalPrice
    totalPrice += goods["초코파이"] * chocopis
    print(f'초코파이 구매 금액: {goods["초코파이"] * chocopis}원') 

def matdongsansPrice():
    global totalPrice
    totalPrice += goods["맛동산"] * matdongsans
    print(f'맛동산 구매 금액: {goods["맛동산"] * matdongsans}원') 

shrimpCrackers = int(input('새우깡 구매 개수: '))
bibibigs = int(input('비비빅 구매 개수: '))
chocopis = int(input('초코파이 구매 개수: '))
matdongsans = int(input('맛동산 구매 개수: '))

print(f'새우깡 구매 개수: {shrimpCrackers}')
print(f'비비빅 구매 개수: {bibibigs}')
print(f'초코파이 구매 개수: {chocopis}')
print(f'맛동산 구매 개수: {matdongsans}')
print('=' * 40)
shrimpCrackersPrice()
bibibigsPrice()
chocopisPrice()
matdongsansPrice()
print('=' * 40)
print(f'총 구매 금액: {totalPrice}')
print('=' * 40)

# global 키워드 -> 함수 내부에서 전역 변수를 수정하고 싶을때 사용한다.
