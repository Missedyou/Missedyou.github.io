# -*- coding:utf-
import subprocess
import sys
import os

def push():
    add = subprocess.Popen("git add .", shell=True)
    add.wait()
    
    commit_content = sys.argv[1]

    commit = subprocess.Popen("git commit -m '%s'"%commit_content, shell=True)
    commit.wait()

    push = subprocess.Popen("git push origin master", shell=True)


if __name__ == '__main__':
    push()