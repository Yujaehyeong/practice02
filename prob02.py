# 문제2. 다음과 같은 텍스트에서 모든 태그를 제외한 텍스트만 출력하세요.

s = """
<html>
    <body style='background-color:#ffff'>
        <h4>Click</h4>
        <a href='http://www.python.org'>Here</a>
        <p>
        	To connect to the most powerful tools in the world.
        </p>
    </body>
</html>"""

exceptTag ='';
tag='';
for i in range(0, len(s)):
    if s[i] == '<':
        exceptTag +=" "
        tag = '<'
    elif s[i] =='>':
        exceptTag +=" "
        tag =''
    elif tag == '<':
        exceptTag +=" "
    else:
        exceptTag += s[i]
print(exceptTag,end='')