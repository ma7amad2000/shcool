from tkinter import *
from tkinter import ttk
import pymysql


class Student:
    #    --------------- النافذه ------------
    def __init__(self, root):
        self.root = root
        self.root.geometry('1350x690+1+1')
        self.root.title('منظومة مدرسه')
        self.root.configure(background="silver")
        self.root.resizable(False, False)
        title = Label(self.root,
                      text='[نظام تسجيل الطلاب]', bg='#1AAECB', font=('monospce', 14,), fg='white')
        title.pack(fill=X)
        # ---------------  متغيرات قاعدة البيانات-------

        self.id_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.nw3_var = StringVar()
        self.phone_var = StringVar()
        self.mstawa_var = StringVar()
        self.search_var = StringVar()
        self.address_var = StringVar()
        self.delst_var = StringVar()


# ------------------ ادوات النحكم بالبرنامج  -------------
        adwat_Frame = Frame(self.root, bg='white')
        adwat_Frame.place(x=1137, y=30, width=210, height=400)
        Lbl_id = Label(adwat_Frame, text='رقم القيد', bg='white')
        Lbl_id.pack()
        id_ent = Entry(adwat_Frame, textvariable=self.id_var,
                       bd='4', justify='center')
        id_ent.pack()
        lbl_name = Label(adwat_Frame, bg='white', text='اسم الطالب')
        lbl_name.pack()
        name_ent = Entry(adwat_Frame, textvariable=self.name_var,
                         bd='4', justify='center')
        name_ent.pack()
        lbl_email = Label(adwat_Frame, bg='white', text='ايميل ولي الامر')
        lbl_email.pack()
        email_ent = Entry(
            adwat_Frame, textvariable=self.email_var, bd='4', justify='center')
        email_ent.pack()

        lbl_phone = Label(adwat_Frame, bg='white', text='هاتف ولي الامر')
        lbl_phone.pack()
        phone_ent = Entry(
            adwat_Frame, textvariable=self.phone_var, bd='4', justify='center')
        phone_ent.pack()

        lbl_mstawa = Label(adwat_Frame, bg='white', text='مستوى الطالب')
        lbl_mstawa.pack()
        email_mstawa = Entry(
            adwat_Frame, textvariable=self.mstawa_var, bd='4', justify='center')
        email_mstawa.pack()

        lbl_nw3 = Label(adwat_Frame, bg='white', text='اختر جنس الطالب')
        lbl_nw3.pack()
        combo_nw3 = ttk.Combobox(adwat_Frame, textvariable=self.nw3_var)
        combo_nw3['value'] = ('ذكر', 'انثى')
        combo_nw3.pack()

        lbl_address = Label(adwat_Frame, text='عنوان الطالب', bg='white')
        lbl_address.pack()
        addres_ent = Entry(
            adwat_Frame, textvariable=self.address_var, justify='center', bd='4')
        addres_ent.pack()

        lbl_delSt = Label(adwat_Frame, fg='red', bg='white',
                          text='حذف طالب بالقيد')
        lbl_delSt.pack()
        delst_ent = Entry(
            adwat_Frame, textvariable=self.delst_var, bd='4', justify='center')
        delst_ent.pack()
        # -------- ازرار التحكم -------
        azrar_Frame = Frame(self.root, bg='white')
        azrar_Frame.place(x=1137, y=435, width=210, height=253)
        title1 = Label(azrar_Frame, text='لوحة التحكم',
                       font=('Deco', 14), fg='white', bg='#298089')
        title1.pack(fill=X)

        add_btn = Button(azrar_Frame, text='اضافة طالب',bg='#1AAECB', fg='white',command=self.add_student)
        add_btn.place(x=33, y=39, width=150, height=30)

        del_btn = Button(azrar_Frame, text='مسح طالب',
                         bg='#1AAECB', fg='white',command=self.delet)
        del_btn.place(x=33, y=80, width=150, height=30)
        update_btn = Button(
            azrar_Frame, text='تعديل بيانات الطالب', bg='#1AAECB', fg='white',command=self.edit_tab)
        update_btn.place(x=33, y=115, width=150, height=30)
        clear_btn = Button(azrar_Frame, text='افراغ', bg='#1AAECB', fg='white',command=self.clear)
        clear_btn.place(x=33, y=150, width=150, height=30)
        abuot_btn = Button(azrar_Frame, text='حول المطور',
                           bg='red', fg='white')
        abuot_btn.place(x=33, y=185, width=150, height=30)
        exit_btn = Button(azrar_Frame, text='اغلاق البرنامج',
                          bg='red', fg='white')
        exit_btn.place(x=33, y=225, width=150, height=30)

        # _________________ بحث عن الطلاب ___________________

        search_Frame = Frame(self.root, bg='white')
        search_Frame.place(x=1, y=30, width=1134, height=50)

        lbl_sear = Label(search_Frame, text='البحث عن طالب', bg='white')
        lbl_sear.place(x=1034, y=12)

        combo_sear = ttk.Combobox(search_Frame, justify='right')
        combo_sear['value'] = ('القيد', 'الاسم', 'البريد', 'الهاتف')
        combo_sear.place(x=880, y=12)

        search_ent = Entry(
            search_Frame, textvariable=self.search_var, justify='right', bd='3')
        search_ent.place(x=740, y=12)

        se_btn = Button(search_Frame, text='بحث', bg='#298089', fg='white')
        se_btn.place(x=630, y=12, width=100, height=25)

        # -----------  عرض البيانات ------------
        data_Frame = Frame(self.root, bg='#F2F4F4')
        data_Frame.place(x=1, y=82, width=1134, height=605)

        # --------- السكرول ----------
        scroll_x = Scrollbar(data_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(data_Frame, orient=VERTICAL)

        # --------------- tree veiw --------------
        self.student_table = ttk.Treeview(data_Frame,
                                          columns=(
                                              'address', 'nw3', 'mstawa', 'phone', 'email', 'name', 'id'),
                                          xscrollcommand=scroll_x.set,
                                          yscrollcommand=scroll_y.set)
        self.student_table.place(x=18, y=1, width=1130, height=590)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=LEFT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table['show'] = 'headings'
        self.student_table.heading('id', text='رقم القيد')
        self.student_table.heading('name', text='اسم الطالب\ه')
        self.student_table.heading('email', text='البريد')
        self.student_table.heading('phone', text='هاتف الطالب\ولي الامر')
        self.student_table.heading('mstawa', text='مستوى الطالب\ه')
        self.student_table.heading('nw3', text='جنس الطالب')
        self.student_table.heading('address', text='العنوان')

        self.student_table.column('address', width=130)
        self.student_table.column('nw3', width=30)
        self.student_table.column('mstawa', width=50)
        self.student_table.column('phone', width=70)
        self.student_table.column('email', width=70)
        self.student_table.column('name', width=130)
        self.student_table.column('id', width=30)
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)

# ========التعامل مع قاعدة البيانات======

        self.fetch_all()
    def add_student(self):
        con = pymysql.connect(
        host='localhost', user='root', password='', database='stude')
        cur = con.cursor()
        cur.execute("insert into students1 values(%s,%s,%s,%s,%s,%s,%s)", (
                                                         self.address_var.get(),
                                                         self.nw3_var.get(),
                                                         self.mstawa_var.get(),
                                                         self.phone_var.get(),
                                                         self.email_var.get(),
                                                         self.name_var.get(),
                                                         self.id_var.get()
                                                            ))
        con.commit()
        self.fetch_all()
        self.clear()
        con.close()
  
    def fetch_all(self):
        con  = pymysql.connect(
        host='localhost', user='root', password='', database='stude')
        cur  = con.cursor()
        cur.execute('select * from students1')
        rows = cur.fetchall()
        if len (rows) !=0:
              self.student_table.delete(*self.student_table.get_children())
              for row in rows:
               self.student_table.insert("",END,value=row)
               con.commit()
        con.close()
    
    
    def delet(self):
        con  = pymysql.connect(host='localhost', user='root', password='', database='stude')
        cur  = con.cursor()
        cur.execute('DELETE FROM students1 WHERE id= %s',self.delst_var.get())
        con.commit()
        self.fetch_all()
        con.close()

    def clear(self):
        self.id_var.set('')
        self.name_var.set('')
        self.email_var.set('')
        self.address_var.set('')
        self.nw3_var.set('')
        self.phone_var.set('')
        self.mstawa_var.set('')


    def get_cursor(self,ev):
        cursor_row =self.student_table.focus()
        content = self.student_table.item(cursor_row)
        row = content['values']
        self.address_var.set(row[0])
        self.nw3_var.set(row[1])
        self.mstawa_var.set(row[2])
        self.phone_var.set(row[3])
        self.email_var.set(row[4])
        self.name_var.set(row[5])
        self.id_var.set(row[6])
 
    def edit_tab(self):
        con = pymysql.connect(
        host='localhost', user='root', password='', database='stude')
        cur = con.cursor()
        cur.execute("UPDATE `students1` SET `address`='%s',`nw3`='%s',`mstawa`='%s',`phone`='%s',`email`='%s',`name`='%s',WHERE `id`='%s'  ", (
                                                         self.address_var.get(),
                                                         self.nw3_var.get(),
                                                         self.mstawa_var.get(),
                                                         self.phone_var.get(),
                                                         self.email_var.get(),
                                                         self.name_var.get(),
                                                         self.id_var.get()
                                                           ))
        con.commit()
        self.fetch_all()
        self.clear()
        con.close()


root = Tk()
ob = Student(root)

root.mainloop()
