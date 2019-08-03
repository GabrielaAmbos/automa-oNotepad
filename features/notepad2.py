from pywinauto import *


class Notepad:

    def __init__(self):
        self.notepad = Application(backend="win32").start('notepad.exe')
        self.dlg = Desktop(backend="win32").Notepad

    def digitarTexto(self, texto):
        self.dlg.edit.type_keys(str(texto), with_spaces="True")

    def abrirMenuSalvar(self):
        self.dlg.menu_item(u'&Arquivo->Sal&var como...').click()

    def renomearArquivoESalvar(self, nome):
        # self.dlg.child_window(title="Salvar como", class_name="#32770").select()
        # self.dlg.child_window(title="*.txt", class_name="Edit").edit.set_text(str(nome))
        self.dlg.Salvar.ComboBox.edit.set_text(str(nome))
        # self.dlg.Salvar.edit.set_text(str(nome))
        self.dlg.Salvar.Salvar.click()

    def exibirDataEHora(self):
        self.dlg.menu_item(u' &Editar->Hora/&data\tF5').click()

    def getText(self):
        text = self.dlg.child_window(class_name="Edit")
        return text

    def abrirMenuImprimir(self):
        self.dlg.menu_item(u'&Arquivo->&Imprimir...\tCtrl+P').click()
        self.dlg.Imprimir.Button3.click()
