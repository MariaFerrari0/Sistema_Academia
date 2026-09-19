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
        self.arvore = ArvoreBinaria()

        with open(
            CAMINHO_ARQUIVO,
            "r",
            encoding="utf-8"
        ) as arquivo:

            posicao = 0

            for linha in arquivo:

                if linha.strip():

                    dados = linha.strip().split("|")

                    if len(dados) >= 5:

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
                f"{float(aluno['peso']):.2f}|"
                f"{float(aluno['altura']):.2f}\n"
            )

            arquivo.write(linha)

        self.arvore.inserir(
            codigo,
            posicao
        )

        return True

    def calcular_imc(self, peso, altura):
        if altura <= 0:
            return 0

        return peso / (altura ** 2)

    def diagnostico_imc(self, imc):
        if imc < 18.5:
            return "Abaixo do peso"

        elif imc < 25:
            return "Peso normal"

        elif imc < 30:
            return "Acima do peso"

        else:
            return "Obesidade"

    def listar(self):
        alunos = []

        with open(
            CAMINHO_ARQUIVO,
            "r",
            encoding="utf-8"
        ) as arquivo:

            for linha in arquivo:

                if not linha.strip():
                    continue

                dados = linha.strip().split("|")

                if len(dados) < 5:
                    continue

                peso = float(dados[3])
                altura = float(dados[4])

                imc = self.calcular_imc(
                    peso,
                    altura
                )

                alunos.append({
                    "codigo": int(dados[0]),
                    "nome": dados[1],
                    "data_nascimento": dados[2],
                    "peso": peso,
                    "altura": altura,
                    "imc": round(imc, 2),
                    "diagnostico": self.diagnostico_imc(imc)
                })

        return alunos

    def buscar(self, codigo):
        codigo = int(codigo)

        with open(
            CAMINHO_ARQUIVO,
            "r",
            encoding="utf-8"
        ) as arquivo:

            for linha in arquivo:

                if not linha.strip():
                    continue

                dados = linha.strip().split("|")

                if len(dados) < 5:
                    continue

                if int(dados[0]) == codigo:

                    peso = float(dados[3])
                    altura = float(dados[4])

                    imc = self.calcular_imc(
                        peso,
                        altura
                    )

                    return {
                        "codigo": int(dados[0]),
                        "nome": dados[1],
                        "data_nascimento": dados[2],
                        "peso": peso,
                        "altura": altura,
                        "imc": round(imc, 2),
                        "diagnostico": self.diagnostico_imc(imc)
                    }

        return None

    def atualizar(self, aluno):
        codigo = int(aluno["codigo"])

        if self.arvore.buscar(codigo) is None:
            return False

        with open(
            CAMINHO_ARQUIVO,
            "r",
            encoding="utf-8"
        ) as arquivo:

            registros = arquivo.readlines()

        novos_registros = []

        for linha in registros:

            if not linha.strip():
                continue

            dados = linha.strip().split("|")

            if len(dados) < 5:
                continue

            if int(dados[0]) == codigo:

                linha = (
                    f"{codigo}|"
                    f"{aluno['nome']}|"
                    f"{aluno['data_nascimento']}|"
                    f"{float(aluno['peso']):.2f}|"
                    f"{float(aluno['altura']):.2f}\n"
                )

            novos_registros.append(linha)

        with open(
            CAMINHO_ARQUIVO,
            "w",
            encoding="utf-8"
        ) as arquivo:

            arquivo.writelines(novos_registros)

        self._carregar_indice()

        return True

    def excluir(self, codigo):
        codigo = int(codigo)

        if self.arvore.buscar(codigo) is None:
            return False

        with open(
            CAMINHO_ARQUIVO,
            "r",
            encoding="utf-8"
        ) as arquivo:

            registros = arquivo.readlines()

        novos_registros = []

        for linha in registros:

            if not linha.strip():
                continue

            dados = linha.strip().split("|")

            if len(dados) < 5:
                continue

            if int(dados[0]) != codigo:
                novos_registros.append(linha)

        with open(
            CAMINHO_ARQUIVO,
            "w",
            encoding="utf-8"
        ) as arquivo:

            arquivo.writelines(novos_registros)

        self._carregar_indice()

        return True