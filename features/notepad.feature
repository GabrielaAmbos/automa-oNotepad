Feature: notepad

  Scenario: Escrever uma frase e salvar o arquivo
    Given que eu abro o notepad
    When eu escrevo a frase Teste Notepad
    And eu seleciono a opção salvar
    Then o arquivo é salvo com o nome de teste.txt

  Scenario: Exibir hora e data
    Given que eu abro o notepad
    When eu vou no menu e seleciono Hora/Data
    Then é exibido 18:21 31/07/2019

  Scenario: imprimir um texto
    Given que eu abro o notepad
    When eu escrevo a frase Me imprima!!!!
    And seleciono a opção imprimir
    Then eu clico em Imprimir

  Scenario: Abrir um arquivo
    Given que eu abro o notepad
    When eu seleciono a opção abrir
    And pesquiso pelo arquivo teste.txt
    Then clico em abrir

  Scenario: Mudar a fonte
    Given que eu abro o notepad
    When seleciono a opção fonte
    And altero o tipo de fonte para arial
    And o tamanho para 14
    And clico em OK
    Then escrevo a frase A fonte deve ser Arial 14

  Scenario: Copiar e colar uma frase
    Given que eu abro o notepad
    When eu escrevo a frase Copie isso!!!
    And seleciono a opção Selecionar tudo
    And seleciono a opção Copiar
    Then seleciono a opção Colar


