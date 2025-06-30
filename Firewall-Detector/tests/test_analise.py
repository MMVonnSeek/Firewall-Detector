from detector.analise import testar_porta

def test_porta_80_google():
    assert testar_porta("8.8.8.8", 53) is True  # DNS do Google