#language: pt

Funcionalidade: notepad

  Cenário: Escrever uma frase e salvar o arquivo
    Dado que eu abra o notepad
    Quando eu escrevo uma frase qualquer
    E seleciono a opção salvar
    Então o arquivo é salvo

  Cenário: Exibir hora e data
    Dado que eu abra o notepad
    Quando eu seleciono a opção Hora/Data
    Então é exibido a hora atual

  Cenário: Imprimir um texto
    Dado que eu abra o notepad
    Quando eu escrevo uma frase qualquer
    E seleciono a opção Imprimir
    Então o arquivo vai para a fila de impressão

   Cenário: Abrir um arquivo qualquer
     Dado que eu abra o notepad
     Quando eu seleciono a opção Abrir
     E pesquiso pelo arquivo teste.txt
     Então clico em abrir

   Cenário: Mudar a fonte
     Dado que eu abra o notepad
     Quando eu seleciono a opção Fonte
     E altero os valores
     Então escrevo a frase Arial tamanho 14

   Cenário: Copiar e colar uma frase qualquer
     Dado que eu abra o notepad
     Quando eu escrevo uma frase qualquer
     E seleciono as opções para copiar
     Então a frase é duplicada


