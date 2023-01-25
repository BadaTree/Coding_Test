# 10의 배수 간편하게 표현하기 : 유효숫자e지수 = 유효숫자*10^지수
# print(f"1억은 {1e9}이다")

# 컴퓨터에서 실수 정확하게 표현하기 : round (실수형데이터,반올림하고자하는 위치-1)

a = 0.3 + 0.6
# 컴퓨텅에서는 0.899999로 표현됨
if round(a, 4) == 0.9:  # 소수점 5번째 자리에서 반올림
    print("실수로 정확하게 표현됨")

# 파이썬에서의 사칙연산
a = 7
b = 3

# 나누기
print(a / b)

# 나머지
print(a % b)

# 몫
print(a // b)

# 거듭제곱
print(a ** b)

# 리스트 컴프리헨션 : 대괄호 안에 조건문과 반복문을 넣어 초기화하는 방법

array = [i for i in range(20) if i % 2 != 0]
print(array)

# 2차원 리스트를 초기화할 때 매우 효과적이다
# 3*5 list

array = [[0] * 5 for _ in range(3)]
print(array)

# 리스트 관련 메서드

a = [3, 9, 1, 16, 5, 4, 9, 7, 0, 9]

# list 맨 끝에 원소 삽입
a.append(5)
# 오름차순으로 정렬
a.sort()
# 내림차순으로 정렬
a.sort(reverse=True)
# 특정위치에 원소 삽입 (삽입할 위치의 인덱스, 값)
a.insert(1, 25)
# 특정 값 개수 세기
print(a.count(5))

# 특정 값을 가지는 원소 제거 (여러개라면 하나만 제거 )
a.remove(9)
print(a)
# python에서 removeall 구현하기
remove_value = [9]
result = [i for i in a if i not in remove_value]
print(result)

# 사전 자료형 선언 및 함수
dictionary = dict()
dictionary['키'] =160
dictionary['몸무계'] =  45

print(dictionary)