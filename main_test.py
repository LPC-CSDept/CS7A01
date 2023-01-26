import main
import io
import sys
import re


def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '5 4 3 2 1\n1'
    sys.stdin = io.StringIO(datastr)

    main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    # regex_string = r'[\w,\W]*1'
    # regex_string += r'[\w,\W]*3'
    # regex_string += r'[\w,\W]*5'
    # regex_string += r'[\w,\W]*'
    # print(regex_string)
    # res = re.search(regex_string, main.evenlist)
    # assert res != None
    # print(res.group())
    assert main.main.numbers[0] == 1
    assert main.main.numbers[1] == 4
    assert main.main.numbers[2] == 3
    assert main.main.numbers[3] == 2
    assert main.main.numbers[4] == 5


def test_main_2():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '5 25 15 10 0\n3'
    sys.stdin = io.StringIO(datastr)

    main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    # regex_string = r'[\w,\W]*1'
    # regex_string += r'[\w,\W]*3'
    # regex_string += r'[\w,\W]*5'
    # regex_string += r'[\w,\W]*'
    # print(regex_string)
    # res = re.search(regex_string, main.evenlist)
    # assert res != None
    # print(res.group())
    assert main.main.numbers[0] == 0
    assert main.main.numbers[1] == 5
    assert main.main.numbers[2] == 10
    assert main.main.numbers[3] == 15
    assert main.main.numbers[4] == 25
