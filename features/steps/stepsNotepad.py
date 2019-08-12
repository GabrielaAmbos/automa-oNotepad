from behave import *
from features.notepad import Notepad


@given('que eu abra o notepad')
def step_impl(context):
    context.notepad = Notepad()


@when('eu escrevo uma frase qualquer')
def step_impl(context):
    context.notepad.digitarTexto(str('Teste notepad'))


@when('seleciono a opção salvar')
def step_impl(context):
    context.notepad.abrirMenuSalvar()


@then('o arquivo é salvo')
def step_impl(context):
    context.notepad.digitarNaCaixa(str('teste.txt'))
    context.notepad.botaoConfirmar()


@when('eu seleciono a opção Hora/Data')
def step_impl(context):
    context.notepad.abrirMenuDataHora()


@then('é exibido a hora {atual}')
def step_impl(context, atual):
    context.notepad.getText() == atual


@when('seleciono a opção Imprimir')
def step_impl(context):
    context.notepad.abrirMenuImprimir()


@then('o arquivo vai para a fila de impressão')
def step_impl(context):
    context.notepad.botaoConfirmar()


@when('eu seleciono a opção Abrir')
def step_impl(context):
    context.notepad.abrirMenuAbrir()


@when('pesquiso pelo arquivo {nome}')
def step_impl(context, nome):
    context.notepad.digitarNaCaixa(str(nome))


@then('clico em abrir')
def step_impl(context):
    context.notepad.botaoConfirmar()


@when('eu seleciono a opção Fonte')
def step_impl(context):
    context.notepad.abrirMenuFonte()


@when('altero os valores')
def step_impl(context):
    context.notepad.digitarNaCaixa('Arial')
    context.notepad.mudarCampo()
    context.notepad.mudarCampo()
    context.notepad.digitarNaCaixa('14')
    context.notepad.botaoConfirmar()


@then('escrevo a frase {texto}')
def step_impl(context, texto):
    context.notepad.digitarTexto(texto)


@when('seleciono as opções para copiar')
def step_impl(context):
    context.notepad.abrirMenuSelecionarTudo()
    context.notepad.abrirMenuCopiar()


@then('a frase é duplicada')
def step_impl(context):
    context.notepad.abrirMenuColar()


