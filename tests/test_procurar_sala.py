import registradorSalas.gerenciador as ger

def test_procurar_sala():
    gerenciador = ger.Gerenciador()
    gerenciador.registrar_sala("D04", "Mat", "Alexandre", "Matutino")
    procurar = gerenciador.procurar_sala("D04") 
    assert procurar.getNum_sala() == "D04"

def test_procurar_nao_existe():
    gerenciador = ger.Gerenciador()
    assert gerenciador.procurar_sala("C69") == False      