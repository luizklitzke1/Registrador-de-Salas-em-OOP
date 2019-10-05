import registradorSalas.gerenciador as ger

def test_editar_sala():
    gerenciador = ger.Gerenciador()
    gerenciador.registrar_sala("D04", "Mat", "Alexandre", "Matutino")
    assert gerenciador.editar_sala("D04", "professor", "Giovanni" ) == True

def test_editar_sala_nao_existe():
    gerenciador = ger.Gerenciador()
    gerenciador.registrar_sala("D04", "Mat", "Alexandre", "Matutino")  
    assert gerenciador.editar_sala("D69", "professor", "Giovanni" )  == False


    