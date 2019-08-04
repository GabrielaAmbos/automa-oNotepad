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
    context.notepad.digitarNaCaixa(str(nome))
    context.notepad.botaoConfirmar()


@when('eu vou no menu e seleciono Hora/Data')
def step_impl(context):
    context.notepad.abrirMenuDataHora()


@then('é exibido {horaAndData}')
def step_impl(context, horaAndData):
    context.notepad.getText() == horaAndData


@when('seleciono a opção imprimir')
def step_impl(context):
    context.notepad.abrirMenuImprimir()


@then('eu clico em Imprimir')
def step_impl(context):
    context.notepad.botaoConfirmar()


@when('eu seleciono a opção abrir')
def step_impl(context):
    context.notepad.abrirMenuAbrir()


@when('pesquiso pelo arquivo {nome}')
def step_impl(context, nome):
    context.notepad.digitarNaCaixa(str(nome))


@then('clico em abrir')
def step_impl(context):
    context.notepad.botaoConfirmar()


@when('seleciono a opção fonte')
def step_impl(context):
    context.notepad.abrirMenuFonte()


@when('altero o tipo de fonte para {fonte}')
def step_impl(context, fonte):
    context.notepad.digitarNaCaixa(fonte)
    context.notepad.mudarCampo()
    context.notepad.mudarCampo()


@when('o tamanho para {tamanho}')
def step_impl(context,tamanho):
    context.notepad.digitarNaCaixa(tamanho)


@when('clico em OK')
def step_impl(context):
    context.notepad.botaoConfirmar()


@then('escrevo a frase {texto}')
def step_impl(context, texto):
    context.notepad.digitarTexto(texto)


@when('seleciono a opção Selecionar tudo')
def step_impl(context):
    context.notepad.abrirMenuSelecionarTudo()


@when('seleciono a opção Copiar')
def step_impl(context):
    context.notepad.abrirMenuCopiar()


@then('seleciono a opção Colar')
def step_impl(context):
    context.notepad.abrirMenuColar()


