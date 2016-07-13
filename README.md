nltk-dictionary
=============
A general dictionary (with synonyms, antonyms) for ebook users reading on PC. Just copy the word and it will automatically show you the various meaning(s) of the word. If you are on Linux or some other OS you will experience problem in creating system notifications. Will update the code for that soon.

This was built in Python 3.4 and please refer to the pre-requistes required for running it successfully. 

Pre-requisites - 
-------
1. Python 3.4 (although it shoudn't have problem running on other Python versions.)
2. NLTK for Python 
3. Wordnet corpus
4. Pyperclip for Python
5. (For Linux users) PyMsgBox library for creating alert box(refer google for installation)

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

Screenshots -  
-------
![Screenshot 1](https://s32.postimg.org/6f85uyuph/ss1.png "Screenshot 1")


![Screenshot 2](https://s32.postimg.org/jr2sdw9md/ss2.png "Screenshot 2")

Steps to install pyperclip,nltk - 
-------
1. Extract the zip content
2. Open cmd
3. Run the following commands - 
```cmd
cd "folderpath where zip is extracted"
python setup.py install
```
For nltk_data -
-------
1. Extract the folder and save it in your python directory.
