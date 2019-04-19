from hashlib import md5



def md5_code(txt):
    m:md5 = md5()
    m.update(txt.encode())
    return m.hexdigest()


if __name__ == '__main__':
    print(md5_code("https://www.gushiwen.org/"))