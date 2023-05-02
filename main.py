from os import system
from datetime import datetime

# MOSTRAR SEPARADOR
def separador() -> None:
    print('-' * 50)

# LIMPAR TELA
def limpar() -> None:
    system('clear')

# MOSTRAR TÍTULO
def titulo(texto) -> None:
    separador()
    print(f'{texto: ^50}')
    separador()

# LEITOR DE OPÇÕES
def mostrar_opcoes(texto: str, opcoes: list) -> bool:
    limpar()
    titulo(texto)
    for num, opcao in enumerate(opcoes):
        print(f'[ {num} ] {opcao.indentificador}')
    separador()
    escolha = ler_opcao('ESCOLHA: ', len(opcoes))
    separador()
    return opcoes[escolha].funcao()

# LER UM INTEIRO PARA REPRESENTAR A ESCOLHA
def ler_opcao(texto, quant) -> int:
    resposta = None
    while resposta is None or resposta not in range(quant):
        try:
            resposta = int(input(texto))
        except ValueError:
            print('Opção inválida! Informe um valor inteiro!')
        else:
            if resposta not in range(quant):
                print(f'Opção inválida! Informe um valor entre 0 e {quant - 1}')        
    return resposta


# FUNÇÃO DO LOOP PRINCIPAL
def iniciar() -> bool:
    return mostrar_opcoes('GERENCIADOR DE NOTAS:', menu_principal)

def atualizar() -> list:
    # OPÇÕES DO MENU DE DISCIPLINAS
    lista = disciplinas.copy()
    lista.extend(opcoes)
    return lista

def adicionar_disciplina() -> bool:
    disciplinas.append(Disciplina(input('Nome da disciplina: ')))
    return True

# FUNÇÕES DE SAÍDA DA INTERFACE
def sair() -> bool:
    hora = datetime.now().hour
    if hora < 6:
        despedida = 'uma boa madrugada'
    elif hora < 12:
        despedida = 'um bom dia'
    elif hora < 18:
        despedida = 'uma boa tarde'
    else:
        despedida = 'uma boa noite'
    print(f'Tenha {despedida}. Até mais!')
    return False

# CLASSES 
class Opcao:
    def __init__(self, indentificador: str, funcao) -> None:
        self.indentificador = indentificador
        self.funcao = funcao


class Disciplina(Opcao):
    def __init__(self, indentificador: str) -> None:
        super().__init__(indentificador, self.menu)
        self.dados = {
            'Professor(a)': '-',
            'Sala': '-',
        }
        self.notas = [
            [70, 100],
            [60, 90],
            
        ]
    
    def info(self) -> None:
        limpar()
        titulo(self.indentificador)
        for key, value in self.dados.items():
            print(f'{key}: {value}')
        separador()
        print('NOTAS: ')
        for nota in self.notas:
            print(nota)


    def menu(self) -> bool:
        self.info()
        input()
        return True
        
disciplinas = [
    Disciplina('Fundamentos de Eletricidade'),
    Disciplina('Inglês Instrumental'),
    Disciplina('Introdução à Telemática'),
    Disciplina('Laboratório de Sistemas Aberto'),
    Disciplina('Português Instrumental'),
    Disciplina('Programação 1'),
    Disciplina('Pré-Cálculo'),
]

opcoes = [
    Opcao('Adicionar Disciplina', adicionar_disciplina),
    Opcao('Sair', sair)
]

rodando = True
while rodando:
    menu_principal = atualizar()
    rodando = iniciar()