import base64
import os

def img2base64(fp):
    with open(fp, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        s = base64_data.decode()
        return s

def test_img2base64():
    if os.path.exists('./test/1.txt'):
        os.remove('./test/1.txt')
    if os.path.exists('./test/1(re).png'):
        os.remove('./test/1(re).png')

    with open('./test/1.txt', 'wb') as f:
        f.write(bytes(img2base64('./test/1.png'), encoding='utf-8'))

    with open('./test/1(re).png', 'wb') as f:
        f.write(base64.b64decode(bytes(img2base64('./test/1.png'), encoding='utf-8')))

test_img2base64()
