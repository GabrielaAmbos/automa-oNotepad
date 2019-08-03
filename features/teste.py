from pywinauto import *
import time

app = application.Application()
app.start("Notepad.exe")
# app.Notepad.menu_item(u'&Editar->Hora/&data\tF5').click()

app.Notepad.edit.type_keys("Teste!!!!!!", with_spaces="True")
app.Notepad.menu_item(u'&Arquivo->&Imprimir...\tCtrl+P').click()
app.Imprimir.Button3.click()

app.Dialog.print_control_identifiers()
# app.Notepad.PrintControlIdentifiers()