import tkinter as tk
def averiguar():
    arquivo_a_abrir = open(arquivo.get(), "r")
    texto = str(arquivo_a_abrir.read())
    if "resenha" in texto:
        resultado.config(text="RESENHA DETECTADA!!!")
        vezes.config(text=str(texto.count("resenha")) + " vezes")
        porcentagem.config(text=str(texto.count("resenha") * 7 / len(texto) * 100) + "% resenha")
    else:
        resultado.config(text="sem resenha aqui.")
        vezes.config(text="")
        porcentagem.config(text="")
    arquivo_a_abrir.close()
root = tk.Tk()
root.title("MAQUINA DE AVERIGUAR RESENHA MODELO 67000")
root.geometry("600x150")
tk.Label(root, text="QUER AVERIGUAR UMA RESENHA? USE A MAQUINA DE AVERIGUAR RESENHA!").grid(row=0, column=0)
tk.Label(root, text="Coloque o arquivo a ser averiguado aqui.").grid(row=1, column=0, sticky=tk.W)
arquivo = tk.Entry(root)
arquivo.grid(row=2, column=0, sticky=tk.W)
tk.Button(root, text="AVERIGUAR", command=averiguar).grid(row=3, column=0, sticky=tk.W)
#resultado
resultado = tk.Label(root)
resultado.grid(row=4, column=0, sticky=tk.W)
#vezes
vezes = tk.Label(root)
vezes.grid(row=5, column=0, sticky=tk.W)
#porcentagem
porcentagem = tk.Label(root)
porcentagem.grid(row=6, column=0, sticky=tk.W)
root.mainloop()
