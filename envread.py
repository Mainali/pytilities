import os

uat_pass = os.environ.get("uatpass", None)
if not uat_pass :
    passwd = raw_input('enter pass: ')
    os.environ["uatpass"]= passwd
    print('saved password {}',os.environ['uatpass'])
else:
    print(os.environ['uatpass'])