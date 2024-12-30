import sys
import random
import string
from PySide6.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton, QVBoxLayout

class Form(QDialog):

    def __init__(self):
        super(Form, self).__init__()
        self.setWindowTitle("Gerador de Senhas")

        # Lista vazia para salvar senhas geradas
        self.list_pwds_save = []

        # Criação dos componentes da interface
        self.edit = QLineEdit("Gere uma senha")
        self.button = QPushButton("Gerar")

        # Criando layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.edit)
        layout.addWidget(self.button)

        # Evento de clique no botão
        self.button.clicked.connect(self.showpwd)

    def gerando_senha(self):
        # Ajustar o comprimento para garantir que a quantidade de letras, números e símbolos seja a mesma
        letras_minuscola = (string.ascii_lowercase * (45 // len(string.ascii_lowercase) + 1))[:100]
        letras_maiusculas = (string.ascii_uppercase * (45 // len(string.ascii_uppercase) + 1))[:100]
        simbolos = (string.punctuation * (45 // len(string.punctuation) + 1))[:100]

        # Gerar 45 números aleatórios entre 100 e 3500
        numeros_aleatorios = [random.randint(100, 3500) for _ in range(100)]

        # Gerar senhas com números, letras e símbolos alternados
        gerandor_1 = [f'{num}{letra}' for num, letra in zip(numeros_aleatorios, letras_minuscola)]
        gerador_2 = [f'{num}{letra}' for num, letra in zip(numeros_aleatorios, letras_maiusculas)]
        gerador_3 = [f'{simbolo}{num}' for simbolo, num in zip(simbolos, numeros_aleatorios)]

        lista_combinada = set()
        for i in range(len(gerandor_1)):
            lista_combinada.add(gerandor_1[i])
            lista_combinada.add(gerador_2[i])
            lista_combinada.add(gerador_3[i])

        # Criar a senha unificada
        senha_completa = "".join(list(lista_combinada))

        # Pegar uma fatia da senha gerada, evitando que comece com números ou letras isolados
        senha = senha_completa[1:16]

        # Salvar a senha gerada
        self.list_pwds_save.append({'senha': senha})

        return senha

    def showpwd(self):
        # Gerar a senha e exibi-la no campo de texto
        senha_gerada = self.gerando_senha()
        self.edit.setText(senha_gerada)

if __name__ == "__main__":
    # run 
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec())
