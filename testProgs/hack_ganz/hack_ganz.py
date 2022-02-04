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



# rtsp over tcp, bosch camera 
# ./testRTSPClient rtsp://service:tpain@192.168.202.81/rtsp_tunnel?h26x=4&line=1&inst=1


# Drew's Ganz DVR box
# ./testRTSPClient rtsp://TEST:1234@192.168.203.147/live

# Xulong's Ganz box
# ./testRTSPClient rtsp://TEST:1234@192.168.204.153/live
