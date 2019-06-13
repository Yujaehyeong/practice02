# 문제1. 파이썬 경로명 s = '/usr/local/bin/python' 에서
# 각각의 디렉토리 경로명을 분리하여 출력하세요.

s = '/usr/local/bin/python'

folder = ''
list = []
result = ''
separateFileName = '\''
for i in range(0, len(s)):
    if s[i] != '/':
        folder+=s[i]
        if i==len(s)-1:
            result += '\'' + folder + '\''
            separateFileName +='\', \''+folder+'\''
    else:
        if folder != '':
            result += '\''+folder+'\', '
            separateFileName+= '/'+folder
            folder=''
print(result)
print(separateFileName)