nltk-dictionary
=============
A general dictionary (with synonyms, antonyms) for ebook users reading on PC. Just copy the word and it will automatically show you the various meaning(s) of the word. 

This was built in Python 3.4 and please refer to the pre-requistes required for running it successfully. 

Pre-requisites - 
-------
1. Python 3.4 (although it shoudn't have problem running on other Python versions.)
2. NLTK for Python 
3. Wordnet corpus
4. Pyperclip for Python

Usage - 
-------
1. Save the script in your python folder. 
2. Open IDLE or cmd to run python.
3. Run the following code - 

```python
import os
os.chdir('path') #path where script is saved

from dictionary import PyDict
PyDict().run() #by default the script runs for 2 hours in background

#To run for specific hour(s) say 1.5 hours
PyDict().run(timer=1.5)
```
To stop script, simply close the screen.

Screenshot -  
-------
![Alt text](https://postimg.org/image/qzcztgagh/ "Screenshot 1")
