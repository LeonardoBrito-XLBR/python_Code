import os
from dataclasses import dataclass

os.system("cls || clear")


def Salvar (livros):

    arquivo = "Catalogo_Livro2.txt"

    #Realizando Comandos de escrita em um arquivo externo
    with open(arquivo,"w") as arquivoDeLivros:
        for livro in livros:
            arquivoDeLivros.write(f"{livro.nome}\n{livro.autor}\n{livro.categoria}\n{livro.preco}")

    print("Dados dos Livros salvos com sucesso!")

#LENDO O QUE ESTA NO 
def lerLivros():
    with open("Catalogo_Livro2.txt", "r")as arquivo:
        livrosCadastrados = arquivo.read()
    print(livrosCadastrados)

#CRIANDO A CLASS + ATIVIDADE 
@dataclass
class Livro:
    nome: str
    autor: str
    categoria: str
    preco: float #talvez int
livros = []

#GUARDANDO A CLASS NUMA VARIAVEL + ADD VALORES
livro = Livro (
    nome = input ("Qual o nome do livro: "),
    autor = input("Qual o nome do Autor do livro: "),
    categoria = input ("Qual a categoria vai receber: "),
    preco = float (input("Quanto ele vai valer: "))



)

#Guardando os dados em uma lista
livros.append(livro)

#chamando as funções
Salvar(livros)
lerLivros()