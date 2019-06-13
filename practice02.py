

# 문제2. 다음과 같은 텍스트에서 모든 태그를 제외한 텍스트만 출력하세요.

# s = """
# <html>
#     <body style='background-color:#ffff'>
#         <h4>Click</h4>
#         <a href='http://www.python.org'>Here</a>
#         <p>
#         	To connect to the most powerful tools in the world.
#         </p>
#     </body>
# </html>"""
#
# exceptTag ='';
# tag='';
# for i in range(0, len(s)):
#     if s[i] == '<':
#         exceptTag +=" "
#         tag = '<'
#     elif s[i] =='>':
#         exceptTag +=" "
#         tag =''
#     elif tag == '<':
#         exceptTag +=" "
#     else:
#         exceptTag += s[i]
# print(exceptTag,end='')



# 문제3. 1)다음 문자열을 모든 소문자를 대문자로 변환하고,
# 문자 ',', '.','\n'를 없앤 후에 중복 없이 각 단어를 순서대로 출력하세요.

# s = """We encourage everyone to contribute to Python. If you still have questions after reviewing the material
# in this guide, then the Python Mentors group is available to help guide new contributors through the process."""

# s = s.replace(',','').replace('.','').replace('\n','')
# s = s.upper()
# list = s.split(' ');
# print(list)
# dic = dict()
# for voca in list:
#     if dic.__contains__(voca):
#         dic[voca] = dic.get(voca)+1
#     else:
#         dic[voca] = 1
#
# keyList = dic.keys()
# keyList = sorted(keyList)
# for key in keyList:
#     print(key+':'+str(dic.get(key)))



# 문제4 반복문을 이용하여 369게임에서 박수를 쳐야 하는 경우의 수를 순서대로 화면에
# 출력해보세요. 1부터 99까지만 실행하세요.

# number = int(input(''))
# temp = number
# clap = ''
# while number >= 1:
#     if (number % 10) % 3 == 0:
#         clap +='짝'
#     number /= 10
#     number = int(number)
# print(temp, clap)


# 문제5. 함수 sum 을 만드세요. 이 함수는 임의의 개수의 인수를 받아서 그 합을 계산합니다.







# 문제6 숨겨진 카드의 수를 맞추는 게임입니다.
# 1-100까지의 임의의 수를 가진 카드를 한 장 숨기고 이 카드의 수를 맞추는 게임입니다.
# 아래의 화면과 같이 카드 속의 수가 57인 경우를 보면 수를 맞추는 사람이 40이라고 입력하면
# "더 높게", 다시 75이라고 입력하면 "더 낮게" 라는 식으로 범위를 좁혀가며 수를 맞추고 있습니다.
# 게임을 반복하기 위해 y/n이라고 묻고 n인 경우 종료됩니다.

# min , max = 1, 100
# while True :
#     n= random.randrange(max) +min
#     print(n)
#
#     if n == int(input('수 입력: ')):
#         break
