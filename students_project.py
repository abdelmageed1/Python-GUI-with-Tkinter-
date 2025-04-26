from tkinter import *
from tkinter import ttk
from database import  db



class StudentApp:
    def __init__(self, root):
        self.root = root
        self.root.state('zoomed')
        self.root.title("نظام إدارة الطلاب")
        self.root.configure(bg='#f0f4f7')
        self.root.resizable(False, True)

        self.primary_color = '#1a2b4c'
        self.accent_color = '#4a90e2'
        self.button_color = '#357ABD'
        self.button_fg = 'white'
        self.entry_bg = 'white'

        self.setup_title()
        self.setup_form_frame()
        self.setup_control_panel()
        self.setup_search_bar()
        self.setup_details_section()

        self.db = db.DatabaseManager()
        self.refresh()


    def setup_title(self):
        title_label = Label(
            self.root,
            text="[ نظام تسجيل الطلاب ]",
            font=("Arial", 20, "bold"),
            bg=self.primary_color,
            fg='white'
        )
        title_label.pack(fill='x', ipadx=10, ipady=10)

    def setup_form_frame(self):
        form_frame = Frame(self.root, bg='#ffffff', bd=1, relief=SOLID)
        form_frame.place(x=950, y=80, width=320, height=480)

        Label(form_frame, text="بيانات الطالب", font=("Arial", 16, "bold"), bg='white', fg=self.primary_color).pack(pady=10)

        self.entries = {}
        fields = ["الرقم القومي", "اسم الطالب", "الإيميل", "رقم الموبايل", "عنوان الطالب"]
        for field in fields:
            self.create_labeled_entry(form_frame, field)

        # الجنس
        global gender_combo
        Label(form_frame, text="نوع الطالب", font=("Arial", 13), bg='white', fg='black').pack(pady=(10, 2))
        self.gender_var = StringVar()
        gender_combo = ttk.Combobox(
            form_frame,
            values=["ذكر", "أنثى"],
            textvariable=self.gender_var,
            state="readonly",
            font=("Arial", 12),
            justify="center"
        )
        gender_combo.pack(pady=5)
        gender_combo.current(0)

    def setup_control_panel(self):
        control_frame = Frame(self.root, bg='#ffffff', bd=1, relief=SOLID)
        control_frame.place(x=950, y=580, width=320, height=350)

        Label(control_frame, text="لوحة التحكم", font=("Arial", 16, "bold"),
              bg=self.primary_color, fg='white').pack(fill='x', ipady=10)

        buttons = [
            ("أضافة طالب جديد", self.addStd),
            ("تعديل بيانات طالب", self.dummy_action),
            ("افراغ الحقول", self.dummy_action),
            ("من نحن", self.dummy_action),
            ("إغلاق البرنامج", self.root.quit),
        ]

        for text, cmd in buttons:
            Button(control_frame, text=text, command=cmd,
                   bg=self.button_color, fg=self.button_fg,
                   font=("Arial", 13), width=25, pady=2,
                   bd=0, cursor="hand2").pack(pady=12)



    def refresh(self):

            # تنظيف الجدول الأول
            for item in tree.get_children():
                tree.delete(item)

            # تحميل الطلاب من الداتابيز
            students = self.db.fetch_all_students()
            for student in students:
                # بنعرض القيم المطلوبة فقط (وليس الـ id الداخلي)
                tree.insert("", "end", values=(student[2], student[1], student[6], student[3], student[4]))

    def setup_search_bar(self):
        search_frame = Frame(self.root, bg='white', bd=1, relief=SOLID)
        search_frame.place(x=30, y=80, width=880, height=80)

        Label(search_frame, text="البحث عن طالب", font=("Arial", 14, "bold"),
              bg='white', fg=self.primary_color).grid(row=0, column=0, padx=10, pady=20)

        self.search_var = StringVar()
        search_combo = ttk.Combobox(
            search_frame,
            values=['الرقم القومي', "الاسم", "الإيميل", "رقم الموبايل"],
            textvariable=self.search_var,
            state="readonly",
            font=("Arial", 12),
            justify="center"
        )
        search_combo.grid(row=0, column=1, padx=10)
        search_combo.current(0)

        Entry(search_frame, width=30, font=("Arial", 12)).grid(row=0, column=2, padx=20)

        Button(search_frame, text="بحث", font=("Arial", 12, "bold"),
               bg=self.accent_color, fg='white',
               bd=0, padx=15, pady=6, cursor="hand2").grid(row=0, column=3, padx=10)

        btn_refresh = Button(search_frame, text="تحديث",
                             font=("Arial", 12, "bold"),
                             bg=self.accent_color, fg='white',
                              bd=0, padx=15, pady=6, cursor="hand2" , command=self.refresh).grid(row=0, column=3, padx=10)



    def create_labeled_entry(self, parent, label_text):
        Label(parent, text=label_text, font=("Arial", 13), bg='white', fg='black').pack(pady=(10, 2))
        entry = Entry(parent, width=30, font=("Arial", 12), bg=self.entry_bg)
        entry.pack(ipady=5)
        self.entries[label_text] = entry

    def addStd(self):
        std_info=[]
        for lab , ent in   self.entries.items() :

          std_info.append(ent.get())
        std_info.append(gender_combo.get())
        self.db.insert_student(national_id=std_info[0], name=std_info[1], email=std_info[2], phone=std_info[3], address=std_info[4], gender=std_info[5])

    def dummy_action(self):
        pass

    """
  1234567890 ال
اسم الطالب ali
الإيميل aaaaaa@
رقم الموبايل 012303334
عنوان الطالب carit
gender  ذكر

national_id, name, email, phone, address, gender
===


    """

#         frame4 عرض التفاصيل\
    def setup_details_section(self):
        frame4 = Frame(self.root, bg='white', bd=1, relief=SOLID)
        frame4.place(x=30, y=170, width=880, height=780)

        global  tree
        columns = ("الاسم", "الرقم القومى", "النوع", "الاميل", "رقم الموبايل")
        tree = ttk.Treeview(frame4, columns=columns, show="headings", height=8)

        # تعريف رؤوس الأعمدة
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor=CENTER)

        # Scrollbars
        scrollbar_v = Scrollbar(frame4, orient="vertical", command=tree.yview)
        scrollbar_h = Scrollbar(frame4, orient="horizontal", command=tree.xview)

        tree.configure(yscrollcommand=scrollbar_v.set, xscrollcommand=scrollbar_h.set)

        # ترتيب العناصر داخل الفريم
        scrollbar_v.pack(side="right", fill="y")
        scrollbar_h.pack(side="bottom", fill="x")
        tree.pack(side="left", fill="both", expand=True)

    # def add_entry(self):
    #     getDataFromEntries = {}
    #     for i in ent
    #     name = entry_name.get()
    #     age = entry_age.get()
    #
    #     if name and age:
    #         tree.insert("", "end", values=(name, age))
    #         entry_name.delete(0, tk.END)
    #         entry_age.delete(0, tk.END)
    #     else:
    #         messagebox.showwarning("تحذير", "الرجاء إدخال الاسم والعمر")

if __name__ == "__main__":
    root = Tk()
    app = StudentApp(root)
    root.mainloop()
