from os import system
from datetime import datetime


# CLASSES 
class Notas:
    """
    Objeto com o formato das notas, recebe no "formato 58:60 30:40;66:100" e converte para uma lista que pode ser apresentada com o método mostrar().
    """

    def __init__(self, notas: str = None) -> None:
        self.notas = []  # formato = [[[58, 60], [30, 40]], [[66, 100]]]
        if notas is not None:
            for etapa in notas.split(';'):
                lista = []
                for par_nota in etapa.split():
                    lista.append([int(i) for i in par_nota.split(':')])
                self.notas.append(lista)

    def mostrar(self) -> None:
        if not self.notas:
            print('Sem notas')
        else:
            for num, nota in enumerate(self.notas):  # [[58, 60], [30, 40]]
                print(f'NOTA {num + 1}:')
                for par in nota:  # [58, 60]
                    print(f'  {par[0]}/{par[1]} ({par[0] / par[1] * 100:.0f}%)')
                print(f'  MÉDIA: {self.media_ponderada(nota):.0f}')

    def media_ponderada(self, pares) -> float:
        if not self.notas:
            return 0
        nota_pesos = []
        pesos = []
        for par in pares:
            nota_pesos.append(par[0])
            pesos.append(par[1])
        return sum(nota_pesos) / sum(pesos) * 100


class Opcao:
    """Objeto para armazenar as informações das Opções do sistema."""

    def __init__(self, nome: str, funcao) -> None:
        """Inicia o objeto Opcao, leva como parâmetros o texto que estará visível e a função que ela executará"""
        self.nome = nome
        self.funcao = funcao


class Disciplina(Opcao):
    """Objeto para armazernar as informações das Opções de Disciplinas. Herda de Opcao."""

    def __init__(self, nome: str, professor: str, notas: Notas) -> None:
        """Inicia o Objeto Disciplina com informações da disciplina."""
        super().__init__(nome, self.menu)
        self.dados = {
            'Professor(a)': professor,
        }
        self.notas = notas
        self.opcoes_disc = [
            Opcao('Editar informações', self.editar_infos),
            Opcao('Adicionar nota', self.adicionar_nota),
            Opcao('Modificar nota', self.modificar_nota),
            Opcao('Apagar Disciplina', self.apagar_disciplina),
            Opcao('Voltar Menu', voltar)
        ]

    def menu(self) -> None:
        limpar()
        titulo(self.nome)
        for key, value in self.dados.items():
            print(f'{key}: {value}')
        separador()
        self.notas.mostrar()
        opcoes(None,'O QUE DESEJA FAZER? ', limpar_tela=False)

    def apagar_disciplina(self) -> None:
        msg = f'Tem certeza que deseja APAGAR\n"{self.nome}"? (S/N) '
        while (resposta := str(str(input(msg)).upper().strip())) not in 'SN' or resposta == '':
            print(f'Resposta inválida, digite "S" ou "N".')
        if resposta == 'S':
            disciplinas.remove(self)
            del self
            iniciar()
        elif resposta == 'N':
            self.menu()

    def modificar_nota(self) -> None:
        pass

    def adicionar_nota(self) -> None:
        pass

    def editar_infos(self) -> None:
        pass


# FUNÇÕES
def separador() -> None:
    """Cria um separador com 50 traços."""
    print('-' * 50)


def limpar() -> None:
    """Limpa a tela do terminal."""
    system('clear')


def titulo(titulo: str) -> None:
    """Mostra o parâmetro titulo centralizado e entre separadores de 50 traços."""
    separador()
    print(f'{titulo: ^50}')
    separador()


def opcoes(
        texto: str,
        list_opcoes: list,
        mensagem_final: str,
        limpar_tela: bool = True
) -> None:
    """Exibe as opções disponíveis, ler a escolha do usuário e já executa a escolha."""
    mostrar_opcoes(texto, list_opcoes, limpar_tela)
    ler_opcao(mensagem_final, list_opcoes)


def mostrar_opcoes(
        texto: str,
        list_opcoes: list,
        limpar_tela: bool = True
) -> None:
    """Mostra na tela o título e as opções disponíveis enumeradas."""
    if limpar_tela:
        limpar()
    if texto is not None:
        titulo(texto)
    else:
        separador()
    for num, opcao in enumerate(list_opcoes):
        print(f'[ {num} ] {opcao.nome}')
    separador()


def ler_opcao(texto, list_opcoes) -> None:
    """Ler e executa a opção escolhida pelo usuário."""
    quant = len(list_opcoes)
    escolha = None
    while escolha is None or escolha not in range(quant):
        try:
            escolha = int(input(texto))
        except ValueError:
            print('Opção inválida! Informe um valor inteiro!')
        else:
            if escolha not in range(quant):
                print(f'Opção inválida! Informe um valor entre 0 e {quant - 1}')
    separador()
    list_opcoes[escolha].funcao()


def ordenar_disciplinas(list_disciplinas: list) -> list:
    ordenado = {}
    for disciplina in list_disciplinas:
        ordenado[disciplina.nome] = disciplina
    chaves_ordenadas = sorted(list(ordenado.keys()))
    list_disciplinas = [ordenado[i] for i in chaves_ordenadas]
    return list_disciplinas


def iniciar() -> None:
    """Função para iniciar o sistema"""
    opcoes('GERENCIADOR DE NOTAS:', ordenar_disciplinas(disciplinas).__add__(opcoes_main), 'ESCOLHA: ')


def adicionar_disciplina() -> None:
    """Função para adicionar uma nova disciplina, retorna True caso não tenha erros"""
    try:
        nome = input('Nome da disciplina: ')
        prof = input('Professor(a): ')
        disciplinas.append(Disciplina(nome, prof, Notas()))
    except:
        print('Ocorreu um erro ao tentar adicionar a disciplina.')
    else:
        print('disciplina adicionada com sucesso!')
    finally:
        input('Pressione ENTER para continuar...')
        iniciar()


def sair() -> None:
    """Mostra uma mensagem de saída e fecha a aplicação"""
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


def importar_disciplinas() -> list:
    disciplinas = []
    with open('disciplinas.csv', 'r', encoding='utf-8') as arquivo:
        arquivo = arquivo.readlines()

        for linha in arquivo:
            info = linha.replace('\n', '').split(',')

            nome = info[0]
            prof = info[1]
            try:
                notas = Notas(info[2])
            except:
                notas = Notas(None)

            disciplinas.append(Disciplina(nome, prof, notas))
    return ordenar_disciplinas(disciplinas)


def voltar() -> None:
    iniciar()


# OPÇÕES E MENUS
disciplinas = importar_disciplinas()

opcoes_main = [
    Opcao('Adicionar Disciplina', adicionar_disciplina),
    Opcao('Sair', sair)
]
