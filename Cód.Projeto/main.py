import json
lista_estud = []
lista_professores = []
lista_materias = []
lista_turmas = []
lista_matriculas = []
def mostrar_menu_inicial():   #Apresentando o menu inicial ao usuário
    print("_____MENU INICIAL - SISTEMA DE NAVEGAÇÃO ACADÊMICA_____")
    print('1 - Estudantes')
    print("2 - Professores")
    print("3 - Matérias")
    print("4 - Turmas")
    print("5 - Matrícula")
    print("6 - Sair ")
    return int(input("Digite o número da opção desejada: "))
def mostrar_menu_operacoes():   #Apresentando o menu de operações ao usuário
    print("_____MENU DE OPERAÇÕES_____")
    print("1 - Atualizar Dados")
    print("2 - Cadastrar")
    print("3 - Excluir")
    print("4 - Listar")
    print("5 - Menu Inicial")
    return int(input("Digite o número da opção desejada: "))

def atualizar_cadastro( lista_estud, lista_professores, lista_materias, lista_turmas, lista_matriculas):
    if opcao1 == 1:   #Função atualizar cadastro de alunos
        print('Atualizar Cadastro de Estudante')
        cod_atualizar_est = int(input("Insira o código do estudante que deseja atualizar: "))
        estudante_atualizado = None
        for estudante in lista_estud:
            if estudante.get('codigo') == cod_atualizar_est:
                estudante_atualizado = estudante
                break
        if estudante_atualizado is None:
            print(f"Código {cod_atualizar_est} não encontrado!")
        else:
            novo_cod_est = int(input('Digite o novo código do estudante: '))
            novo_nome_est = input("Digite o novo nome do estudante: ")
            novo_cpf_est = input('Digite o novo CPF do estudante: ')
            estudante_atualizado['codigo'] = novo_cod_est
            estudante_atualizado['estudante'] = novo_nome_est
            estudante_atualizado['cpf_est'] = novo_cpf_est
            print("Atualizado com sucesso!")
            print(estudante_atualizado)
    elif opcao1 == 2:   #Função atualizar cadastro de profssores
        print('Atualizar Cadastro de Professor')
        cod_atualizar_pro = int(input("Insira o código do professor que deseja atualizar: "))
        professor_atualizado = None
        for professor in lista_professores:
            if professor.get('codigo') == cod_atualizar_pro:
                professor_atualizado = professor
                break
        if professor_atualizado is None:
            print(f"Código {cod_atualizar_pro} não encontrado!")
        else:
            novo_cod_pro = int(input('Digite o novo código do professor: '))
            novo_nome_pro = input("Digite o novo nome do professor: ")
            novo_cpf_pro = input('Digite o novo CPF do professor: ')
            professor_atualizado['codigo'] = novo_cod_pro
            professor_atualizado['professor'] = novo_nome_pro
            professor_atualizado['cpf_prof'] = novo_cpf_pro
            print("Atualizado com sucesso!")
            print(professor_atualizado)
    elif opcao1 == 3:   #Função atualizar cadastro de matérias
        print('Atualizar Matéria')
        codp_atualizar_mat = int(input("Insira o código da matéria que deseja atualizar: "))
        materia_atualizada = None
        for materia in lista_materias:
            if materia['codigo_mat'] == codp_atualizar_mat:
                materia_atualizada = materia
                break
        if materia_atualizada is None:
            print(f"Código {codp_atualizar_mat} não encontrado!")
        else:
            novo_cod_mat = int(input('Digite o novo código da matéria:'))
            novo_nome_mat = input("Digite o novo nome: ")
            materia_atualizada['codigo_mat'] = novo_cod_mat
            materia_atualizada['materia'] = novo_nome_mat
            print("Atualizado com sucesso!")
            print(materia_atualizada)
    elif opcao1 == 4:   #Função atualizar cadastro de turmas
        print('Atualizar Cadastro de Turma')
        codp_atualizar_turma = int(input("Insira o código da turma que deseja atualizar: "))
        turma_atualizada = None
        for turma in lista_turmas:
            if turma['turma'] == codp_atualizar_turma:
                turma_atualizada = turma
                break
        if turma_atualizada is None:
            print(f"Código {codp_atualizar_turma} não encontrado!")
        else:
            novo_cod_turma = int(input('Digite o novo código da turma:'))
            turma_atualizada['turma'] = novo_cod_turma
            print("Atualizado com sucesso!")
            print(turma_atualizada)
    elif opcao1 == 5:   #Função atualizar cadastro de matrículas
        print('Atualizar Matrícula')
        codp_atualizar_matricula = int(input("Insira o código da matrícula que deseja atualizar: "))
        matricula_atualizada = None
        for matricula in lista_matriculas:
            if matricula['matricula'] == codp_atualizar_matricula:
                matricula_atualizada = matricula
                break
        if matricula_atualizada is None:
            print(f"Código {codp_atualizar_matricula} não encontrado!")
        else:
            novo_cod_matricula = int(input('Digite o novo código da matricula:'))
            matricula_atualizada['matricula'] = novo_cod_matricula
            print("Atualizado com sucesso!")
            print(matricula_atualizada)
    else:
        print("Opção inválida")

def fazer_cadastro(lista_estud, lista_professores, lista_materias, lista_turmas, lista_matriculas):
    if opcao1 == 1:   #Fazendo cadastro de estudante
        print('Cadastrar Estudante')
        nome = str(input("Insira o nome completo do novo estudante: "))
        cod = int(input("Digite o número do código de segurança do estudante: "))
        cpf = input("Digite o CPF do estudante: ")
        dados_estudantes = {}
        dados_estudantes['estudante'] = nome
        dados_estudantes[('codigo')] = cod
        dados_estudantes['cpf_est'] = cpf
        lista_estud.append(dados_estudantes)
        guardar_arquivo(lista_estud, lista_professores, lista_materias, lista_turmas, lista_matriculas)
        print('Estudante cadastrado com sucesso!')
    elif opcao1 == 2:   #Fazendo cadastro de professor
        print('Cadastrar Professor')
        nome = str(input("Insira o nome completo do novo professor: "))
        cod = int(input("Digite o número do código de segurança do professor: "))
        cpf = input("Digite o CPF do professor: ")
        dados_professores = {}
        dados_professores['professor'] = nome
        dados_professores['codigo'] = cod
        dados_professores['cpf_prof'] = cpf
        lista_professores.append(dados_professores)
        guardar_arquivo(lista_estud, lista_professores, lista_materias, lista_turmas, lista_matriculas)
        print('Professor cadastrado com sucesso!')
    elif opcao1 == 3:  #Fazendo cadastro de matéria
        print('Cadastrar Matéria')
        nome_materia = str(input("Insira o nome da nova matéria: "))
        cod_materia = int(input("Digite o número do código da matéria: "))
        dados_materias = {}
        dados_materias['materia'] = nome_materia
        dados_materias['codigo_mat'] = cod_materia
        lista_materias.append(dados_materias)
        guardar_arquivo(lista_estud, lista_professores, lista_materias, lista_turmas, lista_matriculas)
        print('Matéria cadastrada com sucesso!')
    elif opcao1 == 4:   #Fazendo cadastro de turma
        print('Cadastrar Turma')
        cod_turma = int(input("Digite o número do código da turma: "))
        cod_pro = int(input("Digite o número do código do professor: "))
        cod_materia = int(input("Digite o número do código da matéria: "))
        dados_turmas = {}
        dados_turmas['turma'] = cod_turma
        dados_turmas['codigo_pro'] = cod_pro
        dados_turmas['codigo_mat'] = cod_materia
        lista_turmas.append(dados_turmas)
        guardar_arquivo(lista_estud, lista_professores, lista_materias, lista_turmas, lista_matriculas)
        print('Turma cadastrada com sucesso!')
    elif opcao1 == 5:   #Fazendo cadastro de matrícula
        print('Cadastrar Matrícula')
        cod_matricula = int(input("Digite o número do código da matrícula "))
        cod_turma = int(input("Digite o número do código da turma: "))
        cod_est = int(input("Digite o número do código do estudante: "))
        dados_matricula = {}
        dados_matricula['matricula'] = cod_matricula
        dados_matricula['turma'] = cod_turma
        dados_matricula['estudante'] = cod_est
        lista_matriculas.append(dados_matricula)
        guardar_arquivo(lista_estud, lista_professores, lista_materias, lista_turmas, lista_matriculas)
        print('Matrícula cadastrada com sucesso!')
    else:
        print("Opção inválida")

def excluir_cadastro(lista_estud, lista_professores, lista_materias, lista_turmas, lista_matriculas):
    if opcao1 == 1:   # Excluindo cadastro professor
        print('Excluir Estudante')
        codp_excluir_est = int(input("Digite o código do estudante que deseja excluir: "))
        estudante_removido = None
        for dados_estudante in lista_estud:
            if dados_estudante['codigo'] == codp_excluir_est:
                estudante_removido = dados_estudante
                break
        if estudante_removido is None:
            print(f"Código {codp_excluir_est} não encontrado")
        else:
            lista_estud.remove(estudante_removido)
            print('Estudante removido com sucesso!')
    elif opcao1 == 2:   # Excluindo cadastro professor
        print('Excluir Professor')
        codp_excluir_pro = int(input("Digite o código do professor que deseja excluir: "))
        professor_removido = None
        for dados_professores in lista_professores:
            if dados_professores['codigo'] == codp_excluir_pro:
                professor_removido = dados_professores
                break
        if professor_removido is None:
            print(f"Código {codp_excluir_pro} não encontrado")
        else:
            lista_professores.remove(professor_removido)
            print('Professor removido com sucesso!')
    elif opcao1 == 3:   # Excluindo matéria
        print('Excluir Matéria')
        codp_excluir_mat = int(input("Digite o código da matéria que deseja excluir: "))
        materia_removida = None
        for dados_materias in lista_materias:
            if dados_materias['codigo_mat'] == codp_excluir_mat:
                materia_removida = dados_materias
                break
        if materia_removida is None:
            print(f"Código {codp_excluir_mat} não encontrado")
        else:
            lista_materias.remove(materia_removida)
            print('Matéria removida com sucesso!')
    elif opcao1 == 4:   # Excluindo turma
        print('Excluir Turma')
        codp_excluir_turma = int(input("Digite o código da turma que deseja excluir: "))
        turma_removida = None
        for dados_turmas in lista_turmas:
            if dados_turmas['turma'] == codp_excluir_turma:
                turma_removida = dados_turmas
                break
        if turma_removida is None:
            print(f"Código {codp_excluir_turma} não encontrado")
        else:
            lista_turmas.remove(turma_removida)
        print('Turma removida com sucesso!')
    elif opcao1 == 5:   # Excluindo matricula
        print('Excluir Matrícula')
        codp_excluir_matricula = int(input("Digite o código da matrícula que deseja excluir: "))
        matricula_removida = None
        for dados_matricula in lista_matriculas:
            if dados_matricula['matricula'] == codp_excluir_matricula:
                matricula_removida = dados_matricula
                break
        if (matricula_removida is None):
            print(f"Código {codp_excluir_matricula} não encontrado")
        else:
            lista_matriculas.remove(matricula_removida)
        print('Matrícula removida com sucesso!')
    else:
        print("Opção inválida")

def listando_cadastros(lista_estud, lista_professores, lista_materias, lista_turmas, lista_matriculas):
    if opcao1 == 1:   #Fazendo listagem de estudantes
        print("Listagem de Estudantes")
        if not lista_estud:
            print('AINDA NÃO HÁ ALUNOS CADASTRADOS')
        else:
            for dados_estudantes in lista_estud:
                print(dados_estudantes)
    elif opcao1 == 2:   #Fazendo listagem de professores
        print("Listagem de Professores")
        if not lista_professores:
            print('AINDA NÃO HÁ PROFESSORES CADASTRADOS')
        else:
            for dados_professores in lista_professores:
                print(dados_professores)
    elif opcao1 == 3:   #Fazendo listagem de Matérias
        print("Listagem de Matérias")
        if not lista_materias:
            print("AINDA NÃO HÁ MATÉRIAS CADASTRADAS")
        else:
            for dados_materias in lista_materias:
                print(dados_materias)
    elif opcao1 == 4:   #Fazendo listagem de turmas
        print("Listagem de Turmas")
        if not lista_turmas:
            print("AINDA NÃO HÁ TURMAS CADASTRADAS")
        else:
            for dados_turmas in lista_turmas:
                print(dados_turmas)
    elif opcao1 == 5:   #Fazendo listagem de matriculas
        print("Listagem de Matrículas")
        if not lista_matriculas:
            print("AINDA NÃO HÁ MATRÍCULAS CADASTRADAS")
        else:
            for dados_matricula in lista_matriculas:
                print(dados_matricula)
def guardar_arquivo(lista_estud, lista_professores, lista_materias, lista_turmas, lista_matriculas):
    dados = {'estudantes': lista_estud, 'professores': lista_professores, 'materia': lista_materias, 'turmas': lista_turmas, 'matriculas': lista_matriculas}
    with open('dados_gerais.json', 'w') as arquivo:
        json.dump(dados, arquivo)

def ler_arquivo():
    try:
        with open('dados_gerais.json', 'r') as arquivo:
            dados = json.load(arquivo)
            return dados.get('estudantes', []), dados.get('professores', []), dados.get('materia', []), dados.get('turmas', []), dados.get('matriculas', [] )
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return [], [], [], [], []

while True:
    opcao1 = mostrar_menu_inicial()
    if opcao1 == 1 or 2 or 3 or 4 or 5:
        lista_estud, lista_professores, lista_materias, lista_turmas, lista_matriculas = ler_arquivo()
        while True:
            opcao2 = mostrar_menu_operacoes()
            if opcao2 == 1:
                atualizar_cadastro(lista_estud, lista_professores, lista_materias, lista_turmas, lista_matriculas)
            elif opcao2 == 2:
                fazer_cadastro(lista_estud, lista_professores, lista_materias, lista_turmas, lista_matriculas)
            elif opcao2 == 3:
                excluir_cadastro(lista_estud, lista_professores, lista_materias, lista_turmas, lista_matriculas)
            elif opcao2 == 4:
                listando_cadastros(lista_estud, lista_professores, lista_materias, lista_turmas, lista_matriculas)
            elif opcao2 == 5:
                print("VOLTANDO AO MENU INICIAL")
                break
    elif opcao1 == 6:
        print("Saindo...")
        break
    else:
     print('OPÇÃO INVÁLIDA')

