# Teste de Automação: Login e Compra em Website

## Descrição

Este script foi criado como parte de um desafio para automatizar o processo de login e compra no site [SauceDemo](https://www.saucedemo.com), neste projeto o Selenium é utilizado para controlar o navegador web e automatizar processos.

## Linguagens e Frameworks Utilizados
- Python: 3.12
- Selenium: 4.15.2

## Etapas
De acordo com as regras do desafio, o script realiza as seguintes etapas:

1. Acessa a página de login do SauceDemo.
2. Extrai os nomes de usuários e a senha do arquivo CSV.
3. Seleciona um usuário aleatório entre os disponíveis e realiza o login.
4. Adiciona os itens solicitados ao carrinho.
5. Visualiza o carrinho.
6. Prossegue para a finalização da compra, especificando o nome, sobrenome e CEP do usuário.
7. Finaliza a compra exibindo o valor total no console.

## Dependências
Além do Python 3.12 e Selenium 4.15.2, o script requer algumas dependências adicionais para funcionar:
- ChromeDriver
    - Utilizado para abrir e controlar o Google Chrome durante a automação.
    - Certifique-se de que o ChromeDriver está instalado e configurado no PATH do sistema.
      Obs: Costuma vir junto com a instalação do google chrome nas novas versões
- Google Chrome
    - Navegador utilizado no script.

## Instalação e Uso

### Clonar o Repositório:

```
cd pasta_desejada
git clone https://github.com/PhFariaa/Projeto_Automacao.git
cd Projeto_Automacao
```

### Instale o selenium
```
Pip install selenium==4.15.2
```

### Rode o script
```
python main.py
```
