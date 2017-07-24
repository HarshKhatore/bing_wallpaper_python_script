import os

def install():
    os.chdir("C:\Python27\Scripts")
    cmdQuery = 'pip install requests'
    os.system(cmdQuery)
    cmdQuery = 'pip install pillow'
    os.system(cmdQuery)
    
if __name__ == "__main__":
    install()