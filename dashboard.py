from tkinter import *
from tkinter import ttk

# Functionality Part


def employee_screen():
    global back_icon
    employee_frame = Frame(window, width=745, height=405)
    employee_frame.place(x=200, y=92)
    headline_label = Label(employee_frame, text='Employee Task Management View', font=('david', 18, 'bold'), pady=10, bg='#B4CDCD', fg='white')
    headline_label.place(x=0, y=0, relwidth=1)

    back_icon = PhotoImage(file='back button.png')
    back_bt = Button(employee_frame, image=back_icon, bd=0, bg='#B4CDCD', command=lambda: employee_frame.place_forget())
    back_bt.place(x=5, y=7)

    upper_frame = Frame(employee_frame, bg='white')
    upper_frame.place(x=0, y=50, relwidth=1, height=390)

    search_frame = Frame(upper_frame, bg='#7A8B8B')
    search_frame.pack(fill=X)

    search_content_frame = Frame(search_frame, bg='#7A8B8B')
    search_content_frame.pack(expand=True, padx=10)

    search_filter = ttk.Combobox(search_content_frame, values=('Name', 'Employee number'), font=('Times new roman', 11), state='readonly')
    search_filter.set('Search By')
    search_filter.pack(side=LEFT, padx=2)

    search_line = Entry(search_content_frame, font=('Times new roman', 10))
    search_line.pack(side=LEFT, padx=2)

    search_bt = Button(search_content_frame, text='Search', font=('Times new roman', 10))
    search_bt.pack(side=LEFT, padx=2)

    show_all_bt = Button(search_content_frame, text='Show All', font=('Times new roman', 10))
    show_all_bt.pack(side=LEFT, padx=2)

    vertical_scr = ttk.Scrollbar(orient=VERTICAL)

    employee_table = ttk.Treeview(upper_frame, columns=('Emp No', 'Emp Name', 'Open', 'In Progress', 'Closed'),
                                  show='headings', height=12, yscrollcommand=vertical_scr.set)

    vertical_scr.config(command=employee_table.yview)

    vertical_scr.pack(side=RIGHT, anchor='center', ipady=100)

    employee_table.pack(pady=10, anchor='nw', ipadx=100)

    employee_table.heading('Emp No', text='Employee No')
    employee_table.heading('Emp Name', text='Employee Name')
    employee_table.heading('Open', text='Open Missions')
    employee_table.heading('In Progress', text='Missions In Progress')
    employee_table.heading('Closed', text='Closed Missions')

    employee_table.column('Emp No', width=50)
    employee_table.column('Emp Name', width=120)
    employee_table.column('Open', width=120)
    employee_table.column('In Progress', width=120)
    employee_table.column('Closed', width=120)

    note = Label(upper_frame, text='* Data as of today', font=('Times new roman', 10), fg='black', bg='white')
    note.pack(side=LEFT, anchor="n")


# GUI Part

window = Tk()
window.title('Dashboard')
window.geometry("950x500+160+70")
window.iconbitmap('employee icon.ico')
window.resizable(False, False)
window.config(bg='#EAEAEA')

bg_image = PhotoImage(file='title icon.png')

title_label = Label(window, image=bg_image, compound=LEFT, text='Employee Task Management System', font=('david', 27, 'bold'),
                    bg='#53868B', fg='white', anchor='w', padx=35)
title_label.place(x=0, y=0, relwidth=1)

logout_bt = Button(window, text='Logout', font=('david', 15, 'bold'), fg='#53868B')
logout_bt.place(x=820, y=15)

sub_title_label = Label(window, text='        Welcome Admin\t\t Date: 19-10-2024\t       Time: 22:00:00 PM', font=('david', 12, 'bold'), bg='#DCDCDC', fg='#53868B')
sub_title_label.place(x=0, y=70, relwidth=1)

left_frame = Frame(window)
left_frame.place(x=0, y=92, width=200, height=410)

lf_image = PhotoImage(file='skills logo lf.png')
lf_logo = Label(left_frame, image=lf_image)
lf_logo.pack()

menu_label = Label(left_frame, text='Menu', font=('david', 20, 'bold'), fg='white', bg='#5F9EA0')
menu_label.pack(fill=X, pady=15)

emp_bt_image = PhotoImage(file='employee bt.png')
employees_bt = Button(left_frame, image=emp_bt_image, compound=LEFT, text='Employees', font=('david', 18, 'bold'), fg='#53868B', anchor='w', padx=15, command=employee_screen)
employees_bt.pack(fill=X)

dep_bt_image = PhotoImage(file='department bt.png')
departments_bt = Button(left_frame, image=dep_bt_image, compound=LEFT, text='Departments', font=('david', 18, 'bold'), fg='#53868B', anchor='w', padx=15)
departments_bt.pack(fill=X)

per_bt_image = PhotoImage(file='performance bt.png')
performance_bt = Button(left_frame, image=per_bt_image, compound=LEFT, text='Performance', font=('david', 18, 'bold'), fg='#53868B', anchor='w', padx=15)
performance_bt.pack(fill=X)

goals_bt_image = PhotoImage(file='goals bt.png')
goals_bt = Button(left_frame, image=goals_bt_image, compound=LEFT, text='Goals', font=('david', 18, 'bold'), fg='#53868B', anchor='w', padx=15)
goals_bt.pack(fill=X)

exit_bt_image = PhotoImage(file='exit_bt.png')
exit_bt = Button(left_frame, image=exit_bt_image, compound=LEFT, text='Exit', font=('david', 18, 'bold'), fg='#53868B', anchor='w', padx=15)
exit_bt.pack(fill=X)

open_task_frame = Frame(window, bg='#68838B', bd=2, relief=RIDGE)
open_task_frame.place(x=300, y=130, height=160, width=260)
open_task_icon = PhotoImage(file='open task icon.png')
open_task_icon_label = Label(open_task_frame, image=open_task_icon, bg='#68838B')
open_task_icon_label.pack(pady=5)

open_task_label = Label(open_task_frame, text='Total Open Tasks', bg='#68838B', fg='white', font=('david', 14, 'bold'))
open_task_label.pack()

open_task_count_label = Label(open_task_frame, text='29', bg='#68838B', fg='white', font=('david', 24, 'bold'))
open_task_count_label.pack()

prog_task_frame = Frame(window, bg='#68838B', bd=2, relief=RIDGE)
prog_task_frame.place(x=600, y=130, height=160, width=260)
prog_task_icon = PhotoImage(file='progress task icon.png')
prog_task_icon_label = Label(prog_task_frame, image=prog_task_icon, bg='#68838B')
prog_task_icon_label.pack(pady=5)

prog_task_label = Label(prog_task_frame, text='Tasks In Progress', bg='#68838B', fg='white', font=('david', 14, 'bold'))
prog_task_label.pack()

prog_task_count_label = Label(prog_task_frame, text='11', bg='#68838B', fg='white', font=('david', 24, 'bold'))
prog_task_count_label.pack()

closed_task_frame = Frame(window, bg='#68838B', bd=2, relief=RIDGE)
closed_task_frame.place(x=450, y=310, height=160, width=260)
closed_task_icon = PhotoImage(file='closed task icon.png')
closed_task_icon_label = Label(closed_task_frame, image=closed_task_icon, bg='#68838B')
closed_task_icon_label.pack(pady=5)

closed_task_label = Label(closed_task_frame, text='Closed Tasks \n(Current Month)', bg='#68838B', fg='white', font=('david', 14, 'bold'))
closed_task_label.pack()

closed_task_count_label = Label(closed_task_frame, text='108', bg='#68838B', fg='white', font=('david', 24, 'bold'))
closed_task_count_label.pack()


window.mainloop()
