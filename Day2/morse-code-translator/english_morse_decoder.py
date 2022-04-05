import Tkinter as tk


def english_morse_decoder(string,lang):
    '''
    accepts a string and returns the translated string in morse
    '''
    decoder = { 'a': '.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.',
                  'f':'..-.', 'g':'--.', 'h':'....', 'i':'..', 'j': '.---', 'k':'-.-',
                  'l':'.-..', 'm': '--', 'n':'-.', 'o':'---', 'p':'.--.',
                  'q':'--.-','r':'.-.','s': '...', 't':'-', 'u': '..-','v':'...-','w':'.--','x':'-..-',
                  'y':'-.--','z':'--..', '1':'.----','2':'..---','3':'...--','4':'....-','5':'.....', '6':'-....',
                  '7':'--...','8':'---..','9':'----.','0':'-----','?':'..--..', '!':'-.-.--', '.':'.-.-.-',
                  ',':'--..--',';':'-.-.-.',':':'---...','+':'.-.-.', '-':'-....-','/':'-..-.','=':'-...-'}
    res = ''
    flag = 0
    if(lang == 'mor'):
        for s in string:
            if(s == ' '):
                res+='/ '
            elif(s in decoder.keys()):
                res += decoder[s]+' '
            else: # unknowm character
                flag=1
                break
    else:
        decoder = {y:x for x,y in decoder.items()}
        string = string.split(' ')
        for s in string:
            if(s == '/'):
                res+=' '
            elif(s in decoder.keys()):
                res += decoder[s]
            else: # unknowm character
                flag=1
                break
    
    if(flag!=0):
        return(False,'Invalid string entered')
    else:
        return(True, res)



