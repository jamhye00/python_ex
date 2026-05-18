# 1.숫자 5개를 리스트에 저장한 뒤 가장 큰 숫자 출력하기
#  [3, 7, 1, 9, 5]
# numbers = [3, 7, 1, 9, 5]
# numbers.sort(reverse=True)
# print(f'maxNum: {numbers[:1]}')

# 1
# maxNum = 0
# for num in numbers:
#     if num > maxNum:
#         maxNum = num

# print(f'maxNum: {maxNum}')

# 2
# print(max(numbers))


# 2. 사용자에게 숫자 입력받아서
# 1부터 입력한 숫자까지 합계 출력하기 ( 5 )
# userNum = int(input('숫자 입력: '))
# sum = 0

# for i in range(1, userNum+1):
#     sum += i

# print(f'1부터 {userNum}까지의 합: {sum}')

# 3. 리스트에 있는 숫자 중 짝수만 출력하기
#  [1,2,3,4,5,6]
# numbers1 = [1, 2, 3, 4, 5, 6]

# for num in numbers1:
#     if num % 2 == 0:
#         print(f'{num}은 짝수입니다.')

# 4. 리스트 숫자를 오름차순 정렬하기
# [5,1,7,3]
# numbers2 = [5, 1, 7, 3]
# numbers2.sort()
# print(f'numbers2: {numbers2}') 

# 5. 리스트 숫자를 내림차순 정렬하기
#  [5,1,7,3]
# numbers2.sort(reverse=True)
# print(f'numbers2: {numbers2}') 

# 6. 리스트 안 숫자의 평균 구하기 [10,20,30]
# numbers3 = [10, 20, 30]

# for listNum in numbers3:
#     average = listNum / len(numbers3)
#     print(f'average: {average:.2f}')

# total = 0
# totalAverage = 0

# for listNum in numbers3:
#      total += listNum

# totalAverage = total / len(numbers3)
# print(f'totalAverage: {totalAverage:.2f}')

# 7. 리스트에서 가장 작은 숫자 찾기
#  (min() 사용 금지)
numbers3 = [3, 7, 1, 9, 5]
# numbers3.sort()
# print(f'minNum: {numbers3[:1]}')

minNum = numbers3[0]
for num in numbers3:
    if num < minNum:
        minNum = num

print(f'minNum: {minNum}')

# 8. 1부터 100까지 숫자 중
# 3의 배수와 5의 배수 출력하기
# for num in range(1,101):
#     if num % 3 == 0:
#         print(f'3의 배수: {num}')

# print('-------------------------------')

# for num in range(1,101):
#     if num % 5 == 0:
#         print(f'5의 배수: {num}')

# 9. 사용자가 입력한 숫자를 리스트에 저장하다가
# 0 입력하면 종료 후 리스트 출력하기
# [입력: 3 ,입력: 7, 입력: 2 ,입력: 0]
nums = []

while True:
    userInputNumber = int(input('숫자 입력:'))
   
    if userInputNumber == 0:
        break
        
    nums.append(userInputNumber)    

print(f'nums: {nums}')  