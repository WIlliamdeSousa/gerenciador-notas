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
        print(f'[ {num} ] {opcao.nome}')
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
    lista.extend(opcoes_main)
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

def importar_disciplinas() -> list:
    disciplinas = []
    with open('disciplinas.csv', 'r', encoding='utf-8') as arquivo:
        arquivo = arquivo.readlines()
        
        for linha in arquivo:
            info = linha.replace('\n','').split(',')

            nome = info[0]
            prof = info[1]
            notas = Notas(info[2])

            disciplinas.append(Disciplina(nome, prof, notas))
    return disciplinas

# CLASSES 
class Notas: # formato da entrada = 58:60 30:40;66:100
    def __init__(self, notas: str) -> None:
        self.notas = [] # formato = [[[58, 60], [30, 40]], [[66, 100]]]
        for etapa in notas.split(';'):
            lista = []
            for par_nota in etapa.split():
                lista.append([int(i) for i in par_nota.split(':')])
            self.notas.append(lista)
        
    def mostrar(self) -> None:
        for num, nota in enumerate(self.notas): # [[58, 60], [30, 40]]
            print(f'NOTA {num + 1}:')
            for par in nota: # [58, 60]
                print(f'  {par[0]}/{par[1]} ({par[0] / par[1]:.2f} %)')        
                

class Opcao:
    def __init__(self, nome: str, funcao) -> None:
        self.nome = nome
        self.funcao = funcao


class Disciplina(Opcao):
    def __init__(self, nome: str, professor: str, notas: Notas) -> None:
        super().__init__(nome, self.menu)
        self.dados = {
            'Professor(a)': professor,
        }
        self.notas = notas
    
    def info(self) -> None:
        limpar()
        titulo(self.nome)
        for key, value in self.dados.items():
            print(f'{key}: {value}')
        separador()

    def menu(self) -> bool:
        self.info()
        input()
        return True


disciplinas = importar_disciplinas()

opcoes_main = [
    Opcao('Adicionar Disciplina', adicionar_disciplina),
    Opcao('Sair', sair)
]

opcoes_disc = [
    Opcao('Editar informações', editar_infos),
    Opcao('Adicionar nota', adicionar_nota),
    Opcao('Modificar nota', modificar_nota),
    Opcao('Apagar Disciplina', apagar_disciplina),
    Opcao('Voltar Menu', voltar)
]

rodando = True
while rodando:
    menu_principal = atualizar()
    rodando = iniciar()