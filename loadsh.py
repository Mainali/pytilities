import requests

try:
    resp = requests.get('https://acpmasquerade-nepal-loadshedding-schedule-by-sparrow-sms.p.mashape.com/schedule.php?format=text&group=5',headers={"X-Mashape-Key": "x0WfLi5sPgmshuWPHTmQgdh2e1WUp1rApKSjsn4c2sPOLVRnHc","Accept": "text/plain"})
    print('------------live Data---------')
    print(resp.text)
    print('------------live Data---------')
    with open("lsdata.txt","w") as text_file:
        text_file.write("{}".format(resp.text))

except:
    print('------------local cached Data---------')
    try:
        file = open('lsdata.txt', 'r')
        print(file.read())
        file.close()
    except:
        print('NOT FOUND!')
    print('------------local cached Data---------')