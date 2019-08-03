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
    And seleciono a opção imprimir e clico em Imprimir
    Then o arquivo vai para a impressão

