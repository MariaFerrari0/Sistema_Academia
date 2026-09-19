import os

from gym.estruturas.arvore_binaria import ArvoreBinaria


CAMINHO_ARQUIVO = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
    "dados",
    "alunos.dat"
)


class ArquivoAlunos:

    def __init__(self):
        self.arvore = ArvoreBinaria()
        self._criar_arquivo()
        self._carregar_indice()

    def _criar_arquivo(self):
        os.makedirs(
            os.path.dirname(CAMINHO_ARQUIVO),
            exist_ok=True
        )

        if not os.path.exists(CAMINHO_ARQUIVO):
            open(
                CAMINHO_ARQUIVO,
                "w",
                encoding="utf-8"
            ).close()

    def _carregar_indice(self):
        with open(
            CAMINHO_ARQUIVO,
            "r",
            encoding="utf-8"
        ) as arquivo:

            posicao = 0

            for linha in arquivo:
                if linha.strip():
                    dados = linha.strip().split("|")
                    codigo = int(dados[0])

                    self.arvore.inserir(
                        codigo,
                        posicao
                    )

                posicao += len(
                    linha.encode("utf-8")
                )

    def inserir(self, aluno):
        codigo = int(aluno["codigo"])

        if self.arvore.buscar(codigo) is not None:
            return False

        with open(
            CAMINHO_ARQUIVO,
            "a",
            encoding="utf-8"
        ) as arquivo:

            posicao = arquivo.tell()

            linha = (
                f"{codigo}|"
                f"{aluno['nome']}|"
                f"{aluno['data_nascimento']}|"
                f"{aluno['peso']}|"
                f"{aluno['altura']}\n"
            )

            arquivo.write(linha)

        self.arvore.inserir(
            codigo,
            posicao
        )

        return True

    def listar(self):
        alunos = []

        with open(
            CAMINHO_ARQUIVO,
            "r",
            encoding="utf-8"
        ) as arquivo:

            for linha in arquivo:
                if linha.strip():
                    dados = linha.strip().split("|")

                    alunos.append({
                        "codigo": int(dados[0]),
                        "nome": dados[1],
                        "data_nascimento": dados[2],
                        "peso": float(dados[3]),
                        "altura": float(dados[4])
                    })

        return alunos

    def buscar(self, codigo):
        posicao = self.arvore.buscar(
            int(codigo)
        )

        if posicao is None:
            return None

        with open(
            CAMINHO_ARQUIVO,
            "r",
            encoding="utf-8"
        ) as arquivo:

            arquivo.seek(posicao)
            linha = arquivo.readline()

        dados = linha.strip().split("|")

        return {
            "codigo": int(dados[0]),
            "nome": dados[1],
            "data_nascimento": dados[2],
            "peso": float(dados[3]),
            "altura": float(dados[4])
        }