# divmod from Zerynth
#
# This is file is meant to be run through both Zerynth and Python3
# as to compare the two implementations.

try:
    # works in Zerynth
    import streams
    streams.serial()

    divmod_ = __builtins__.divmod

except:
#-if False
    # works in Python
    divmod_ = divmod
#-endif
    pass

###########################################################

fmt = '(%04s, %019s)'
def test(a, b, exp):
    got = divmod_(a,b)
    got_str = fmt % (str(got[0]), str(got[1]))
    exp_str = fmt % (str(exp[0]), str(exp[1]))
    print('divmod(%04s, %04s) ' % (str(a), str(b)), end='')
    if exp_str == got_str:
        print('== %s (pass)' % exp_str)
    else:
        print('fail\n  expected: %s\n  got: %s' % (exp, got))

###########################################################

try:
    test( 1  ,  1  , ( 1  ,  0                  ))
    test(-1  ,  1  , (-1  ,  0                  ))
    test( 1  , -1  , (-1  ,  0                  ))
    test( 2  ,  1  , ( 2  ,  0                  ))
    test( 3  ,  2  , ( 1  ,  1                  ))
    test(10  ,  3  , ( 3  ,  1                  ))

    test( 1.0,  1  , ( 1.0,  0.0                ))
    test(-1.0,  1  , (-1.0,  0.0                ))
    test( 1.0, -1  , (-1.0, -0.0                ))
    test( 2.0,  1  , ( 2.0,  0.0                ))
    test( 2.5,  2  , ( 1.0,  0.5                ))
    test( 3.0,  2  , ( 1.0,  1.0                ))
    test( 3.5,  2  , ( 1.0,  1.5                ))
    test(10.0,  3  , ( 3.0,  1.0                ))

    test( 1  ,  1.0, ( 1.0,  0.0                ))
    test(-1  ,  1.0, (-1.0,  0.0                ))
    test( 1  , -1.0, (-1.0, -0.0                ))
    test( 2  ,  1.0, ( 2.0,  0.0                ))
    test( 2  ,  1.5, ( 1.0,  0.5                ))
    test( 3  ,  1.5, ( 2.0,  0.0                ))
    test( 3  ,  2.0, ( 1.0,  1.0                ))
    test(10  ,  3.3, ( 3.0,  0.10000000000000053))

    test( 1.0,  1.0, ( 1.0,  0.0                ))
    test(-1.0,  1.0, (-1.0,  0.0                ))
    test( 1.0, -1.0, (-1.0, -0.0                ))
    test( 2.0,  1.0, ( 2.0,  0.0                ))
    test( 2.0,  1.5, ( 1.0,  0.5                ))
    test( 2.5,  2.0, ( 1.0,  0.5                ))
    test( 3.0,  2.0, ( 1.0,  1.0                ))
    test( 3.0,  1.5, ( 2.0,  0.0                ))
    test( 3.5,  2.0, ( 1.0,  1.5                ))
    test(10.0,  3.3, ( 3.0,  0.10000000000000053))

except Exception as e:
#-if False
    raise
#-endif
    print("Something bad happened:",e)
