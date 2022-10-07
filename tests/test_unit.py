import functions

def test_add_taps():
    string = "This is a test"
    assert functions.addTaps(string, 1) == "\tThis is a test"

def test_new_lines():
    string = "This is a test"
    #if condition returns True, then nothing happens:
    assert functions.addNewLines(string, 1) == "\nThis is a test"

def test_break_up_sentences():
    string = "This is a test. This is a test."
    assert functions.breakUpSentences(string) == "This is a test.\n This is a test.\n"

def test_space_after_comment():
    string = "%This is a test"
    assert functions.addSpaceInComment(string) == "% This is a test"