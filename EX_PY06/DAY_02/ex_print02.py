"""
내장함수 print() 사용법
- print함수의 매개 변수 알아보기
- 매개 변수(parameter) : 함수 코드 실행 시에 필요한 데이터를 
                        명시해 놓은 것
- sep 매개 변수 : 구분자 의미, 여러 개 데이터를 보기 좋게 출력되도록 구분 해주는 변수
- end 매개 변수 : 출력 데이터의 마지막 부분에 줄바꿈 문자를 추가해 놓은 변수
"""

# 여러 개 데이터 전달 시 구분 문자를 변경하기
# 010-1111-2222

print("010", "1111", "2222") # 기본값 : 공백
print("010", "1111", "2222", sep = "-") # 설정값 : 하이픈 (-)
print("010", "1111", "2222", sep = "*") # 설정값 : 별 (*)

# 20살 입니다.

age = 20
print(age, "살 입니다.")
print(age, "살 입니다.", sep = "") # '' empty 문자

# 화면 출력 후에 문자 설정하기 => [기본] 줄바꿈 '\n'

print(1)             # 1\n
print(2, end = ' ')  # 2_
print(3)             # 3\n

# 출력 결과는 아래와 같고 print() 함수는 4개 사용
# 1234567
# abcdefg ABCDEFG
# 1234567

print(1234567)
print("abcdefg", end = " ")
print("ABCDEFG")
print(1234567)