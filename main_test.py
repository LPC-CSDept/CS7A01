import main
import io
import sys
import re


def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    # datastr = '5 4 3 2 1\n1'
    # sys.stdin = io.StringIO(datastr)

    main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    regex_string = r'[\w,\W]*ello'
    regex_string += r'[\w,\W]*orld'
    regex_string += r'[\w,\W]*'
    print(regex_string)
    res = re.search(regex_string, lines[0])
    assert res != None

    regex_string = r'[\w,\W]*CS7'
    regex_string += r'[\w,\W]*Introduction'
    regex_string += r'[\w,\W]*'
    print(regex_string)
    res = re.search(regex_string, lines[1])
    assert res != None
    # print(res.group())
    # assert main.main.numbers[0] == 1
    # assert main.main.numbers[1] == 4
    # assert main.main.numbers[2] == 3
    # assert main.main.numbers[3] == 2
    # assert main.main.numbers[4] == 5
