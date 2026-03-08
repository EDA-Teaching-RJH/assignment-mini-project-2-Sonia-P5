from verifying_code import pay

def test_pay():
    assert pay("$70")==True

def test_wrong_pay():
    assert pay("70")==False