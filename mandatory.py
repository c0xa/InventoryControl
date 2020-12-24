import psycopg2 
from tkinter import *
from tkinter import messagebox
from tkinter.scrolledtext import Scrollbar
import tkinter.ttk as ttk
from tkinter.ttk import Combobox
import time
import tkinter as tk

class win:
    personset = []
    productset = []
    expenditureinvoiceset = []
    receiptinvoiceset = []

class Table(tk.Frame):
    def __init__(self, parent=None, headings=tuple(), rows=tuple()):
        super().__init__(parent)

        table = ttk.Treeview(self, show="headings", selectmode="browse")
        table["columns"]=headings
        table["displaycolumns"]=headings

        for head in headings:
            table.heading(head, text=head, anchor=tk.CENTER)
            table.column(head, anchor=tk.CENTER)

        for row in rows:
            table.insert('', tk.END, values=tuple(row))

        scrolltable = tk.Scrollbar(self, command=table.yview)
        table.configure(yscrollcommand=scrolltable.set)
        scrolltable.pack(side=tk.RIGHT, fill=tk.Y)
        table.pack(expand=tk.YES, fill=tk.BOTH)


def maindory(conn):

    #conn = psycopg2.connect(dbname='postgres', user='postgres', password='12345', host='localhost', port='5433')

    # conn = psycopg2.connect(dbname='pg_default', user='postgres',
    #  password='12345', host='1663')
    cursor = conn.cursor()
    root = Tk()
    root.geometry("1600x700+0+0")
    root.title("Inventory Control")
    # root.iconbitmap("payment_option_icon_150162.ico")
    Tops = Frame(root, bg="white", width=1600, height=700, relief=SUNKEN)
    Tops.pack(side=TOP)

    # f1 = Frame(root, width = 1300,height=700, relief=SUNKEN)
    # f1.pack(side=LEFT)

    f2 = Frame(root, width=50, height=700, relief=SUNKEN)
    f2.pack(side=RIGHT)
    # ------------------TIME--------------
    localtime = time.asctime(time.localtime(time.time()))
    # -----------------INFO TOP------------
    lblinfo = Label(Tops, font=('aria', 30, 'bold'), text="Inventory Control", fg="steel blue", bd=10, anchor='w')
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(Tops, font=('aria', 20), text=localtime, fg="steel blue", anchor='w')
    lblinfo.grid(row=1, column=0)

    tab_control = ttk.Notebook(root, padding=(20,))
    tab_control.enable_traversal()
    tab1 = ttk.Frame(tab_control)
    tab2 = ttk.Frame(tab_control)
    tab3 = ttk.Frame(tab_control)
    tab4 = ttk.Frame(tab_control)
    tab5 = ttk.Frame(tab_control)
    tab6 = ttk.Frame(tab_control)
    tab7 = ttk.Frame(tab_control)
    tab8 = ttk.Frame(tab_control)
    tab9 = ttk.Frame(tab_control)
    tab10 = ttk.Frame(tab_control)
    tab11 = ttk.Frame(tab_control)
    tab12 = ttk.Frame(tab_control)

    def updateDatepersonset():
        cursor.execute("SELECT idperson, firstname, secondname, patronymic from person")
        rows = cursor.fetchall()
        win.personset = []
        for row in rows:
            win.personset.append(str(
                str(row[0]) + " ,firstname=" + str(row[1]) + " ,secondname= " + str(row[2]) + " ,patronymic=" + str(
                    row[3])))

    def updateDateproductset():
        cursor.execute("SELECT idproduct, codeproduct, nameproduct from product")
        rows = cursor.fetchall()
        win.productset = []
        for row in rows:
            win.productset.append(str(str(row[0]) + " ,codeproduct=" + str(row[1]) + " ,nameproduct=" + str(row[2])))

    def updateDateexpenditureinvoiceset():
        cursor.execute("SELECT idexpenditure, DateEI , CountEI , CodePersonEI, CodeProductEI from expenditureinvoice")
        rows = cursor.fetchall()
        win.expenditureinvoiceset = []
        for row in rows:
            win.expenditureinvoiceset.append(str(
                str(row[0]) + " ,date=" + str(row[1]) + " ,count=" + str(row[2]) + " ,CodePerson=" + str(
                    row[3]) + " ,codeproduct=" + str(row[4])))

    def updateDatereceiptinvoiceset():
        cursor.execute("SELECT idreceipt, DateRI, CountRI, CodePersonRI , CodeProductRI from receiptinvoice")
        rows = cursor.fetchall()
        win.receiptinvoiceset = []
        for row in rows:
            win.receiptinvoiceset.append(
                str(str(row[0]) + " ,date=" + str(row[1]) + " ,count=" + str(row[2]) + " ,CodePerson=" + str(
                    row[3]) + " ,codeproduct=" + str(row[4])))

    updateDatepersonset()
    updateDateproductset()
    updateDateexpenditureinvoiceset()
    updateDatereceiptinvoiceset()

    def addPerson():
        cursor.execute("CALL insert_data(%s, %s, %s);", (First_name.get(), Second_name.get(), Patronymic.get()))
        conn.commit()
        messagebox.showinfo("Success",
                            (First_name.get()) + " " + Second_name.get() + " " + Patronymic.get() + " added")
        updateDatepersonset()

    def addProduct():
        cursor.execute("SELECT idproduct from product")
        rows = cursor.fetchall()
        for row in rows:
            if (row[0] == int(Codeproduct.get())):
                messagebox.showinfo("Error",
                                    (Codeproduct.get()) + " was created")
                return (0)
        cursor.execute("CALL insert_product(%s, %s, %s);",
                       (int(Codeproduct.get()), Name_product.get(), float(Price.get())))
        conn.commit()
        messagebox.showinfo("Success",
                            (Codeproduct.get()) + " " + Name_product.get() + " added")
        updateDateproductset()

    def addEI():
        year = int(DateyearEI.get())
        month = int(DatemonthEI.get())
        day = int(DatedayEI.get())
        dateei = str(year) + '-' + str(month) + "-" + str(day)
        producttab = (productCode.get()).split()
        persontab = (personCode.get()).split()
        cursor.execute("SELECT idproduct, count, NameProduct  from product")
        rows = cursor.fetchall()
        for row in rows:
            if (row[0] == int(producttab[0])):
                if (row[1] < int(Number_of_goodsEI.get())):
                    messagebox.showinfo("Error",
                                        (Number_of_goodsEI.get() + " less than in stock"))
                    return (0)
                else:
                    Name_product = row[2]
        cursor.execute("call insert_expenditureinvoice (%s, %s, %s, %s)",
                       (dateei, int(Number_of_goodsEI.get()), int(persontab[0]), int(producttab[0])))
        conn.commit()
        messagebox.showinfo("Success",
                            (Name_product + " added"))

        updateDateexpenditureinvoiceset()
        updateDateproductset()

    def addRI():
        year = int(DateyearRI.get())
        month = int(DatemonthRI.get())
        day = int(DatedayRI.get())
        dateri = str(year) + '-' + str(month) + "-" + str(day)
        producttab2 = (productCode2.get()).split()
        persontab2 = (personCode2.get()).split()
        cursor.execute("call insert_ReceiptInvoice (%s, %s, %s, %s)",
                       (dateri, int(Number_of_goodsRI.get()), int(persontab2[0]), int(producttab2[0])))
        conn.commit()
        messagebox.showinfo("Success",
                            ("added"))
        updateDatereceiptinvoiceset()
        updateDateproductset()

    def DeletePerson():
        persontab3 = (personCode3.get()).split()
        cursor.execute("call delete_data (" +
                       (persontab3[0]) + ")")
        conn.commit()
        messagebox.showinfo("Success",
                            ("deleted"))
        updateDatepersonset()
        updateDatereceiptinvoiceset()
        updateDateexpenditureinvoiceset()

    def DeleteProduct():
        producttab3 = (productCode3.get()).split()
        cursor.execute("call delete_product (" + producttab3[0] + ");")
        conn.commit()
        messagebox.showinfo("Success",
                            ("deleted"))
        updateDateproductset()
        updateDatereceiptinvoiceset()
        updateDateexpenditureinvoiceset()

    def Deleteexpenditureinvoice():
        expenditureinvoicetab = (expenditureinvoiceCode.get()).split()

        cursor.execute("call delete_expenditureinvoice (" +
                       expenditureinvoicetab[0] + ")")
        conn.commit()
        messagebox.showinfo("Success",
                            ("deleted"))
        updateDateexpenditureinvoiceset()

    def Deletereceiptinvoice():
        receiptinvoicetab = (receiptinvoiceCode.get()).split()
        cursor.execute("call delete_ReceiptInvoice (" +
                       receiptinvoicetab[0] + ")")
        conn.commit()
        messagebox.showinfo("Success",
                            ("deleted"))
        updateDatereceiptinvoiceset()

    def editPerson():
        persontab4 = (personCode4.get()).split()
        cursor.execute("call edit_person ('" + First_name_new.get() + "', '" + Second_name_new.get()
                       + "', '" + Patronymic_new.get() + "', " + persontab4[0] + ")")
        conn.commit()
        messagebox.showinfo("Success",
                            (
                                First_name_new.get()) + " " + Second_name_new.get() + " " + Patronymic_new.get() + " edited")
        updateDatepersonset()
        updateDatereceiptinvoiceset()
        updateDateexpenditureinvoiceset()

    def editProduct():
        producttab4 = (productCode4.get()).split()
        cursor.execute("call edit_product ('" + Codeproduct_new.get() + "', '" + Name_product_new.get()
                       + "', '" + Price_new.get() + "', " + producttab4[0] + ")")
        conn.commit()
        messagebox.showinfo("Success",
                            (Codeproduct_new.get()) + " " + Name_product_new.get() + " edited")
        updateDateproductset()
        updateDatereceiptinvoiceset()
        updateDateexpenditureinvoiceset()

    def editEI():
        year = int(DateyearEI_new.get())
        month = int(DatemonthEI_new.get())
        day = int(DatedayEI_new.get())
        dateei = str(year) + '-' + str(month) + "-" + str(day)
        cursor = conn.cursor()

        producttab2 = (productCode5.get()).split()
        persontab2 = (personCode5.get()).split()
        expenditureinvoicetab2 = (expenditureinvoiceCode2.get()).split()
        cursor.execute("call edit_expenditureinvoice (%s, %s, %s, %s, %s)",
                       (dateei, int(Number_of_goodsEI_new.get()), int(persontab2[0]), int(producttab2[0]),
                        int(expenditureinvoicetab2[0])))
        conn.commit()
        messagebox.showinfo("Success",
                            (expenditureinvoicetab2[0] + " edited"))

        updateDateexpenditureinvoiceset()

    def editRI():
        year = int(DateyearRI_new.get())
        month = int(DatemonthRI_new.get())
        day = int(DatedayRI_new.get())
        dateri = str(year) + '-' + str(month) + "-" + str(day)
        producttab3 = (productCode6.get()).split()
        persontab3 = (personCode6.get()).split()
        receiptinvoicetab2 = (receiptinvoiceCode2.get()).split()
        cursor.execute("call edit_ReceiptInvoice (%s, %s, %s, %s, %s)",
                       (dateri, int(Number_of_goodsRI_new.get()), int(persontab3[0]), int(producttab3[0]),
                        int(receiptinvoicetab2[0])))

        conn.commit()
        messagebox.showinfo("Success",
                            (receiptinvoicetab2[0] + " edited"))
        updateDatereceiptinvoiceset()

    def changePerson():
        personCode["values"] = win.personset
        personCode2["values"] = win.personset
        personCode3["values"] = win.personset
        personCode4["values"] = win.personset
        personCode5["values"] = win.personset
        personCode6["values"] = win.personset

    def changeProduct():
        productCode["values"] = win.productset
        productCode2["values"] = win.productset
        productCode3["values"] = win.productset
        productCode4["values"] = win.productset
        productCode5["values"] = win.productset
        productCode6["values"] = win.productset

    def changeEI():
        expenditureinvoiceCode["values"] = win.expenditureinvoiceset
        expenditureinvoiceCode2["values"] = win.expenditureinvoiceset

    def changeRI():
        receiptinvoiceCode["values"] = win.receiptinvoiceset
        receiptinvoiceCode2["values"] = win.receiptinvoiceset

    # --------------------------------------------------------------------------------------
    # addPerson
    # tab1

    First_name = StringVar()
    Second_name = StringVar()
    Patronymic = StringVar()

    lblreference = Label(tab1, font=('aria', 16, 'bold'), text="First name", fg="steel blue", bd=10, anchor='w').pack()

    txtreference = Entry(tab1, font=('ariel', 16, 'bold'), textvariable=First_name, bd=6, insertwidth=4,
                         bg="powder blue", justify='right').pack()

    lblfries = Label(tab1, font=('aria', 16, 'bold'), text="Second name", fg="steel blue", bd=10, anchor='w').pack()

    txtfries = Entry(tab1, font=('ariel', 16, 'bold'), textvariable=Second_name, bd=6, insertwidth=4, bg="powder blue",
                     justify='right').pack()

    lblLargefries = Label(tab1, font=('aria', 16, 'bold'), text="Patronymic", fg="steel blue", bd=10, anchor='w').pack()

    txtLargefries = Entry(tab1, font=('ariel', 16, 'bold'), textvariable=Patronymic, bd=6, insertwidth=4,
                          bg="powder blue", justify='right').pack()

    btnTotal = Button(tab1, padx=16, pady=8, bd=10, fg="black", font=('ariel', 11, 'bold'), width=10, text="Add",
                      bg="powder blue", command=addPerson).pack()

    # --------------------------------------------------------------------------------------
    # addProduct
    # tab4
    # --------------------------------------------------------------------------------------
    Name_product = StringVar()
    Codeproduct = StringVar()
    Price = StringVar()

    lblreference = Label(tab4, font=('aria', 16, 'bold'), text="Code product", fg="steel blue", bd=10,
                         anchor='w').pack()

    txtreference = Entry(tab4, font=('ariel', 16, 'bold'), textvariable=Codeproduct, bd=6, insertwidth=4,
                         bg="powder blue", justify='right').pack()

    lblreference = Label(tab4, font=('aria', 16, 'bold'), text="Name product", fg="steel blue", bd=10,
                         anchor='w').pack()

    txtreference = Entry(tab4, font=('ariel', 16, 'bold'), textvariable=Name_product, bd=6, insertwidth=4,
                         bg="powder blue", justify='right').pack()

    lblfries = Label(tab4, font=('aria', 16, 'bold'), text="Price", fg="steel blue", bd=10, anchor='w').pack()

    txtfries = Entry(tab4, font=('ariel', 16, 'bold'), textvariable=Price, bd=6, insertwidth=4, bg="powder blue",
                     justify='right').pack()

    btnTotal = Button(tab4, padx=16, pady=8, bd=10, fg="black", font=('ariel', 11, 'bold'), width=10, text="Add",
                      bg="powder blue", command=addProduct).pack()

    # --------------------------------------------------------------------------------------
    # addEI
    # tab7
    # --------------------------------------------------------------------------------------

    DateyearEI = StringVar()
    DatemonthEI = StringVar()
    DatedayEI = StringVar()
    Number_of_goodsEI = StringVar()

    personCode = Combobox(tab7, values=win.personset, postcommand=changePerson, width=100)
    productCode = Combobox(tab7, values=win.productset, postcommand=changeProduct, width=100)
    Label(tab7, font=('aria', 16, 'bold'), text="Person", fg="steel blue", bd=10, anchor='w').pack()
    personCode.pack()
    Label(tab7, font=('aria', 16, 'bold'), text="Product", fg="steel blue", bd=10, anchor='w').pack()
    productCode.pack()
    Label(tab7, font=('aria', 16, 'bold'), text="Year", fg="steel blue", bd=10, anchor='w').pack()

    Entry(tab7, font=('ariel', 16, 'bold'), textvariable=DateyearEI, bd=6, insertwidth=4, bg="powder blue",
          justify='right').pack()

    Label(tab7, font=('aria', 16, 'bold'), text="Month", fg="steel blue", bd=10, anchor='w').pack()

    Entry(tab7, font=('ariel', 16, 'bold'), textvariable=DatemonthEI, bd=6, insertwidth=4, bg="powder blue",
          justify='right').pack()

    Label(tab7, font=('aria', 16, 'bold'), text="Day", fg="steel blue", bd=10, anchor='w').pack()
    Entry(tab7, font=('ariel', 16, 'bold'), textvariable=DatedayEI, bd=6, insertwidth=4, bg="powder blue",
          justify='right').pack()

    Label(tab7, font=('aria', 16, 'bold'), text="Number of goods", fg="steel blue", bd=10, anchor='w').pack()
    Entry(tab7, font=('ariel', 16, 'bold'), textvariable=Number_of_goodsEI, bd=6, insertwidth=4, bg="powder blue",
          justify='right').pack()

    Button(tab7, padx=16, pady=8, bd=10, fg="black", font=('ariel', 11, 'bold'), width=10, text="Add", bg="powder blue",
           command=addEI).pack()

    # --------------------------------------------------------------------------------------
    # addRI
    # tab10
    # --------------------------------------------------------------------------------------

    Number_of_goodsRI = StringVar()
    DateyearRI = StringVar()
    DatemonthRI = StringVar()
    DatedayRI = StringVar()
    Number_of_goodsRI = StringVar()
    personCode2 = Combobox(tab10, values=win.personset, postcommand=changePerson, width=100)
    productCode2 = Combobox(tab10, values=win.productset, postcommand=changeProduct, width=100)

    Label(tab10, font=('aria', 16, 'bold'), text="Person", fg="steel blue", bd=10, anchor='w').pack()
    personCode2.pack()
    Label(tab10, font=('aria', 16, 'bold'), text="Product", fg="steel blue", bd=10, anchor='w').pack()
    productCode2.pack()
    Label(tab10, font=('aria', 16, 'bold'), text="Year", fg="steel blue", bd=10, anchor='w').pack()

    Entry(tab10, font=('ariel', 16, 'bold'), textvariable=DateyearRI, bd=6, insertwidth=4, bg="powder blue",
          justify='right').pack()

    Label(tab10, font=('aria', 16, 'bold'), text="Month", fg="steel blue", bd=10, anchor='w').pack()

    Entry(tab10, font=('ariel', 16, 'bold'), textvariable=DatemonthRI, bd=6, insertwidth=4, bg="powder blue",
          justify='right').pack()

    Label(tab10, font=('aria', 16, 'bold'), text="Day", fg="steel blue", bd=10, anchor='w').pack()
    Entry(tab10, font=('ariel', 16, 'bold'), textvariable=DatedayRI, bd=6, insertwidth=4, bg="powder blue",
          justify='right').pack()

    Label(tab10, font=('aria', 16, 'bold'), text="Number of goods", fg="steel blue", bd=10, anchor='w').pack()
    Entry(tab10, font=('ariel', 16, 'bold'), textvariable=Number_of_goodsRI, bd=6, insertwidth=4, bg="powder blue",
          justify='right').pack()

    Button(tab10, padx=16, pady=8, bd=10, fg="black", font=('ariel', 11, 'bold'), width=10, text="Add",
           bg="powder blue", command=addRI).pack()

    # --------------------------------------------------------------------------------------
    # DeletePerson
    # tab3
    # --------------------------------------------------------------------------------------
    Label(tab3, font=('aria', 16, 'bold'), text="Person", fg="steel blue", bd=10, anchor='w').pack()

    personCode3 = Combobox(tab3, values=win.personset, postcommand=changePerson, width=100)
    personCode3.pack()

    btnTotal = Button(tab3, padx=16, pady=8, bd=10, fg="black", font=('ariel', 11, 'bold'), width=10, text="Delete",
                      bg="powder blue", command=DeletePerson).pack()

    # --------------------------------------------------------------------------------------
    # DeleteProduct
    # tab6
    # --------------------------------------------------------------------------------------
    Label(tab6, font=('aria', 16, 'bold'), text="Product", fg="steel blue", bd=10, anchor='w').pack()

    productCode3 = Combobox(tab6, values=win.productset, postcommand=changeProduct, width=100)
    productCode3.pack()

    btnTotal = Button(tab6, padx=16, pady=8, bd=10, fg="black", font=('ariel', 11, 'bold'), width=10, text="Delete",
                      bg="powder blue", command=DeleteProduct).pack()

    # --------------------------------------------------------------------------------------
    # Deleteexpenditureinvoice
    # tab9
    # --------------------------------------------------------------------------------------
    Label(tab9, font=('aria', 16, 'bold'), text="Expenditure invoice", fg="steel blue", bd=10, anchor='w').pack()
    expenditureinvoiceCode = Combobox(tab9, values=win.expenditureinvoiceset, postcommand=changeEI, width=100)

    expenditureinvoiceCode.pack()

    Button(tab9, padx=16, pady=8, bd=10, fg="black", font=('ariel', 16, 'bold'), width=10, text="Delete",
           bg="powder blue", command=Deleteexpenditureinvoice).pack()

    # --------------------------------------------------------------------------------------
    # Deletereceiptinvoice
    # tab12
    # --------------------------------------------------------------------------------------
    Label(tab12, font=('aria', 16, 'bold'), text="Receipt invoice", fg="steel blue", bd=10, anchor='w').pack()
    receiptinvoiceCode = Combobox(tab12, values=win.receiptinvoiceset, postcommand=changeRI, width=100)

    receiptinvoiceCode.pack()

    Button(tab12, padx=16, pady=8, bd=10, fg="black", font=('ariel', 11, 'bold'), width=10, text="Delete",
           bg="powder blue", command=Deletereceiptinvoice).pack()

    # --------------------------------------------------------------------------------------
    # editPerson
    # tab2
    # --------------------------------------------------------------------------------------

    First_name_new = StringVar()
    Second_name_new = StringVar()
    Patronymic_new = StringVar()

    Label(tab2, font=('aria', 16, 'bold'), text="Person", fg="steel blue", bd=10, anchor='w').pack()
    personCode4 = Combobox(tab2, values=win.personset, postcommand=changePerson, width=100)

    personCode4.pack()

    Label(tab2, font=('aria', 16, 'bold'), text="New first name", fg="steel blue", bd=10, anchor='w').pack()

    Entry(tab2, font=('ariel', 16, 'bold'), textvariable=First_name_new, bd=6, insertwidth=4, bg="powder blue",
          justify='right').pack()

    Label(tab2, font=('aria', 16, 'bold'), text="New second name", fg="steel blue", bd=10, anchor='w').pack()

    Entry(tab2, font=('ariel', 16, 'bold'), textvariable=Second_name_new, bd=6, insertwidth=4, bg="powder blue",
          justify='right').pack()

    Label(tab2, font=('aria', 16, 'bold'), text="New patronymic", fg="steel blue", bd=10, anchor='w').pack()

    Entry(tab2, font=('ariel', 16, 'bold'), textvariable=Patronymic_new, bd=6, insertwidth=4, bg="powder blue",
          justify='right').pack()

    Button(tab2, padx=16, pady=8, bd=10, fg="black", font=('ariel', 11, 'bold'), width=10, text="Edit",
           bg="powder blue", command=editPerson).pack()

    # --------------------------------------------------------------------------------------
    # editProduct
    # tab5
    # --------------------------------------------------------------------------------------
    Name_product_new = StringVar()
    Codeproduct_new = StringVar()
    Price_new = StringVar()

    Label(tab5, font=('aria', 16, 'bold'), text="Code product", fg="steel blue", bd=10, anchor='w').pack()
    productCode4 = Combobox(tab5, values=win.productset, postcommand=changeProduct, width=100)

    productCode4.pack()

    Label(tab5, font=('aria', 16, 'bold'), text="New code product", fg="steel blue", bd=10, anchor='w').pack()

    Entry(tab5, font=('ariel', 16, 'bold'), textvariable=Codeproduct_new, bd=6, insertwidth=4, bg="powder blue",
          justify='right').pack()

    Label(tab5, font=('aria', 16, 'bold'), text="New name product", fg="steel blue", bd=10, anchor='w').pack()

    Entry(tab5, font=('ariel', 16, 'bold'), textvariable=Name_product_new, bd=6, insertwidth=4, bg="powder blue",
          justify='right').pack()

    Label(tab5, font=('aria', 16, 'bold'), text="New price", fg="steel blue", bd=10, anchor='w').pack()

    Entry(tab5, font=('ariel', 16, 'bold'), textvariable=Price_new, bd=6, insertwidth=4, bg="powder blue",
          justify='right').pack()

    Button(tab5, padx=16, pady=8, bd=10, fg="black", font=('ariel', 11, 'bold'), width=10, text="Edit",
           bg="powder blue", command=editProduct).pack()

    # --------------------------------------------------------------------------------------
    # editEI
    # tab8
    # --------------------------------------------------------------------------------------

    DateyearEI_new = StringVar()
    DatemonthEI_new = StringVar()
    DatedayEI_new = StringVar()
    Number_of_goodsEI_new = StringVar()

    Label(tab8, font=('aria', 11, 'bold'), text="Expenditure invoice", fg="steel blue", bd=10, anchor='w').pack()

    expenditureinvoiceCode2 = Combobox(tab8, values=win.expenditureinvoiceset, postcommand=changeEI, width=100)

    expenditureinvoiceCode2.pack()

    Label(tab8, font=('aria', 11, 'bold'), text="Person", fg="steel blue", bd=10, anchor='w').pack()

    personCode5 = Combobox(tab8, values=win.productset, postcommand=changePerson, width=100)

    personCode5.pack()
    Label(tab8, font=('aria', 11, 'bold'), text="Product", fg="steel blue", bd=10, anchor='w').pack()
    productCode5 = Combobox(tab8, values=win.productset, postcommand=changeProduct, width=100)

    productCode5.pack()
    Label(tab8, font=('aria', 11, 'bold'), text="Year", fg="steel blue", bd=10, anchor='w').pack()

    Entry(tab8, font=('ariel', 11, 'bold'), textvariable=DateyearEI_new, bd=6, insertwidth=4, bg="powder blue",
          justify='right').pack()

    Label(tab8, font=('aria', 11, 'bold'), text="Month", fg="steel blue", bd=10, anchor='w').pack()

    Entry(tab8, font=('ariel', 11, 'bold'), textvariable=DatemonthEI_new, bd=6, insertwidth=4, bg="powder blue",
          justify='right').pack()

    Label(tab8, font=('aria', 11, 'bold'), text="Day", fg="steel blue", bd=10, anchor='w').pack()
    Entry(tab8, font=('ariel', 11, 'bold'), textvariable=DatedayEI_new, bd=6, insertwidth=4, bg="powder blue",
          justify='right').pack()

    Label(tab8, font=('aria', 11, 'bold'), text="Number of goods", fg="steel blue", bd=10, anchor='w').pack()
    Entry(tab8, font=('ariel', 11, 'bold'), textvariable=Number_of_goodsEI_new, bd=6, insertwidth=4, bg="powder blue",
          justify='right').pack()

    Button(tab8, padx=16, pady=8, bd=10, fg="black", font=('ariel', 11, 'bold'), width=10, text="Edit",
           bg="powder blue", command=editEI).pack()

    # --------------------------------------------------------------------------------------
    # addRI
    # tab11
    # --------------------------------------------------------------------------------------

    Number_of_goodsRI_new = StringVar()
    DateyearRI_new = StringVar()
    DatemonthRI_new = StringVar()
    DatedayRI_new = StringVar()
    productCode6 = Combobox(tab11, values=win.productset, postcommand=changeProduct, width=100)

    personCode6 = Combobox(tab11, values=win.productset, postcommand=changePerson, width=100)
    receiptinvoiceCode2 = Combobox(tab11, values=win.receiptinvoiceset, postcommand=changeRI, width=100)
    Label(tab11, font=('aria', 11, 'bold'), text="Receipt invoice", fg="steel blue", bd=10, anchor='w').pack()
    receiptinvoiceCode2.pack()
    Label(tab11, font=('aria', 11, 'bold'), text="Person", fg="steel blue", bd=10, anchor='w').pack()
    personCode6.pack()
    Label(tab11, font=('aria', 11, 'bold'), text="Product", fg="steel blue", bd=10, anchor='w').pack()
    productCode6.pack()
    Label(tab11, font=('aria', 11, 'bold'), text="Year", fg="steel blue", bd=10, anchor='w').pack()

    Entry(tab11, font=('ariel', 11, 'bold'), textvariable=DateyearRI_new, bd=6, insertwidth=4, bg="powder blue",
          justify='right').pack()

    Label(tab11, font=('aria', 11, 'bold'), text="Month", fg="steel blue", bd=10, anchor='w').pack()

    Entry(tab11, font=('ariel', 11, 'bold'), textvariable=DatemonthRI_new, bd=6, insertwidth=4, bg="powder blue",
          justify='right').pack()

    Label(tab11, font=('aria', 11, 'bold'), text="Day", fg="steel blue", bd=10, anchor='w').pack()
    Entry(tab11, font=('ariel', 11, 'bold'), textvariable=DatedayRI_new, bd=6, insertwidth=4, bg="powder blue",
          justify='right').pack()

    Label(tab11, font=('aria', 11, 'bold'), text="Number of goods", fg="steel blue", bd=10, anchor='w').pack()
    Entry(tab11, font=('ariel', 11, 'bold'), textvariable=Number_of_goodsRI_new, bd=6, insertwidth=4, bg="powder blue",
          justify='right').pack()

    Button(tab11, padx=16, pady=8, bd=10, fg="black", font=('ariel', 11, 'bold'), width=10, text="Edit",
           bg="powder blue", command=editRI).pack()

    # --------------------------------------------------------------------------------------
    tab_control.add(tab1, text='Add person')
    tab_control.add(tab2, text="Edit person")
    tab_control.add(tab3, text='Delete person')
    tab_control.add(tab4, text='Add product')
    tab_control.add(tab5, text="Edit product")
    tab_control.add(tab6, text='Delete product')
    tab_control.add(tab7, text='Add expenditure invoice')
    tab_control.add(tab8, text="Edit expenditure invoice")
    tab_control.add(tab9, text='Delete expenditure invoice')
    tab_control.add(tab10, text='Add receipt invoice')
    tab_control.add(tab11, text="Edit receipt invoice")
    tab_control.add(tab12, text='Delete receipt invoice')
    tab_control.pack(side=LEFT, expand=1, fill='both')

    def table1():
        roo = Tk()
        roo.geometry("1600x220+0+0")
        roo.title("2a")
        cursor.execute("SELECT nameproduct, price, dateei, countei, dateri, countri, count,"
                       "    CASE"
                       "        WHEN count = 0"
                       "            THEN 'END'"
                       "        WHEN count > 0"
                       "            THEN 'OK'"
                       "    END duration "
                       "FROM PRODUCT LEFT OUTER JOIN  ExpenditureInvoice ON (ExpenditureInvoice.CodeProductEI  = PRODUCT.idproduct) "
                       "LEFT OUTER JOIN receiptinvoice ON (receiptinvoice.CodeProductRI  = PRODUCT.idproduct)")

        rows = cursor.fetchall()
        table1 = []
        for row in rows:
            table1.append(row)
        table = Table(roo, headings=('Nameproduct', 'price', 'dateEI', 'countei', 'dateri', 'countri', 'count', 'duration'),
                      rows=table1)
        table.pack(expand=tk.YES, fill=tk.BOTH)
        roo.mainloop()

    def table2():
        roo2 = Tk()
        roo2.geometry("1600x220+0+0")
        roo2.title("Watch person")
        cursor.execute("SELECT * from person")

        rows = cursor.fetchall()
        table1 = []
        for row in rows:
            table1.append(row)
        table = Table(roo2, headings=(
            'Firstname', 'secondname', 'patronymic'),
                      rows=table1)
        table.pack(expand=tk.YES, fill=tk.BOTH)
        roo2.mainloop()

    def table3():
        roo3 = Tk()
        roo3.geometry("1600x220+0+0")
        roo3.title("2c")
        roo3.title("Watch product")
        cursor.execute("SELECT Codeproduct, nameproduct, price, count from product")

        rows = cursor.fetchall()
        table1 = []
        for row in rows:
            table1.append(row)
        table = Table(roo3, headings=(
            'Codeproduct', 'nameproduct', 'price', 'count'),
                      rows=table1)
        table.pack(expand=tk.YES, fill=tk.BOTH)
        roo3.mainloop()

    def table4():
        roo4 = Tk()
        roo4.geometry("1600x220+0+0")
        roo4.title("Watch expenditure invoice")
        cursor.execute("SELECT * from expenditureinvoice")

        rows = cursor.fetchall()
        table1 = []
        for row in rows:
            table1.append(row)
        table = Table(roo4, headings=(
            'idexpenditure', 'date', 'count', 'codeperson', 'codeproduct'),
                      rows=table1)
        table.pack(expand=tk.YES, fill=tk.BOTH)
        roo4.mainloop()

    def table5():
        roo5 = Tk()
        roo5.geometry("1600x220+0+0")
        roo5.title("Expenditure invoice")
        cursor.execute("SELECT * from receiptinvoice")

        rows = cursor.fetchall()
        table1 = []
        for row in rows:
            table1.append(row)
        table = Table(roo5, headings=(
            'idreceiptinvoice', 'date', 'count', 'codeperson', 'codeproduct'),
                      rows=table1)
        table.pack(expand=tk.YES, fill=tk.BOTH)
        roo5.mainloop()

    def qexit():
        root.destroy()

    Button(root, padx=16, pady=8, bd=10, fg="black", font=('ariel', 11, 'bold'), width=30, text="Watch person",
           bg="powder blue", command=table2).pack()
    Button(root, padx=16, pady=8, bd=10, fg="black", font=('ariel', 11, 'bold'), width=30, text="Watch product",
           bg="powder blue", command=table3).pack()
    Button(root, padx=16, pady=8, bd=10, fg="black", font=('ariel', 11, 'bold'), width=30,
           text="Watch expenditure invoice", bg="powder blue", command=table4).pack()
    Button(root, padx=16, pady=8, bd=10, fg="black", font=('ariel', 11, 'bold'), width=30,
           text="Watch receipt invoice", bg="powder blue", command=table5).pack()
    Button(root, padx=16, pady=8, bd=10, fg="black", font=('ariel', 11, 'bold'), width=30,
           text="Watch all invoice", bg="powder blue", command=table1).pack()
    Button(root, padx=16, pady=8, bd=10, fg="black", font=('ariel', 11, 'bold'), width=30, text="EXIT",
          bg="powder blue", command=qexit).pack()

    root.mainloop()

def go(loginto, passwordto,  rootmain):
    try:
        conn = psycopg2.connect(dbname='postgres', user=loginto.get(), password=passwordto.get(), host='localhost',
                                port='5433')
    except:
        messagebox.showinfo("Error",
                            ("Login or password are wrong"))
        return
    # conn = psycopg2.connect(dbname='pg_default', user='postgres',
    #  password='12345', host='1663')
    rootmain.destroy()
    maindory(conn)

def main():
    rootmain = Tk()
    loginto = StringVar()
    passwordto = StringVar()
    rootmain.title("Inventory Control")
    rootmain.geometry("500x400+200+200")
    Label(rootmain, font=('aria', 30, 'bold'), text="Inventory Control", fg="steel blue", bd=10, anchor='w').pack()
    Label(rootmain, font=('aria', 11, 'bold'), text="Login", fg="steel blue", bd=10, anchor='w').pack()
    Entry(rootmain, font=('ariel', 11, 'bold'), textvariable=loginto, bd=6, insertwidth=4, bg="powder blue",
        justify='right').pack()
    Label(rootmain, font=('aria', 11, 'bold'), text="Password", fg="steel blue", bd=10, anchor='w').pack()
    Entry(rootmain, font=('ariel', 11, 'bold'), textvariable=passwordto, bd=6, insertwidth=4, bg="powder blue",
          justify='right').pack()
    Label(rootmain, font=('aria', 10, 'bold'), text=" ", fg="steel blue", bd=1, anchor='w').pack()
    Button(rootmain, padx=16, pady=20, bd=10, fg="black", font=('ariel', 11, 'bold'), width=30, text="ENTRY",
          bg="powder blue", command=lambda: (go(loginto, passwordto, rootmain))).pack()
    rootmain.mainloop()
main()