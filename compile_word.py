# --------------
# User Instructions
#
# Write a function, compile_word(word), that compiles a word
# of UPPERCASE letters as numeric digits. For example:
# compile_word('YOU') => '(1*U + 10*O +100*Y)' 
# Non-uppercase words should remain unchaged.

def compile_word(word):
    """Compile a word of uppercase letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    Non-uppercase words unchanged: compile_word('+') => '+'"""
    if not word.isupper(): return word
    else: 
        ret_str = ''
        for rt_index in range(len(word)-1, -1, -1):
            ret_str += '1'+'0'*(len(word)-rt_index-1)+'*'+word[rt_index]+'+' 
    return "(" +ret_str[:len(ret_str)-1]+")"     # strip trailing '+'

def test():
    ''' test cases for compile word '''
    assert compile_word('YOU') == "(1*U+10*O+100*Y)"
    print "compile_word('YOU') is ", compile_word('YOU')
    return 'tests pass'

print test()

