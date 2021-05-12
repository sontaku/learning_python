# [ 연습문제 ]
# - 리스트를 인자로 받아 짝수만 갖는 리스트 반환하는 함수를 만들어서 호출하여 그 결과를 출력하시오
# [ 실행 ]
def even_filter(oldList=[]):
    newList = [oldList[i] for i in range(len(oldList)) if oldList[i] % 2 == 0]
    return newList
print(even_filter([1, 2, 4, 5, 8, 9, 10]))

print('------------------------')
print('------------------------')
print('------------------------')

# - 주어진 수가 소수인지 아닌지 판단하는 함수를 만들어서 호출하여 그 결과를 출력하시오
# [ 실행 ]
def is_prime_number(n):
    # flag = True
    # for i in range(2, n):
    #     if n % i == 0:
    #         flag = False
    # if flag:
    #     return '소수'
    # else:
    #     return '소수가 아닙니다'

    return "소수가 아닙니다." if [False for i in range(2, int(n / 2) + 1) if n % i == 0] else "소수입니다."
    # return '소수' for i in range(2, n) if n % i == 0 if n % i != 0
print(is_prime_number(60))
print(is_prime_number(61))

print('------------------------')
print('------------------------')
print('------------------------')

# - 주어진 문자열에서 모음의 개수를 출력하는 함수를 만들어서 호출하여 그 결과를 출력하시오
# [ 실행 ]
def count_vowel(args):
    args = args.lower()
    vowels = 'aeiou'
    count = 0
    for i in range(len(args)):
        if args[i] in vowels:
            count += 1
    return count
print(count_vowel("pythonian"))