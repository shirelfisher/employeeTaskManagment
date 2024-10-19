from tkinter import *

window = Tk()
window.title('Dashboard')
window.geometry("950x500+160+70")
window.iconbitmap('employee icon.ico')
window.resizable(False, False)
window.config(bg='white')

bg_image = PhotoImage(file='title icon.png')

title_label = Label(window, image=bg_image, compound=LEFT, text='Employee Task Management System', font=('david', 27, 'bold'),
                    bg='#53868B', fg='white', anchor='w', padx=35)
title_label.place(x=0, y=0, relwidth=1)

logout_bt = Button(window, text='Logout', font=('david', 15, 'bold'), fg='#53868B')
logout_bt.place(x=820, y=15)

sub_title_label = Label(window, text='Welcome Admin\t Date: 19-10-2024\t Time: 22:00:00 pm', font=('david', 12, 'bold'), bg='#DCDCDC', fg='#53868B')
sub_title_label.place(x=0, y=70, relwidth=1)

left_frame = Frame(window)
left_frame.place(x=0, y=102, width=200, height=555)

window.mainloop()
