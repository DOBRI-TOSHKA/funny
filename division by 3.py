import re
import sys

# Вам дана последовательность строк.
# Выведите строки, содержащие двоичную запись числа, кратного 3.

pattern = r"^((1(01*0)*1|0)*)$"


for line in sys.stdin:
    try:
        test_line = line.rstrip()
        f = re.findall(pattern, test_line)
        if f is not [] and f[0][0] == test_line:
            print(f[0][0])
    except IndexError:
        pass
