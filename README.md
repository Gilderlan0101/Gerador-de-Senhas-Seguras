# Gerador de Senhas Seguras

## Descrição
O **Gerador de Senhas Seguras** é um projeto desenvolvido em Python utilizando a biblioteca PySide6 para criação de uma interface gráfica. Ele tem como objetivo gerar senhas complexas e únicas, combinando letras maiúsculas, letras minúsculas, números e símbolos. As senhas geradas são exibidas diretamente na interface do usuário, evitando repetições de sequências ou caracteres e garantindo alta segurança.

## Funcionalidades
- Gera senhas seguras de forma aleatória.
- Evita repetição de caracteres ou sequências dentro das senhas.
- Combina diferentes tipos de caracteres: letras maiúsculas, minúsculas, números e símbolos.
- Interface gráfica simples e intuitiva.
- Permite visualizar a senha gerada diretamente em um campo de texto.

## Tecnologias Utilizadas
- **Python**: Linguagem principal do projeto.
- **PySide6**: Biblioteca para criação da interface gráfica.
- **Módulos integrados do Python**:
  - `random`: Para gerar combinações aleatórias.
  - `string`: Para acessar conjuntos de caracteres, como letras e símbolos.

## Como Usar
1. Certifique-se de ter o Python 3.9 ou superior instalado em sua máquina.
2. Instale a biblioteca PySide6 executando:
   ```bash
   pip install PySide6
   ```
3. Execute o arquivo principal do projeto:
   ```bash
   python main.py
   ```
4. Na interface aberta, clique no botão **"Gerar"** para criar uma nova senha.
5. A senha gerada será exibida no campo de texto.

## Estrutura do Projeto
- `main.py`: Arquivo principal contendo todo o código para execução do gerador de senhas e da interface gráfica.

## Exemplo de Uso
Ao clicar no botão **"Gerar"**, uma senha como `aD#123EfGh` será exibida no campo de texto. Cada senha é única e projetada para ser segura.

## Melhorias Futuras
- Adicionar opções para personalizar o comprimento da senha.
- Permitir ao usuário escolher quais tipos de caracteres incluir (ex.: somente letras e números).
- Salvar as senhas geradas em um arquivo seguro.

## Licença
Este projeto é de uso livre. Sinta-se à vontade para modificá-lo e adaptá-lo conforme suas necessidades.

