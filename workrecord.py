from flask import Flask, render_template
# render_template é um helper do Flask que usamos para trazer um HTML para dentro de um arquivo do Python
# Vamos, mais adiante, chamar o render_template() em return da função.
#Aqui estamos nos referenciando a biblioteca que é o Flask,
#e a outra estamos importando a função Flask que vai nos permitir criar a aplicação.

app = Flask(__name__)
#vamos criar variável app=, onde chamamos a função Flask(), e dentro dessa função fazemos __name__, isto é,
# app = Flask(__name__), esse name faz uma referência ao próprio arquivo, garantindo que isso vai fazer rodar a aplicação.

#Criamos uma rota para o nosso site através do mecanismo abaixo
@app.route('/inicio')

#Em seguida criamos a função que define o que existe nessa rota
def ola():
    lista = ['Racismo Estrutural', 'Filosofia', 'Rápido e Devagar', 'Economia', 'Neurobiologia', 'Bioquímica', 'Física']
    return render_template('Lista.html', titulo='Lista de trabalho do dia', leituras=lista)
# Aqui, chamamos o render_template() e passamos para o seu argumento o arquivo html que queremos
app.run() #roda a aplicação

# No arquivo HTML inserimos {{ }} para passar código Python para o HTML - neste caso, apenas uma variável.
# Para escrever a estrutura for dentro do HTML usamos {% %}.
