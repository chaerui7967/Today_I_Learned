import os
print (os.getcwd()) #현재 디렉토리의
print (os.path.realpath(__file__))#파일
print (os.path.dirname(os.path.realpath(__file__)) )#파일이 위치한 디렉토리