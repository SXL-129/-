from PIL import Image

codeLib = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'."
count = len(codeLib)


def converb(i_file):
    txt = ''
    imode = list(i_file.getbands())
    print(i_file.size)
    for i in range(0,i_file.size[1]):
        for j in range(0,i_file.size[0]):
            if imode[-1] == 'A':
                r,g,b,a = i_file.getpixel((j,i))
            elif imode[-1] == 'B':
                r,g,b = i_file.getpixel((j,i))
            gray = int(r*0.299+g*0.587+b*0.114)
            txt = txt + codeLib[int(((count-1)*gray)/256)]
            txt = txt + '\n'
    return txt


fp = open("E:\pythonProject\lufei.jpg",'rb')
i_file = Image.open(fp)
# i_file = i_file.resize((int(i_file.size[0]*0.35),int(i_file.size[1]*0.175)))

tmp = open("mp.txt",'w')
tmp.write(converb(i_file))
tmp.close()