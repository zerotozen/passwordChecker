import requests
import hashlib
from tkinter import *
import tkinter.messagebox

#Main frame
#------------------------------------------------------------------------------------------------------------------#
root=Tk()
root.title('Password checker')
root.iconbitmap('C:\Users\AC\PycharmProjects\modules\Passwords\icon.ico')
root.config(bg="ghost white")

#Functions
#------------------------------------------------------------------------------------------------------------------#
def request_api_data(qery_char):
    url = 'https://api.pwnedpasswords.com/range/' + qery_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching:{res.status_code},check the api and try again')
    return res

def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    # print(f'Aqui los hasshes{hashes}')
    for h, count in hashes:
        if h == hash_to_check:
            # print(f'Aqui la h{h}')
            return count
    return 0

def pwned_api_check(password):
    # check password if exist in API response
    sha1password = (hashlib.sha1(password.encode('utf-8')).hexdigest().upper())
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    # print(response.text)
    # print((f'Aqui sha1password{sha1password}'))
    # print(f'Aqui tail{tail}')
    return get_password_leaks_count(response, tail)

def send_passwd():
    password = password_entry.get()
    print(password)
    password_entry.delete(0,END)
    main(password)

def clicker(event):
    password = password_entry.get()
    main(password)

def main(args):
    for password in args:
        count = pwned_api_check(args)
    if count:
        # print(f'{args} was found {count} times....you should change your password!')
        #print(f'Your password was found {count} times....you should change it!')
        #myLabel=Label(root,text=((f'{args} was found {count} times...you should change your password!')))
        tkinter.messagebox.showinfo('Result',(f'{args} was found {count} times...you should change your password!'))
    else:
        # print(f'{args} was NOT found. Carry on!')
        #print(f'Your password was NOT found. Carry on!')
        #myLabel=Label(root,text=('Your password was NOT found. Carry on!'))
        tkinter.messagebox.showinfo('Result','Your password was not found. Carry on!')


#Entry frame
#------------------------------------------------------------------------------------------------------------------#
entry_frame=Frame(pady=10)
entry_frame.pack(ipadx=0,ipady=0)
entry_frame.config(bg="ghost white")

#Entry
#------------------------------------------------------------------------------------------------------------------#
password_entry=Entry(entry_frame,bd='2',width='40')
password_entry.pack()
password_entry.grid(row=0,column=0)
password_entry.config(show='*')
password_entry.focus()
password_entry.bind('<Return>',clicker)

#Button
#------------------------------------------------------------------------------------------------------------------#
button_frame=Frame(pady=0)
button_frame.pack(ipadx=0,ipady=0)
b = Button(button_frame,text='Enter', command = send_passwd)
b.pack()
b.grid(row=0,column=1)
b.config(height='1',width='10',font='Verdana')

#Frame for labels
#------------------------------------------------------------------------------------------------------------------#
text_frame=LabelFrame(root,padx=10, pady=0)
text_frame.pack(padx=10,pady=10,ipadx=10,ipady=10)
text_frame.config(bg="ghost white",font='Verdana')

#Labels
#------------------------------------------------------------------------------------------------------------------#
label1 = Label(text_frame,text='¿HAVE BEEN YOUR PASSWORD PWNED?')
label1.grid(row=0,column=0, sticky = W, pady = 2)
label1.config(bg="ghost white",font=('Robot',10))

label2 = Label(text_frame,text='STEP 1: Introduce your password')
label2.grid(row=1,column=0, sticky = W, pady = 2)
label2.config(bg="ghost white",font=('Robot',10))

label3 = Label(text_frame,text='STEP 2: Wait to the result')
label3.grid(row=2,column=0, sticky = W, pady = 2)
label3.config(bg="ghost white",font=('Robot',10))

root.mainloop()