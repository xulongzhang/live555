from __future__ import print_function

base_file_path = "ganz."

i = 0
while i <= 48:
    file_name = base_file_path + str(i) + ".h264"
    
    f = open(file_name,'rb')
    n = 0;
    s = f.read(1)
    while s:
        byte = ord(s)
        n = n+1

        print('%02x '%(byte),end='')

        if n == 100:
            break

        s = f.read(1)

    f.close()

    print('')
    i = i + 1
