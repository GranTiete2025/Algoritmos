programa {
  inteiro jogos = -1
  cadeia top[10] 

  funcao inicio() {
    menu()
  }

  funcao vazio menu() {
    inteiro op
    faca {
      limpa()
      escreva("1 - Jogar\n2 - Top 10\n3 - Sair\n")
      escreva("Selecione uma opção: ")
      leia(op)
      escolha (op) {
        caso 1:
          jogar()
        pare
        caso 2:
          exibirTop10()
        pare
        caso 3:
        pare
        caso contrario:
          escreva("\nOpção Inválida!")
          pausa()
      }
    } enquanto (op != 3)
  }

  funcao logico pergunta(cadeia texto) {
    caracter resposta
    escreva(texto, " (S/N): ")
    leia(resposta)
    se (resposta == 'S' ou resposta == 's') {
      retorne verdadeiro
    } senao {
      retorne falso
    }
  }

  funcao vazio pausa() {
    cadeia parar
    escreva("\nPressione [Enter] para continuar...")
    leia(parar)
  }

  funcao vazio jogar() {
    jogos += 1
    se (pergunta("Você é CLT?")) {
      top[jogos] = "Meus sentimentos!!!"
    } senao {
      top[jogos] = "Você é fodão, herdeiro!!!"
    } 
    escreva(top[jogos])
    pausa()
  }

  funcao vazio exibirTop10() {
    
    se (jogos == -1) {
      escreva("\nNão existem jogos registrados!!")
    } senao {
      limpa()
      escreva("Últimos jogos - Top 10\n\n")
      para (inteiro i = 0; i <= jogos; i++) {
        escreva(i + 1, " - ", top[i], "\n")
      }
    }
    pausa()
  }
}
