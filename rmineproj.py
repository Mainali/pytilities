import subprocess

def install(name):
    subprocess.call(['sudo','pip3','install', name])

try:
    from redmine import Redmine
except:
    install('python-redmine')
    from redmine import Redmine


import pprint
import json

try:
    with open('cred.json') as data_file:
        data = json.load(data_file)
except:
    username = input('Username:')
    passwd = input('Password:')
    textcred = '{"uname":"'+username+'","upass":"'+passwd+'"}'
    with open("cred.json","w") as text_file:
        text_file.write(textcred)
    with open('cred.json') as data_file:
        data = json.load(data_file)


myredmine = Redmine('http://redmine.ekbana.info/', username=data['uname'], password=data['upass'])

projects = myredmine.project.all()


# pprint.pprint(list(projects))
# print('------------------------------')
# project = input('project number : ')
# myproject = myredmine.project.get(project)
# print('------------------------------All Issues----------------')
# pprint.pprint(list(myproject.issues))
#
# print('------------------------------------------------------------')
# print('------------------------------Assigned to me----------------')
# myissues = myredmine.issue.filter(project_id=project, assigned_to_id='me', subproject_id='!*', sort='category:desc')
# pprint.pprint(list(myissues))
# print('------------------------------')
# issue = input('issue number : ')
# issuedetail = myredmine.issue.get(issue, include='children,journals,watchers')
# pprint.pprint(issuedetail.description)



def listprojects():
    pprint.pprint(list(projects))

def listissues():
    project = input('project number : ')
    myproject = myredmine.project.get(project)
    print('------------------------------All Issues----------------')
    pprint.pprint(list(myproject.issues))

    print('------------------------------------------------------------')
    print('------------------------------Assigned to me----------------')
    myissues = myredmine.issue.filter(project_id=project, assigned_to_id='me', subproject_id='!*', sort='category:desc')
    pprint.pprint(list(myissues))
    print('------------------------------')

def issdetails():
    issue = input('issue number : ')
    issuedetail = myredmine.issue.get(issue, include='children,journals,watchers')
    pprint.pprint(issuedetail.description)


def menus():
    itm = input('Enter code (p for listing projects, i for issues, id for issue detail,e to exit):')
    if itm == 'p':
        listprojects()
        menus()
    elif itm == 'i':
        listissues()
        menus()
    elif itm == 'id':
        issdetails()
        menus()
    elif itm == 'e':
        return True
    else:
        menus()


menus()