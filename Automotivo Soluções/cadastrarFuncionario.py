from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import BOLD
from turtle import width
from TabFunc import TabFunc


class ver_cadastrar_func():
   def __init__(self):

      self.janela = Tk()
      self.janela.title('Cadastro de Funcionários')
      self.janela.geometry('1600x900')
      self.janela.minsize(1600, 900)
      self.janela.maxsize(1600, 900)
      self.janela.config(bg="#484848")
      self.janela.state("zoomed")
      self.janela.iconbitmap('automotivo.ico')
      #self.janela.attribute('-fullscreen', True)

# ============= SEÇÕES ================ #

      self.container1 = LabelFrame(self.janela, bg="#484848", fg="#e1e3db")

      self.wrapper1 = LabelFrame(
         self.container1, text='Dados do Funcionário', font=("Roboto", 18, 'bold'), bg="#484848", fg="#e1e3db")
      self.wrapper2 = LabelFrame(
         self.janela, text='Funcionários', font=("Roboto", 18, 'bold'), bg="#484848", fg="#e1e3db")
      self.wrapper3 = LabelFrame(
         self.container1, width=400, font=("Roboto", 18, 'bold'), text='Procurar', bg="#484848", fg="#e1e3db")
      self.rodape = Frame(self.janela, bg="#484848")

      self.container1.pack(fill='both', expand='no', padx=30, pady=10)
      self.wrapper1.pack(fill='both', expand='yes',
                        padx=25, pady=10, ipady=30, side="left")
      self.wrapper2.pack(fill='none', expand='no',
                        padx=10, pady=10)
      self.wrapper3.pack(fill='x', expand='no', ipadx=30,
                        padx=30, ipady=75, side="right")
      self.rodape.pack(fill='both', expand='yes', padx=20)


# ========= SEÇÃO DADOS DO FUNCIONÁRIO ======= #
# ---------- LABELS & ENTRYS ----------- #
      self.labelNome = Label(self.wrapper1, font=(
         "Roboto", 16), text='Nome', bg="#484848", fg="#e1e3db")
      self.labelNome.grid(row=0, column=0, padx=5, pady=5)
      self.caixaNome = Entry(self.wrapper1, width=40)
      self.caixaNome.grid(row=0, column=1, padx=5, pady=5)

      self.lbl3 = Label(self.wrapper1, font=("Roboto", 16),
                        text='CPF', bg="#484848", fg="#e1e3db")
      self.lbl3.grid(row=1, column=0, padx=5, pady=3)
      self.caixaCPF = Entry(self.wrapper1, width=40)
      self.caixaCPF.grid(row=1, column=1, padx=5, pady=5)

      self.lbl4 = Label(self.wrapper1, font=("Roboto", 16),
                        text='Cargo', bg="#484848", fg="white")
      self.lbl4.grid(row=2, column=0, padx=5, pady=3)
      self.caixaCargo = Entry(self.wrapper1, width=40)
      self.caixaCargo.grid(row=2, column=1, padx=5, pady=5)

      self.lbl5 = Label(self.wrapper1, font=("Roboto", 16),
                        text='Login', bg="#484848", fg="#e1e3db")
      self.lbl5.grid(row=0, column=2, padx=50, pady=5)
      self.caixaLogin = Entry(self.wrapper1)
      self.caixaLogin.grid(row=0, column=3, padx=5, pady=5)

      self.lbl6 = Label(self.wrapper1, font=("Roboto", 16),
                        text='Senha', bg="#484848", fg="#e1e3db")
      self.lbl6.grid(row=1, column=2, padx=5, pady=5)
      self.caixaSenha = Entry(self.wrapper1)
      self.caixaSenha.grid(row=1, column=3, padx=5, pady=5)

      self.lbl7 = Label(self.wrapper1, font=("Roboto", 16),
                        text='ID Funcionário', bg="#484848", fg="#e1e3db")
      self.lbl7.grid(row=2, column=2, padx=5, pady=5)
      self.caixaId = Entry(self.wrapper1)
      self.caixaId.grid(row=2, column=3, padx=10, pady=5, sticky='W')

# ------------ BOTÕES -------------- #
      self.addBtn = Button(self.wrapper1, text='Adicionar', font=("Roboto", 16),
                           command=self.inserir_func, bg="#566981", fg="#e1e3db", relief=RAISED)
      self.addBtn.bind("<Enter>", self.hoverIn1)
      self.addBtn.bind("<Leave>", self.hoverOut)
      self.alterarBtn = Button(
         self.wrapper1, text='Alterar', font=("Roboto", 16), command=self.alterar_func, bg="#566981", fg="#e1e3db", relief=RAISED)
      self.alterarBtn .bind("<Enter>", self.hoverIn4)
      self.alterarBtn .bind("<Leave>", self.hoverOut)
      self.excluirBtn = Button(
         self.wrapper1, text='Excluir', font=("Roboto", 16), command=self.excluir_func, bg="#566981", fg="#e1e3db", relief=RAISED)
      self.excluirBtn.bind("<Enter>", self.hoverIn3)
      self.excluirBtn.bind("<Leave>", self.hoverOut)
      self.addBtn.grid(row=4, column=1, padx=5, pady=10, ipadx=25)
      self.alterarBtn.grid(row=4, column=2, padx=5, pady=3, ipadx=20)
      self.excluirBtn.grid(row=4, column=3, padx=5, pady=3, ipadx=25)


# ========== SEÇÃO FUNCIONÁRIOS CADASTRADOS ============ #
# ------------------- TREEVIEW ------------------ #
      self.style = ttk.Style(master=self.janela)
      self.style.theme_use("clam")
      self.style.configure("mystyle.Treeview", font=("Roboto", 14))
      self.style.configure("mystyle.Treeview.Heading", font=("Roboto", 16))
      self.style.configure("Treeview", background="silver", rowheight=20, fieldbackground="#E0FFFF",)
      self.style.configure("Heading", background="#4682B4", foreground = "white")

      self.cabecalho = ('#', 'nome', 'cpf', 'cargo',
                        'login', 'senha')
      self.trv = ttk.Treeview(
         self.wrapper2, style="mystyle.Treeview", selectmode='browse', columns=self.cabecalho, show='headings')

      self.trv.column('#', width=30)
      self.trv.column('nome', anchor='center', width=350)
      self.trv.column('cpf', anchor='center', width=180)
      self.trv.column('cargo', anchor='center', width=180)
      self.trv.column('login', anchor='center', width=150)
      self.trv.column('senha', anchor='center', width=150)

      self.trv.heading('#', text='#')
      self.trv.heading('nome', text='NOME')
      self.trv.heading('cpf', text='CPF')
      self.trv.heading('cargo', text='CARGO')
      self.trv.heading('login', text='LOGIN')
      self.trv.heading('senha', text='SENHA')

      self.trv.bind('<Double 1>', self.pegar_linha)
      self.trv.pack()

      self.popular()


# ============= SEÇÃO PROCURAR =========== #
# ---------- LABELS & ENTRYS ----------- #
      self.lbl1 = Label(self.wrapper3, font=(
         "Roboto", 14), text='Palavra-Chave', bg="#566981", fg="#e1e3db", relief=RAISED)
      self.lbl1.pack(side='left', padx=10, pady=10, ipadx=10)

      self.busca = Entry(self.wrapper3)
      self.busca.pack(side='left', padx=6, pady=10, ipadx=10, ipady=2)


# ------------- BOTÕES ------------- #
      self.procurarBtn = Button(
         self.wrapper3, text='Procurar', font=("Roboto", 14), command=self.procurar, bg="#566981", fg="#e1e3db", relief=RAISED)
      self.procurarBtn.pack(side='left', padx=20, pady=10, ipadx=10)
      self.procurarBtn.bind("<Enter>", self.hoverIn2)
      self.procurarBtn.bind("<Leave>", self.hoverOut)

      self.limparBtn = Button(
         self.wrapper3, text='Limpar', font=("Roboto", 14), command=self.limpar, bg="#566981", fg="#e1e3db", relief=RAISED)
      self.limparBtn.pack(side='left', padx=6, pady=10, ipadx=10)
      self.limparBtn .bind("<Enter>", self.hoverIn4)
      self.limparBtn .bind("<Leave>", self.hoverOut)

      self.mostrarBtn = Button(
         self.wrapper2, padx=30, text='Mostrar Todos', font=("Roboto", 16), command=self.popular, bg="#566981", fg="#e1e3db", relief=RAISED)
      self.mostrarBtn.pack(side='right', padx=600, pady=10)
      self.mostrarBtn.bind("<Enter>", self.hoverIn2)
      self.mostrarBtn.bind("<Leave>", self.hoverOut)


# ========= SEÇÃO RODAPÉ ======= #
# ---------- BOTÃO ----------- #
      self.voltarBtn = Button(
         self.rodape, text='Voltar', font=("Roboto", 12), width='15', command=self.voltar_tela, bg="#800000", fg="#e1e3db", relief=RAISED)
      self.voltarBtn.pack(side='right', padx=2, ipadx=2)

      mainloop()

# ============= FUNÇÕES ============== #
   def pegar_linha(self, identificador):
      staff = TabFunc()
      self.normal()
      self.limpar_caixas()
      for item in self.trv.selection():
         self.id = self.trv.item(item, 'values')
      identificador = self.id[0]

      staff.identificar_linha(identificador)
      self.caixaId.insert(INSERT, staff.idfunc)
      self.caixaNome.insert(INSERT, staff.nome)
      self.caixaCPF.insert(INSERT, staff.cpf)
      self.caixaCargo.insert(INSERT, staff.cargo)
      self.caixaLogin.insert(INSERT, staff.login)
      self.caixaSenha.insert(INSERT, staff.senha)
      self.leitura_apenas()

   def limpar_caixas(self):
      self.normal()
      self.caixaNome.delete(0, END)
      self.caixaCPF.delete(0, END)
      self.caixaCargo.delete(0, END)
      self.caixaLogin.delete(0, END)
      self.caixaSenha.delete(0, END)
      self.caixaId.delete(0, END)

   def procurar(self):
      self.trv.delete(*self.trv.get_children())
      staff = TabFunc()
      nome = self.busca.get()
      for i in staff.filtrar_func(nome):
         self.trv.insert('', 'end', values=i)

   def limpar(self):
      self.normal()
      self.busca.delete(0, END)
      self.caixaNome.delete(0, END)
      self.caixaCPF.delete(0, END)
      self.caixaCargo.delete(0, END)
      self.caixaLogin.delete(0, END)
      self.caixaSenha.delete(0, END)
      self.caixaId.delete(0, END)

   def inserir_func(self):
      staff = TabFunc()
      staff.nome = self.caixaNome.get()
      staff.cpf = self.caixaCPF.get()
      staff.cargo = self.caixaCargo.get()
      staff.login = self.caixaLogin.get()
      staff.senha = self.caixaSenha.get()
      staff.add_func()
      self.popular()
      self.limpar_caixas()

   def alterar_func(self):
      staff = TabFunc()
      staff.nome = self.caixaNome.get()
      staff.cpf = self.caixaCPF.get()
      staff.cargo = self.caixaCargo.get()
      staff.login = self.caixaLogin.get()
      staff.senha = self.caixaSenha.get()
      staff.idfunc = self.caixaId.get()
      staff.atualizar_func()
      self.popular()
      self.limpar_caixas()

   def excluir_func(self):
      staff = TabFunc()
      staff.idfunc = self.caixaId.get()
      staff.deletar_func()
      self.popular()
      self.limpar_caixas()

   def voltar_tela(self):
      self.janela.destroy()
      return 

   def popular(self):
      self.trv.delete(*self.trv.get_children())
      staff = TabFunc()
      for i in staff.populate():
         self.trv.insert('', 'end', values=i)

   def leitura_apenas(self):
      self.caixaId.configure(state='disabled')

   def normal(self):
      self.caixaId.configure(state='normal')

   def hoverIn1(self, event):  # verde
      event.widget.config(bg="#32CD32", fg="white", relief=GROOVE)

   def hoverIn2(self, event):  # azul
      event.widget.config(bg="#6495ED", fg="white", relief=GROOVE)

   def hoverIn3(self, event):  # vermelho
      event.widget.config(bg="#FF0000", fg="white", relief=GROOVE)

   def hoverIn4(self, event):  # amarelo
      event.widget.config(bg="#FFD700", fg="white", relief=GROOVE)

   def hoverOut(self, event):
      event.widget.config(bg="#566981", fg="#e1e3db", relief=RAISED)
   # def startJan(self):    
   #    minhaTela = ver_cadastrar_func()
   #    return minhaTela.janela.mainloop()

minhaTela = ver_cadastrar_func()
