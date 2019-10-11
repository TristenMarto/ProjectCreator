from github import Github
from getpass import getpass
import sys
import os

path = "/Users/tristen.assenmacher/Desktop/Studie/projects/"

def createlocal():
    """Use input to create local directory"""
    
    #Github login
    username = "TristenMarto"
    password = getpass()
    user = Github(username, password).get_user()

    name = input("repo name: ")
    desc = input("desc: ")

    target = path + str(name)
    os.makedirs(target)
    os.chdir(target)

    f= open("README.md","w+")
    f.write(desc)
    f.close()

    os.system("git init")
    os.system("git add .")
    os.system("git commit")
    repo = user.create_repo(name)
    os.system("git remote add ")

def gitcommands():
    """init, add commit local files"""

createlocal()

