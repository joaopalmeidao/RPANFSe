# ///////////////////////////////////////////////////////////////
#
# BY: JOAO PEDRO A. OLIVEIRA
#
# ///////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////
# IMPORT / MODULES
# ///////////////////////////////////////////////////////////////

from .manager import *
from tkinter.ttk import Treeview

# ///////////////////////////////////////////////////////////////
# GUI COLORS
# ///////////////////////////////////////////////////////////////

black = "#000000"
white = "#feffff"
blue = "#3032cf"
green = "#3fb5a3"
orange = "#FFA500"
grayblue = "#38576b"
grey = "#403d3d"

# ///////////////////////////////////////////////////////////////
# MAIN APP
# ///////////////////////////////////////////////////////////////


class App(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.resizable(width=False, height=False)
        self.iconbitmap(icon_folder + "rpa_ico.ico")
        self.title(f"{program_name} | {main_name}")
        self.configure(background=white)
        self.resizable(width=FALSE, height=FALSE)
        self.bind("<Escape>", self.on_closing_event)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def manager_init(self):
        data_window.destroy()
        self.withdraw()
        check = self.check_data()
        if check == True:
            time_spend = manager(user)
            self.deiconify()
            on_final(time_spend)
            self.main_window()
        else:
            pass

    def on_closing(self):
        exit()

    def on_closing_event(self, event):
        if messagebox.askokcancel(f"{program_name} | Quit", "Deseja sair?"):
            exit()

    def on_nfsedatasucess(self):
        notas_xml = get_db_data()
        if len(notas_xml) != 0:
            self.withdraw()
            self.data_window()

        else:
            if messagebox.showerror(f"{program_name} | Start", f"Nenhum dado foi gravado no BANCO DE DADOS!\n\nVerifique os arquivos na pasta 'arquivos'!"):
                pass

    def on_firststart(self):
        notas_xml = get_db_data()
        if len(notas_xml) != 0:
            self.withdraw()
            self.data_window()
        else:
            if messagebox.showinfo(f"{program_name} | Start", f"Nenhum dado no BANCO DE DADOS!\n\nClique em 'CARREGAR DADOS' para carregar os dados!"):
                pass

    def on_start(self):
        data_window.withdraw()
        self.deiconify()
        notas_xml = get_db_data()
        est_time = get_timetot()/get_filestot()
        if len(notas_xml) != 0:
            if messagebox.askokcancel(f"{program_name} | Start", f"Estima-se {int(est_time*len(notas_xml)/60)} minuto(s) para lançar as {len(notas_xml)} NFSe!\n\nDeseja iniciar o BOT?"):
                self.manager_init()
            else:
                self.withdraw()
                data_window.deiconify()

        else:
            if messagebox.showinfo(f"{program_name} | Start", f"Nenhum dado no BANCO DE DADOS!\n\nClique em 'CARREGAR DADOS' para carregar os dados!"):
                self.deiconify()

    def on_firststart_event(self, event):
        self.on_firststart()

    def on_start_event(self, event):
        self.on_start()

    def on_getdata(self):
        notas_xml = get_db_data()
        if len(notas_xml) != 0:
            if messagebox.askokcancel(f"{program_name} | GetData", f"Esse processo excluirá os dados gravados anteriormente!\n\nDeseja carregar os dados das NFSe na pasta 'arquivos'?"):
                if RENAME_FILES == True:
                    rename_file()
                else:
                    pass
                check = self.check_files(folder)
                if check == True:
                    self.withdraw()
                    nfse_data()
                    self.deiconify()
                    self.on_nfsedatasucess()
                else:
                    pass
        else:
            if messagebox.askokcancel(f"{program_name} | GetData", f"Deseja carregar os dados das NFSe na pasta 'arquivos'?"):
                if RENAME_FILES == True:
                    rename_file()
                else:
                    pass
                check = self.check_files(folder)
                if check == True:
                    self.withdraw()
                    nfse_data()
                    self.deiconify()
                    self.on_nfsedatasucess()
                else:
                    pass

    def on_getdata_event(self, event):
        self.on_getdata()

    def fhelp(self):
        wbb.open_new(whatsapp)
        exit()

    def check_data(self):
        notas_xml = get_db_data()
        if len(notas_xml) != 0:
            check = True
        else:
            check = False
        return check

    def check_files(self, folder):
        xmls_folder = get_xmlonfolder(folder)
        if xmls_folder != 0:
            check = True
            return check
        else:
            self.deiconify()
            if messagebox.showerror(f"{program_name} | {main_name}", """Nenhum arquivo .xml na pasta "arquivos"."""):
                check = False
                return check

    def clear_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

    def return_login(self):
        self.clear_frame()
        self.login_window()

    def get_last_user(self):
        last_user = cursor.execute(
            f"""
            SELECT user
            FROM last_user    
            """
        )
        last_user = cursor.fetchall()[0]
        return last_user

    def login_window(self):
        last_user = self.get_last_user()

        def users():
            try:
                users_config = cursor.execute(
                    f"""
                    SELECT user
                    FROM users    
                    """
                )
                users_config = cursor.fetchall()
            except:
                on_db_fail()
            users = []
            for i in users_config:
                i = str(i)
                i = i.split("'")
                i = i[1]
                users.append(i)
            return users

        def on_user_fail():
            if messagebox.showinfo(f"{program_name} | {main_name}", "Usuário não encontrado!"):
                pass

        def check_user():
            global user
            user = userentry.get()

            if user == help:
                self.fhelp()

            elif user in users():
                if user != last_user:
                    try:
                        cursor.execute(
                            f"""
                        DELETE FROM last_user
                        """
                        )
                        db.commit()
                    except:
                        on_db_fail()
                    try:
                        cursor.execute(
                            f"""
                        INSERT INTO last_user VALUES ('{user}')
                        """
                        )
                        db.commit()
                    except:
                        on_db_fail()
                else:
                    pass
                teste_login = get_user(user)
                slack = teste_login[0]
                nome_solicitante = teste_login[1]
                id_solicitante = teste_login[2]
                print(f"""
///////////////////////////////////////////////////////////////               
Slack '{slack}'
Nome do Solicitante '{nome_solicitante}'
ID do Solicitante '{id_solicitante}'
///////////////////////////////////////////////////////////////
                """)
                self.clear_frame()
                self.main_window()
            else:
                on_user_fail()
            db.commit()

        def check_user_event(event):
            check_user()

        self.titleframe = Frame(
            self, width=310, height=60, bg=white, relief="flat")
        self.titleframe.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)
        self.infoframe = Frame(
            self, width=240, height=300, bg=white, relief="flat")
        self.infoframe.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

        cadastrobutton = Button(self.infoframe, command=self.newuser_window, text="ADD USER",
                                height=1, bg=blue, fg=white, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
        cadastrobutton.pack(anchor=NW)
        titlelabel = Label(self.titleframe, text="LOGIN", height=1,
                           anchor=NE, font=('Ivy 15'), bg=white, fg=grey)
        titlelabel.pack()
        linelabel = Label(self.titleframe, width=300, text="",
                          height=1, anchor=NW, font=('Ivy 1 '), bg=blue)
        linelabel.pack()
        infolabel = Label(self.infoframe, text="Usuário", height=1,
                          anchor=NW, font=('Ivy 10 bold'), bg=white, fg=grey)
        infolabel.pack()
        userentry = Entry(self.infoframe, justify='center', font=(
            "", 15), highlightthickness=1, relief="solid")
        userentry.pack()
        loginbutton = Button(self.infoframe, command=check_user, text="ENTRAR", width=20,
                             height=2, bg=blue, fg=white, font=('Ivy 12 bold'), relief=RAISED, overrelief=RIDGE)
        loginbutton.pack(pady=30)
        credtslabel = Label(self.infoframe, text=".::. By: João Pedro A. Oliveira .::.",
                            anchor=NW, font="ivy 7 bold", bg=white, fg=black)
        credtslabel.pack()
        userentry.insert(0, last_user)
        credtslabel.bind("<Double-Button-1>", lambda e: wbb.open_new(LinkedIn))
        userentry.bind("<Return>", check_user_event)

    def newuser_window(self):
        global newuser_window
        self.withdraw()

        def on_newuser_windowclosing():
            newuser_window.destroy()
            self.deiconify()

        def inset_user():

            def user_asp():
                words = str(userentry.get()).split(" ")
                return words

            if len(user_asp()) != 1:
                on_usernull()

            elif slackentry.get() != "" and solicitanteentry.get() != "" and identry.get() != "" and userentry.get() != "":
                try:
                    cursor.execute(f"""
                    INSERT INTO users VALUES(
                    '{slackentry.get()}',
                    '{solicitanteentry.get()}',
                    '{identry.get()}',
                    '{userentry.get()}'
                    )
                    """)
                    db.commit()
                    newuser_window.destroy()
                    self.deiconify()
                except:
                    on_userfail()
                    pass
            else:
                on_usernull()
            db.commit()

        def insertuser_event(event):
            inset_user()

        def on_userfail():
            self.deiconify()
            newuser_window.withdraw()
            if messagebox.showinfo(f"{program_name} | {main_name}", "Usuário já está cadastrado!"):
                self.withdraw()
                newuser_window.deiconify()
                pass

        def on_usernull():
            self.deiconify()
            newuser_window.withdraw()
            if messagebox.showinfo(f"{program_name} | {main_name}", "Não é possível cadastrar, campos inválidos!"):
                self.withdraw()
                newuser_window.deiconify()
                pass

        newuser_window = Toplevel()
        newuser_window.iconbitmap(icon_folder + "rpa_ico.ico")
        newuser_window.title(f"{program_name} | {main_name} | CADASTRO USER")
        newuser_window.configure(background=white)
        newuser_window.resizable(width=FALSE, height=FALSE)

        titleframe = Frame(newuser_window, bg=white, relief="flat")
        titleframe.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)
        infoframe = Frame(newuser_window, bg=white, relief="flat")
        infoframe.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

        titlelabel = Label(titleframe, text="CADASTRO USUÁRIO",
                           height=1, anchor=NE, font=('Ivy 15'), bg=white, fg=grey)
        titlelabel.pack()
        linelabel = Label(titleframe, width=300, text="",
                          height=1, anchor=NW, font=('Ivy 1 '), bg=blue)
        linelabel.pack()

        slackabel = Label(infoframe, text="Slack", height=1,
                          anchor=NW, font=('Ivy 9 bold'), bg=white, fg=grey)
        slackabel.pack()
        slackentry = Entry(infoframe, justify='center', font=(
            "", 9), highlightthickness=1, relief="solid")
        slackentry.pack()
        solicitantelabel = Label(infoframe, text="Nome do Solicitante",
                                 height=1, anchor=NW, font=('Ivy 9 bold'), bg=white, fg=grey)
        solicitantelabel.pack()
        solicitanteentry = Entry(infoframe, justify='center', font=(
            "", 9), highlightthickness=1, relief="solid")
        solicitanteentry.pack()
        idlabel = Label(infoframe, text="ID do Solicitante", height=1,
                        anchor=NW, font=('Ivy 9 bold'), bg=white, fg=grey)
        idlabel.pack()
        identry = Entry(infoframe, justify='center', font=(
            "", 9), highlightthickness=1, relief="solid")
        identry.pack()
        userlabel = Label(infoframe, text="Usuário", height=1,
                          anchor=NW, font=('Ivy 9 bold'), bg=white, fg=grey)
        userlabel.pack()
        userentry = Entry(infoframe, justify='center', font=(
            "", 9), highlightthickness=1, relief="solid")
        userentry.pack()
        adduserbutton = Button(infoframe, command=inset_user, text="CADASTAR", width=25,
                               height=2, bg=blue, fg=white, font=('Ivy 12 bold'), relief=RAISED, overrelief=RIDGE)
        adduserbutton.pack(pady=30)
        credtslabel = Label(infoframe, text=".::. By: João Pedro A. Oliveira .::.",
                            anchor=NW, font="ivy 7 bold", bg=white, fg=black)
        credtslabel.pack()
        credtslabel.bind("<Double-Button-1>", lambda e: wbb.open_new(LinkedIn))
        newuser_window.protocol("WM_DELETE_WINDOW", on_newuser_windowclosing)
        userentry.bind("<Return>", insertuser_event)

    def main_window(self):
        notas_xml = get_db_data()
        horas = get_timetot()//3600
        minutos = get_timetot() % 3600/60
        est_time = get_timetot()/get_filestot()
        self.titleframe = Frame(
            self, width=500, height=60, bg=white, relief="flat")
        self.titleframe.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)
        self.infoframe = Frame(
            self, width=440, height=500, bg=white, relief="flat")
        self.infoframe.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)
        logoutbutton = Button(self.titleframe, command=self.return_login, text="LOGOUT",
                              height=1, bg=blue, fg=white, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
        logoutbutton.pack(anchor=NW)
        titlelabel = Label(self.titleframe, text=f"{program_name} {main_name}", height=1, anchor=NE, font=(
            'Ivy 15'), bg=white, fg=grey)
        titlelabel.pack()
        linelabel = Label(self.titleframe, width=400, text="",
                          height=1, anchor=NW, font=('Ivy 1 '), bg=blue)
        linelabel.pack()
        readmelabel = Label(self.infoframe, text=f""".::. INSTRUÇÕES .::.\n 
* Deixe sua conta do Atlassian logada no Navegador.
* Coloque os arquivos .XML e .PDF na pasta "arquivos".
* Clique em 'CARREGAR DADOS', para gravar os dados
dos arquivos na pasta "arquivos".
* Cerca de {int(est_time)} segundos para cada nota.
* Após clicar em INICIAR não interfira no teclado ou no mouse.
* Feche o Console para parar.
* Feche aplicativos pesados antes de iniciar.
* Foram automatizadas:\n 
{get_filestot()} NFSe, totalizando {int(horas)} hora(s) e {int(minutos)} minuto(s)!\n
            """, justify=CENTER, anchor=NE, font='Ivy 8 bold', bg=white, fg=black)
        readmelabel.pack()
        getdatabutton = Button(self.infoframe, command=self.on_getdata, text="CARREGAR DADOS", width=25,
                               height=2, bg=blue, fg=white, font=('Ivy 12 bold'), relief=RAISED, overrelief=RIDGE)
        getdatabutton.pack()
        linelabel = Label(self.infoframe, width=400, text="",
                          height=3, anchor=NW, font=('Ivy 1 '), bg=white)
        linelabel.pack()

        if len(notas_xml) != 0:
            startbutton = Button(self.infoframe, command=self.on_firststart, text="INICIAR", width=25,
                                 height=2, bg=blue, fg=white, font=('Ivy 12 bold'), relief=RAISED, overrelief=RIDGE)
            startbutton.pack()
        else:
            pass

        credtslabel = Label(self.infoframe, text=".::. By: João Pedro A. Oliveira .::.",
                            anchor=NW, font="ivy 7 bold", bg=white, fg=black)
        credtslabel.pack()
        credtslabel.bind("<Double-Button-1>", lambda e: wbb.open_new(LinkedIn))

    def data_window(self):

        def on_datawindowclosing():
            data_window.destroy()
            self.deiconify()

        global data_window
        data_window = Toplevel()
        data_window.iconbitmap(icon_folder + "rpa_ico.ico")
        data_window.title(f"{program_name} | {main_name} | DADOS NFSe")
        data_window.configure(background=white)
        data_window.resizable(width=FALSE, height=FALSE)
        data_window.protocol("WM_DELETE_WINDOW", on_datawindowclosing)

        titleframe = Frame(data_window, bg=white, relief="flat")
        titleframe.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)
        infoframe = Frame(data_window, bg=white, relief="flat")
        infoframe.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

        notas_xml = get_db_data()
        columns = ('id', 'uf', 'filial', 'razao_social',
                   'vencimento', 'valor', 'cod_barras')

        tree = Treeview(infoframe, columns=columns, show='headings', height=20)

        tree.column('id', width=25, minwidth=20, stretch=NO)
        tree.column('uf', width=35, minwidth=20, stretch=NO)
        tree.column('filial', width=125, minwidth=80, stretch=NO)
        tree.column('razao_social', width=350, minwidth=250, stretch=NO)
        tree.column('vencimento', width=100, minwidth=70, stretch=NO)
        tree.column('valor', width=100, minwidth=70, stretch=NO)
        tree.column('cod_barras', width=350, minwidth=290, stretch=NO)

        tree.heading('id', text='ID')
        tree.heading('uf', text='UF')
        tree.heading('filial', text='Dark Store')
        tree.heading('razao_social', text='Fornecedor')
        tree.heading('vencimento', text='Vencimento')
        tree.heading('valor', text='Valor')
        tree.heading('cod_barras', text='Codigo de Barras do Boleto')

        id = 1
        valores = []
        for n in notas_xml:
            valores.append(
                (f'{(id)}', f'{n[1]}', f'{n[2]}', f'{n[3]}', f'{n[5]}', f'R$ {n[6]}', f'{n[9]}'))
            id += 1

        for i in valores:
            tree.insert('', END, values=i)

        def item_selected(event):
            for selected_item in tree.selection():
                item = tree.item(selected_item)
                record = item['values']
                if messagebox.askokcancel(title='Information', message=str(record)):
                    pass

        titlelabel = Label(titleframe, text="DADOS COLETADOS",
                           height=1, anchor=NE, font=('Ivy 15'), bg=white, fg=grey)
        titlelabel.pack()
        linelabel = Label(titleframe, width=930, text="",
                          height=1, anchor=NW, font=('Ivy 1 '), bg=blue)
        linelabel.pack()

        # tree.bind('<<TreeviewSelect>>', item_selected)

        tree.grid(row=0, column=0, sticky='nsew')
        scrollbar = Scrollbar(infoframe, orient=VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')
        linelabel = Label(infoframe, text="", height=3,
                          anchor=NW, font=('Ivy 1 '), bg=white)
        linelabel.grid(row=2, column=0, sticky='nsew')
        startbutton = Button(infoframe, command=self.on_start, text="INICIAR", width=25,
                             height=2, bg=blue, fg=white, font=('Ivy 12 bold'), relief=RAISED, overrelief=RIDGE)
        startbutton.grid(row=3, column=0, sticky='nsew')
        credtslabel = Label(infoframe, text=".::. By: João Pedro A. Oliveira .::.",
                            anchor=CENTER, font="ivy 7 bold", bg=white, fg=black)
        credtslabel.grid(row=4, column=0, sticky='nsew')
        credtslabel.bind("<Double-Button-1>", lambda e: wbb.open_new(LinkedIn))
