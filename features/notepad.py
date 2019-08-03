from pywinauto import *
from pywinauto.keyboard import *
import time

class Notepad:


    def __init__(self):
        self.notepad = Application(backend="win32").start('notepad.exe')
        self.dlg = Desktop(backend="win32").Notepad

    def digitarTexto(self, texto):
        self.dlg.edit.type_keys(str(texto), with_spaces="True")

    def abrirMenuSalvar(self):
        self.dlg.menu_item(u'&Arquivo->Sal&var como...').click()

    def salvar(self, nome):
        send_keys(nome, with_spaces=True)
        send_keys('{ENTER}')

    def exibirDataEHora(self):
        self.dlg.menu_item(u' &Editar->Hora/&data\tF5').click()

    def getText(self):
        text = self.dlg.child_window(class_name="Edit")
        return text

    def abrirMenuImprimir(self):
        self.dlg.menu_item(u'&Arquivo->&Imprimir...\tCtrl+P').click()

    def imprimir(self):
        send_keys('{ENTER}')

