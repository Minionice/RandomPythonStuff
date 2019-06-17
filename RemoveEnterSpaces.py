import os
fname=input('Enter a file path from which to remove enter spaces: ')
text=open(fname, 'r').read()
newtext=text.replace("\r\n", "")
newtext=newtext.replace('\n', '')
os.remove(fname)
f=open(fname, 'w')
f.write(newtext)
f.close()