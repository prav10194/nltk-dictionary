import nltk
import pyperclip
from nltk.corpus import wordnet
import ctypes
import time
import re
import sys


class PyDict:

    def stop(self):
        sys.exit()
    def run(self,loop='NoValue',timer=2):
        timeInSec=timer*3600
        startTime=time.time()
        while True and time.time()-startTime<timeInSec: 
            word=pyperclip.paste()
            #print(word)
            word=re.sub('[^A-Za-z]+', '', word)
            word=word.lower()
            time.sleep(2)

            if word!=loop:
                #print(word+'\t'+loop)
                define=wordnet.synsets(word)        
                
                #print(word)
                #print(define)
                definitions='Meaning of word - '+word+'\n\n'
                counter=1
                for i in define:
                    message=str(counter)+'. '+i.definition()+'\n'
                    definitions=definitions+'\n'+message
                    counter=counter+1

                synonyms=[]
                for i in define:
                    for j in i.lemmas():
                        synonyms=synonyms+[j.name()]
                synonyms=set(synonyms)


                antonyms=[]

                for i1 in define:
                    for j1 in i1.lemmas():
                        for k1 in j1.antonyms():
                            antonyms=antonyms+[k1.name()]

                antonyms=set(antonyms)
                #print(antonyms)
                
                    ctypes.windll.user32.MessageBoxW(0, definitions+'\n\nSynonyms: '+', '.join(synonyms)+'\n\nAntonyms: '+', '.join(antonyms), 'Word Meaning - '+word, 0) #linux users comment this out and uncomment alert given below
                
                    #alert(text=definitions+'\n\nSynonyms: '+', '.join(synonyms)+'\n\nAntonyms: '+', '.join(antonyms), title='Word Meaning - '+word, button='OK')
                #ctypes.windll.user32.MessageBoxW(0, definitions+'\n\nSynonyms: '+', '.join(synonyms)+'\n\nAntonyms: '+', '.join(antonyms), 'Word Meaning - '+word, 0)
                loop=word
                #time.sleep(1)

    


