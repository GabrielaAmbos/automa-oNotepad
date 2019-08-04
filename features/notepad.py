from pywinauto import *
from pywinauto.keyboard import *


class Notepad:

    def __init__(self):
        self.notepad = Application(backend="win32").start('notepad.exe')
        self.dlg = Desktop(backend="win32").Notepad

    def digitarTexto(self, texto):
        self.dlg.edit.type_keys(str(texto), with_spaces="True")
        send_keys('{ENTER}')

    def botaoConfirmar(self):
        send_keys('{ENTER}')

    def digitarNaCaixa(self, nome):
        send_keys(nome, with_spaces=True)

    def mudarCampo(self):
        send_keys('{TAB}')

    def getText(self):
        text = self.dlg.child_window(class_name="Edit")
        return text

    def abrirMenuSalvar(self):
        self.dlg.menu_item(u'&Arquivo->Sal&var como...').click()

    def abrirMenuImprimir(self):
        self.dlg.menu_item(u'&Arquivo->&Imprimir...\tCtrl+P').click()

    def abrirMenuAbrir(self):
        self.dlg.menu_item(u'&Arquivo->A&brir...\tCtrl+O').click()

    def abrirMenuSelecionarTudo(self):
        self.dlg.menu_item(u'&Editar->Selecionar &tudo\tCtrl+A').click()

    def abrirMenuCopiar(self):
        self.dlg.menu_item(u'&Editar->&Copiar\tCrtl+C').click()

    def abrirMenuColar(self):
        self.dlg.menu_item(u'&Editar->&Colar\tCrtl+V').click()
        self.dlg.menu_item(u'&Editar->&Colar\tCrtl+V').click()

    def abrirMenuDataHora(self):
        self.dlg.menu_item(u' &Editar->Hora/&data\tF5').click()

    def abrirMenuFonte(self):
        self.dlg.menu_item(u'&Formatar->F&onte...').click()
