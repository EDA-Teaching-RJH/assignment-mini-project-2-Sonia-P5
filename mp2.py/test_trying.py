from trying import feedback

def test_feedback():
    assert feedback("#EveryoneShouldComeHere.SmileFF")==True

def test_wrong_feedback():
    assert feedback("#IloveithereSmileFF")