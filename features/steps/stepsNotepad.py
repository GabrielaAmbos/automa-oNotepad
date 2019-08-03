from behave import *
from features.notepad import Notepad


@given('que eu abro o notepad')
def step_impl(context):
    context.notepad = Notepad()


@when('eu escrevo a frase {texto}')
def step_impl(context, texto):
    context.notepad.digitarTexto(str(texto))


@when('eu seleciono a opção salvar')
def step_impl(context):
    context.notepad.abrirMenuSalvar()


@then('o arquivo é salvo com o nome de {nome}')
def step_impl(context, nome):
    context.notepad.salvar(str(nome))


@when('eu vou no menu e seleciono Hora/Data')
def step_impl(context):
    context.notepad.exibirDataEHora()


@then('é exibido {horaAndData}')
def step_impl(context, horaAndData):
    context.notepad.getText() == horaAndData


@when('seleciono a opção imprimir')
def step_impl(context):
    context.notepad.abrirMenuImprimir()


@then('eu clico em Imprimir')
def step_impl(context):
    context.notepad.imprimir()
