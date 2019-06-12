# 문제1. 파이썬 경로명 s = '/usr/local/bin/python' 에서
# 각각의 디렉토리 경로명을 분리하여 출력하세요.

# s = '/usr/local/bin/python'
#
# folder = ''
# list = []
# result = ''
# separateFileName = '\''
# for i in range(0, len(s)):
#     if s[i] != '/':
#         folder+=s[i]
#         if i==len(s)-1:
#             result += '\'' + folder + '\''
#             separateFileName +='\', \''+folder+'\''
#     else:
#         if folder != '':
#             result += '\''+folder+'\', '
#             separateFileName+= '/'+folder
#             folder=''
# print(result)
# print(separateFileName)

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
