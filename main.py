import string

from kivy.graphics import Rectangle
from kivy.input.providers.mouse import Color
from kivy.properties import StringProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.layout import Layout
from kivy.uix.scrollview import ScrollView

from kivymd.app import MDApp

from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDFillRoundFlatButton

from kivymd.uix.card import MDCard
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.label import MDLabel
from textblob import TextBlob
import psycopg2


class Login(Screen):
    pass


class LoginUser(Screen):
    pass


class LoginAdmin(Screen):
    pass


class MainUser(Screen):
    pass


class MainAdmin(Screen):
    pass


class ProductList(Screen):
    def __init__(self, **kwargs):
        super(ProductList, self).__init__(**kwargs)
        self.cols = 2
        self.size_hint_y = None
        self.height = 5000


class Main(MDApp):



    text = StringProperty('-.text')

    def chek_adminpassword(self):
        scrn = self.root.get_screen("LoginAdmin")
        name = scrn.ids.adname.text
        password = scrn.ids.adpassword.text
        if name == "admin" and password == "admin":
            self.root.current = "MainAdmin"
            scrn.ids.adname.text = ""
            scrn.ids.adpassword.text = ""
        else:
            scrn.ids.adname.text = ""
            scrn.ids.adpassword.text = ""

    def chek_user(self):
        self.root.current = "MainUser"

    def chek(self):

        scrn = self.root.get_screen("MainUser")
        scrn.ids.x.add_widget(MDLabel(text="fawzi"))

    def x(self, text, id, avit):
        scrn = self.root.get_screen("MainUser")
        user = (scrn.ids.userid.text.split("  "))[3]
        username = (scrn.ids.userid.text.split("  "))[1]
        txt = username + " : " + text
        idd = id
        scrn = self.root.get_screen("MainUser")
        md = MDLabel(text=txt, size_hint=(0.6, None), md_bg_color=(0, 0, 0, 0.2), color=(1, 1, 1, 1))
        import psycopg2

        connection = psycopg2.connect(user="postgres",
                                      password="12345678",
                                      host="localhost",
                                      port="5432",
                                      database="Project")
        connection.autocommit = True

        cursor = connection.cursor()
        sql = '''INSERT INTO public.commentaire(comment, "user", product,username) VALUES (%s,%s,%s,%s);'''
        vals = (text, user, avit, username)

        cursor.execute(sql, vals)
        connection.commit()

        connection.close()

        scrn.ids[idd].add_widget(md)

    def add_user(self):
        scrn = self.root.get_screen("MainAdmin")
        firstname = scrn.ids.firstname.text
        lastname = scrn.ids.lastname.text
        cin = scrn.ids.cin.text
        username = scrn.ids.username.text
        password = scrn.ids.password.text
        import psycopg2

        connection = psycopg2.connect(user="postgres",
                                      password="12345678",
                                      host="localhost",
                                      port="5432",
                                      database="Project")
        connection.autocommit = True

        cursor = connection.cursor()
        sql = 'SELECT cin FROM public."user";'

        cursor.execute(sql)

        cins = []
        mobile_records = cursor.fetchone()
        while mobile_records:
            cins.append(mobile_records[0])
            mobile_records = cursor.fetchone()
        if cin != "":
            a = int(cin) in cins

        if firstname != "" and lastname != "" and not a and username != "" and password != "":

            scrn = self.root.get_screen("MainAdmin")

            txt = "FirstName  :  " + firstname + "\n\nLastName :  " + lastname + "\n\nCin Number  :  " + str(
                cin) + " \n "
            lb = Button(text=txt, size_hint=(0.5, None), height="300dp", background_color=(1, 0, 0, 0.7))
            scrn.ids.userr.add_widget(lb)

            rqt = '''INSERT INTO public."user"(cin, firstname, lastname, username, password) VALUES (%s,%s,%s,%s,%s);'''
            val = (cin, firstname, lastname, username, password)
            cursor.execute(rqt, val)
            scrn.ids.firstname.text = ""
            scrn.ids.lastname.text = ""
            scrn.ids.cin.text = ""
            scrn.ids.username.text = ""
            scrn.ids.password.text = ""

            connection.commit()

            connection.close()
        else:
            connection.commit()

            connection.close()

    def delete_user(self):
        scrn = self.root.get_screen("MainAdmin")
        cin = scrn.ids.cin.text
        import psycopg2

        connection = psycopg2.connect(user="postgres",
                                      password="12345678",
                                      host="localhost",
                                      port="5432",
                                      database="Project")
        connection.autocommit = True

        cursor = connection.cursor()
        sql1 = '''DELETE FROM public."user" WHERE cin = '%s';'''
        connection.autocommit = True

        sql2 = 'SELECT cin FROM public."user";'

        cursor.execute(sql2)

        cins = []
        mobile_records = cursor.fetchone()
        while mobile_records:
            cins.append(mobile_records[0])
            mobile_records = cursor.fetchone()
        if len(cin) != 0:
            a = int(cin) in cins
        else:
            a = False
        if a:
            cursor.execute('''DELETE FROM public."user" WHERE cin = ''' + cin + ''';''')
            scrn.ids.cin.text = ""
            connection.commit()

            connection.close()
        else:
            connection.commit()

            connection.close()

    def add_user_MainAdmin(self, bool):
        scr = self.root.get_screen("LoginAdmin")
        if bool == "True":

            scrn = self.root.get_screen("MainAdmin")
            import psycopg2

            connection = psycopg2.connect(user="postgres",
                                          password="12345678",
                                          host="localhost",
                                          port="5432",
                                          database="Project")
            connection.autocommit = True

            cursor = connection.cursor()
            sql = 'SELECT * FROM public."user";'
            connection.autocommit = True
            cursor.execute(sql)
            user = cursor.fetchone()

            while user:
                firstname = user[1]
                lastname = user[2]
                cin = user[0]
                txt = "FirstName  :  " + firstname + "\n\nLastName :  " + lastname + "\n\nCin Number  :  " + str(
                    cin) + " \n "
                lb = Button(text=txt, size_hint=(0.5, None), height="300dp", background_color=(1, 0, 0, 0.7))
                user = cursor.fetchone()

                scrn.ids.userr.add_widget(lb)
            scr.ids.admn.bool = "False"
            connection.commit()

            connection.close()

    def check_user_password(self):
        import psycopg2

        connection = psycopg2.connect(user="postgres",
                                      password="12345678",
                                      host="localhost",
                                      port="5432",
                                      database="Project")
        connection.autocommit = True

        cursor = connection.cursor()
        sql = 'SELECT username , password,cin FROM public."user";'
        connection.autocommit = True
        cursor.execute(sql)
        user = cursor.fetchone()
        scr = self.root.get_screen("LoginUser")
        usname = scr.ids.usname.text
        uspassword = scr.ids.uspassword.text
        if usname != "" and uspassword != "":
            while user:
                username = user[0]
                password = user[1]
                uscin = user[2]

                user = cursor.fetchone()

                if usname == username and password == uspassword:
                    self.root.current = "MainUser"
                    scrn = self.root.get_screen("MainUser")
                    scrn.ids.userid.text = "WELCOME USER  " + username.upper() + "  CIN_NUMBER  " + str(uscin)
                    scr.ids.usname.text = ""
                    scr.ids.uspassword.text = ""

        connection.commit()
        connection.close()

    def addd_comment(self, x):
        if x == "True":
            import psycopg2

            connection = psycopg2.connect(user="postgres",
                                          password="12345678",
                                          host="localhost",
                                          port="5432",
                                          database="Project")
            connection.autocommit = True

            cursor = connection.cursor()
            sql1 = 'SELECT comment , "user",product,username FROM public."commentaire";'
            cursor.execute(sql1)
            cmt = cursor.fetchone()
            scr = self.root.get_screen("MainUser")
            print(cmt)
            while cmt:
                comment = cmt[0]
                user = cmt[1]
                product = cmt[2]
                username = cmt[3]
                print(comment, user, product, username)
                txt = cmt[3].upper() + " : " + comment
                md = MDLabel(text=txt, size_hint=(0.6, None), md_bg_color=(0, 0, 0, 0.2), text_color=(1, 1, 1, 1))

                scr.ids[product[:2]].add_widget(md)

                cmt = cursor.fetchone()

            sr = self.root.get_screen("LoginUser")
            sr.ids.true.bool = "False"

            connection.commit()
            connection.close()

    def Refresh(self):
        import psycopg2

        connection = psycopg2.connect(user="postgres",
                                      password="12345678",
                                      host="localhost",
                                      port="5432",
                                      database="Project")
        connection.autocommit = True

        cursor = connection.cursor()
        alphabet_string = string.ascii_lowercase
        ids = list(alphabet_string)

        for i in ids:

            sql1 = 'SELECT  comment, product FROM public.commentaire where product = \'' + str((i * 3)) + '\';'
            cursor.execute(sql1)
            cmt = cursor.fetchone()
            f = open("text.txt", "w+")
            while cmt:
                comment = cmt[0]

                f.write(comment + '\n')

                cmt = cursor.fetchone()
            f.close()
            f = open('text.txt', 'r')
            file = f.read()
            blob = TextBlob(file)
            sentiment = blob.sentiment.polarity
            src = self.root.get_screen('MainUser')
            x=9*(sentiment+1)/2 +1
            src.ids[(i * 3)].text = 'avis :'+str(x)[:3]
            f.close()

        connection.commit()
        connection.close()


Main().run()
