import registradorSalas.gerenciador as ger

def test_registrar_sala():
    gerenciador = ger.Gerenciador()

    assert gerenciador.registrar_sala("D04", "Mat", "Alexandre", "Matutino") == 2

def test_registrar_sala_invalido():
    gerenciador = ger.Gerenciador()

    assert gerenciador.registrar_sala("", "", "", "") == 1

def test_registrar_sala_repetido():
    gerenciador = ger.Gerenciador()

    gerenciador.registrar_sala("D04", "Mat", "Alexandre", "Matutino")  
    assert gerenciador.registrar_sala("D04", "Mat", "Alexandre", "Matutino") == 3
