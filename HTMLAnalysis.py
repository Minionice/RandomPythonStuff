import os
import unicodedata

fstring="HTMLTags.txt"

def getTag(str):
    ct=0
    tag=''
    arr=dict()
    arr["div"]=0 #Ensure that this key exists
    while ct<len(str):
        if str[ct]=='<':
            ct+=1
            if str[ct]!='/' and str[ct]!='!':
                while str[ct]!='>' and str[ct]!=' ':
                    tag+=str[ct]
                    ct+=1
                if tagslist.find(tag)!=-1 and tag!=None and tag!='':
                  if arr.get(tag)==None:
                      arr[tag]=1
                  else:
                      arr[tag]+=1
                ct+=1
                tag=''
            else:
                ct+=2
        else:
            ct+=1
    return arr

#Get the URL string from the suer
urlstring=input("Enter a URL for a Web page: ")

#Create a file with all current HTML tags
if os.access(fstring, os.F_OK):
    os.remove(fstring)
f=open(fstring, "w")
f.write("<!--><!DOCTYPE><a><abbr><acronym><address><applet><area><article><aside><audio><b><base><basefont><bdi><bdo><big><blockquote><body><br><button><canvas><caption><center><cite><code><col><colgroup><data><datalist><dd><del><details><dfn><dialog><dir><div><dl><dt><em><embed><fieldset><figcaption><figure><font><footer><form><frame><frameset><h1> - <h6><head><header><hr><html><i><iframe><img><input><ins><kbd><label><legend><li><link><main><map><mark><meta><meter><nav><noframes><noscript><object><ol><optgroup><option><output><p><param><picture><pre><progress><q><rp><rt><ruby><s><samp><script><section><select><small><source><span><strike><strong><style><sub><summary><sup><svg><table><tbody><td><template><textarea><tfoot><th><thead><time><title><tr><track><tt><u><ul><var><video><wbr>")
f.close()
f2=open(fstring, "r")
tagslist=f2.read()
f2.close()

#Obtain the text for the HTML page
os.system('curl '+urlstring+' -o "HTML.txt"') #Runs a cURL command through the OS to extract the HTML file
htmlFile=open("HTML.txt", "r", encoding='utf-8')
text=htmlFile.read()
htmlFile.close()

#Run the analysis function defined earlier and print the results
array=getTag(text)
for key, value in sorted(array.items(), key=lambda item: item[1], reverse=True):
    print("%s: %s" % (key, value))
sum=0
for el in array:
  sum+=array[el]
if sum!=0:
    print("Percentage of div: "+str(array["div"]/sum*100.0))
os.remove("HTML.txt")