import registradorSalas.gerenciador as ger

def test_remover_sala():
    gerenciador = ger.Gerenciador()

    gerenciador.registrar_sala("D04", "Mat", "Alexandre", "Matutino") 
    assert gerenciador.remover_sala("D04") == True

def test_remover_sala_nao_existe():
    gerenciador = ger.Gerenciador()

    assert gerenciador.remover_sala("D04") == False       