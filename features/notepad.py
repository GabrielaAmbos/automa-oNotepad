from pywinauto import application
import time

app = application.Application()
app.start("Notepad.exe")
time.sleep(3)
app.Notepad.edit.type_keys("Teste!!!!!!", with_spaces="True")
time.sleep(2)
app.Notepad.menu_item(u'&Arquivo->Sal&var como...').click()
app.Salvar.ComboBox.edit.set_text("teste.txt")
# app.Salvar.Salvar.click()
# app.Salvar.Cancelar.click()

app.Dialog.print_control_identifiers()
