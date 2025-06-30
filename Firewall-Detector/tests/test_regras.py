from detector.regras import obter_regras_firewall

def test_obter_regras():
    regras = obter_regras_firewall()
    assert isinstance(regras, list)
    assert len(regras) > 0