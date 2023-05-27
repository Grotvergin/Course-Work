"""
Calculate module
"""

data = {'dig':'10', 'num1':'1.1234', 'num2':'0.5678', 'action':'*'}

def calculate(data):

    def sign(a, b):
        if a[0] != '-' and b[0] != '-':
            return a, b, 1
        elif a[0] == '-' and b[0] != '-':
            a = a[1:]
            return a, b, 2
        elif a[0] != '-' and b[0] == '-':
            b = b[1:]
            return a, b, 3
        else:
            a = a[1:]
            b = b[1:]
            return a, b, 4


    def whoisbigger(a, b):
        i = 0
        while i < len(a) - 1 and a[i] == b[i] or a[i] == ',' or b[i] == ',':
            i += 1
        if symtonum(a[i]) > symtonum(b[i]):
            return 1
        elif symtonum(a[i]) < symtonum(b[i]):
            return 2
        else:
            return 3


    def multiplication(a, b):
        itog = ""
        if whoisbigger(a, b) == 2:
            a, b = b, a
        a, b = a[::-1], b[::-1]
        z = 0
        print(a, b)
        k = max(len(a), len(b))
        for i in range(len(b)):
            res = ""
            f = 0
            if b[i] != ',':
                sa = symtonum(b[i])
                for j in range(len(a)):
                    if a[j] != ',':
                        sb = symtonum(a[j])
                        t = sa * sb + f
                        f = t // c
                        res = numtosym(t % c) + res
                if a.find(',') != -1 or b.find(',') != -1:
                    res = '0' * k + res
                    k -= 1
                    #print(res)
                    #print(len(res) - pos)
                    res = res[:(len(res) - pos)] + ',' + res[(len(res) - pos):]
                    #print(res)
                res += '0' * z
                z += 1
                #print(res)
                res, itog = fill(res, itog)
                print(itog)
                #print(res, itog)
                itog = addition(res, itog)
        #print(itog)
        return (itog)

    def translate(string):
        return int((string))


    def beautynum(res):
        while res[0] == '0' and len(res) != 1:
            res = res[1:]
        if res[0] == '-':
            while res[1] == '0' and len(res) != 2:
                res = '-' + res[2:]
        if res[:2] == "-0" and len(res) == 2:
            res = '0'
        while res[-1] == '0' and len(res)!=1:
                res = res[:-1]
        if res[-1] == ',':
            res = res[:-1]
        while res[-1] == '0' and len(res)!=1:
                res = res[:-1]
        if res == "":
            res = '0'
        return res


    def symtonum(g):
        numbers = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return numbers.find(g)


    def numtosym(u):
        numbers = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return numbers[u]


    def fill(a, b):
        if a.find(',') != -1 and b.find(',') != -1:
            sa = len(a[: a.find(',')])
            ea = len(a[a.find(',') + 1:])
            sb = len(b[: b.find(',')])
            eb = len(b[b.find(',') + 1:])
        if a.find(',') == -1 and b.find(',') != -1:
            sa, sb = len(a), len(b[: b.find(',')])
            ea, eb = -1, len(b[b.find(',') + 1:])
        elif a.find(',') != -1 and b.find(',') == -1:
            sb, sa = len(b), len(a[: a.find(',')])
            eb, ea = -1, len(a[a.find(',') + 1:])
        else:
            sa, sb = len(a), len(b)
            ea, eb = 0, 0
        if sa == sb:
            a = '0' + a
            b = '0' + b
        elif sa > sb:
            b = '0' * (sa - sb + 1) + b
            a = '0' + a
        elif sa < sb:
            a = '0' * (sb - sa + 1) + a
            b = '0' + b
        if ea > eb:
            b = b + '0' * (ea - eb)
        else:
            a = a + '0' * (eb - ea)
        if a.find(',') == -1 and b.find(',') != -1:
            a = zerotocomma(a, b.find(','))
        if a.find(',') != -1 and b.find(',') == -1:
            b = zerotocomma(b, a.find(','))
        return a, b

    def zerotocomma(string, num):
        return string[:num] + ',' + string[num + 1:]


    def addition(a, b):
        f = 0
        res = ""
        for i in range(len(b) - 1, -1, -1):
            if a[i] != ',' and b[i] != ',':
                n = symtonum(a[i]) + symtonum(b[i]) + f
                if n >= c:
                    f = 1
                    n -= c
                    res += str(numtosym(n))
                else:
                    f = 0
                    res += str(numtosym(n))
            else:
                res += ','
        return res[::-1]


    def subtraction(a, b):
        if whoisbigger(a, b) == 3:
            return '0'
        elif whoisbigger(a, b) == 1:
            f = 0
            res = ""
            for i in range(len(a) - 1, -1, -1):
                if a[i] != ',' and b[i] != ',':
                    t = symtonum(a[i]) - symtonum(b[i]) - f
                    if t < 0:
                        f = 1
                        t += c
                        res += str(numtosym(t))
                    else:
                        f = 0
                        res += str(numtosym(t))
                else:
                    res += ','
            return res[::-1]
        elif whoisbigger(a, b) == 2:
            f = 0
            res = ""
            for i in range(len(a) - 1, -1, -1):
                if a[i] != ',' and b[i] != ',':
                    t = symtonum(b[i]) - symtonum(a[i]) - f
                    if t < 0:
                        f = 1
                        t += c
                        res += str(numtosym(t))
                    else:
                        f = 0
                        res += str(numtosym(t))
                else:
                    res += ','
            return '-' + res[::-1]


    def commapos(a, b):
        pos = 0
        if ',' in a or ',' in b:
            if ',' in a:
                pos += len(a[a.find(',') + 1 :])
            if ',' in b:
                pos += len(b[b.find(',') + 1 :])
        else:
            pos = -1
        return pos



    c = int(data['dig'])
    a = data['num1'].replace('.', ',').upper()
    b = data['num2'].replace('.', ',').upper()
    d = data['action']


    a, b, s = sign(a, b)
    a, b = fill(a, b)
    pos = commapos(a, b)

    
    if d == '+':
        if s == 1:
            res = addition(a, b)
        elif s == 2:
            res = subtraction(b, a)
        elif s == 3:
            res = subtraction(a, b)
        else:
            res = addition(a, b)
            res = '-' + res
            
    elif d == '-':
        if s == 1:
            res = subtraction(a, b)
        elif s == 2:
            res = addition(a, b)
            res = '-' + res
        elif s == 3:
            res = addition(a, b)
        else:
            res = subtraction(b, a)
            
    elif d == "*":

        if s == 1 or s == 4:
            res = multiplication(a, b)
        elif s == 2 or s == 3:
            res = multiplication(a, b)
            res = '-' + res

    res = beautynum(res)
    #res_10 = translate(res)
    return res#, res_10
print(calculate(data))