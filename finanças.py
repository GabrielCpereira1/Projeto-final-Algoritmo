import json
from datetime import datetime

CATEGORIAS = ["Alimentação", "Transporte", "Saúde", "Lazer", "Trabalho", "Outros"]

def menu():
 while True:
   print("-- Finanças Pessoais --") 
   print("1 - Acessar Conta")
   print("2 - Sair")

   opcao = input("Escolha Uma Opção: ")

   if opcao == "1":
     acessar_conta()

   elif opcao == "2":
     sair()
   
   else:
     print("Opção Invalida")

def acessar_conta():
    credenciais = json.load(open("usuarios.json", "r"))
    tentativas = 3
    while tentativas > 0:
        usuario = input("Usuario:")
        senha = input("Senha:")

        if usuario == credenciais["usuario"] and senha == credenciais["senha"]:
          print("Login Realizado")
          menu_principal()
          return

        else:
            tentativas -= 1
            print(f"Usuario ou senha incorreta, Restam: {tentativas}")
    print("Conta bloqueada. Tente novamnete mais tarde.")

def sair():
  print("Saindo...")
  exit()

def menu_principal():
   while True:
      print("-- Menu Principal --")
      print("1 - Adicionar Entrada")
      print("2 - Adicionar Saída")
      print("3 - Relatório do Mês")
      print("4 - Sair")

      opcao = input("Escolha Uma Opção")
    
      if opcao == "1":
         adicionar_transacao("entrada")
      elif opcao == "2":
         adicionar_transacao("saida") 
      elif opcao == "3":
         relatorio()
      elif opcao == "4":
         sair()
      else:
         print("Opção Invalida")

def escolher_categoria():
   print("\n -- Categorias --")
   i = 1
   for categorias in CATEGORIAS:
     print(f"{i} - {categorias}")
     i += 1

   opcao = input("Escolha uma Categoria: ")

   if opcao.isdigit() and 1 <= int(opcao) <= len(CATEGORIAS):
        return CATEGORIAS[int(opcao) - 1]
   else:
        print("Categoria inválida, usando 'Outros'.")
        return "Outros"
   
  
def adicionar_transacao(tipo):
    descricao = input("Descrição: ")
    categoria = escolher_categoria()

    try:
        valor = float(input("Valor: R$ "))
    except ValueError:
       print("Valor inválido.")
       return
    
    try:
        with open("transacoes.json", "r") as f:
            transacoes = json.load(f)
    except FileNotFoundError:
        transacoes = [] 
    
    transacoes.append ({
       "tipo": tipo,
       "descrição": descricao,
       "categoria": categoria,
       "valor": valor,
       "data": datetime.now().strftime("%d/%m/%Y")

    })

    with open("transacoes.json", "w") as f:
        json.dump(transacoes, f, indent=4, ensure_ascii=False)

    print(f"\n{tipo.capitalize()} de R$ {valor:.2f} Registrada Com Sucesso\n")

def relatorio():
   try:
      with open("transacoes.json", "r") as f:
           transacoes = json.load(f)
   except FileNotFoundError:
        print("Nenhuma transação registrada.\n")
        return
   
   mes_atual = datetime.now().strftime("%m/%Y")

   print(f"\n-- Relatório: {mes_atual} --")

   total_entradas = 0
   total_saidas = 0

   for t in transacoes:
       if t["data"].endswith(mes_atual):
          if t["tipo"] == "entrada" :
             total_entradas += t["valor"]
             label = "Entradas"
          else:
             total_saidas += t["valor"]
             label = "Saídas"
          print(f"{label}: {t ['data']} - {t['categoria']} - {t['descrição']} - R$ {t['valor']:.2f}")
  
   saldo = total_entradas - total_saidas

   print(f"\nTotal Entradas : R$ {total_entradas:.2f}")
   print(f"Total Saídas   : R$ {total_saidas:.2f}")
   print(f"Saldo          : R$ {saldo:.2f}")

   if saldo >= 0:
        print("Saldo Positivo ✔\n")
   else:
        print("Saldo Negativo ✖\n")  
menu()

 
 

