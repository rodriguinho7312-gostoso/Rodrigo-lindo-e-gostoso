#Baixar o selenium e  a voz do robo fdp kskskksks
from email.mime.text import MIMEText as mt
import smtplib as smt
import pyttsx3 as voz
import tkinter as tk
#interface gráfica pika

janela = tk.Tk()
janela.title("Informações do usuario")
texto = tk.Label(janela, text="Preencha os campos abaixo")
texto.pack(pady=10,padx= 10)

tk.Label(janela, text="Digite seu email:").pack()
entrada_email = tk.Entry(janela, width=30)
entrada_email.pack()
tk.Label(janela, text="Digite sua senha:").pack()
entrada_senha = tk.Entry(janela, width=30)
entrada_senha.pack()

tk.Label(janela, text="Digite o email do cabaço(a):").pack()
entrada_email_cabaco = tk.Entry(janela, width=30)
entrada_email_cabaco.pack()

tk.Label(janela, text="Digite a mensagem que quer enviar:").pack()
entrada_mensagem = tk.Entry(janela, width=30)
entrada_mensagem.pack()
def pegar_dados():
    global emaillogin, senhalogin, email_recebedor, sua_mensagem
    emaillogin = entrada_email.get()
    senhalogin = entrada_senha.get()
    email_recebedor = entrada_email_cabaco.get()
    sua_mensagem = entrada_mensagem.get()
    janela.destroy()


botao = tk.Button(janela, text="Enviar", command=pegar_dados)
botao.pack(pady=20)

janela.mainloop()

#não dá para logar no google com o selenium então vou mudar um pouco a dinamica 8==D





#envio de email pika

mensagem = mt('{}'.format(sua_mensagem))
mensagem['From'] = emaillogin
mensagem['To'] = email_recebedor


servidor = smt.SMTP("smtp.gmail.com", 587)
servidor.starttls()
servidor.login(emaillogin, senhalogin)
servidor.sendmail(mensagem["From"], mensagem["To"], mensagem.as_string())
servidor.quit()



#voz do robo muito pika kskskskksskksksk
voz_robo = voz.init()
voz_robo.say("{}".format(sua_mensagem))
voz_robo.say("Mensagem enviada com sucesso para {}".format(email_recebedor))
voz_robo.say('tchau e um beijo no bumbum')
voz_robo.say('Quem executar esse código é muito é gay skskkskskskksksks')
voz_robo.volume = 100
voz_robo.runAndWait()