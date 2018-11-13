import random as rand

#Variables:

num_pattern  = 300000 #maximum number of images you can store in 4GB assuming each image is 36KB
start_time   = 0 #us

#Accelerator related parameters
accel_freq   = 10**9     #1GHz
accel_ccycle = 10000     #compute cycles

access_pattern = 'constant'    #random - accel_cycle varies in range
accel_tpc      = 1.0/accel_ccycle # Time per cycle

img_numpages   = 1 #imge_pge/stride = 3/3

#SSD Related parameters:

#32 channels, 8 dies, 2 planes, 4K blocks, 256 pages per block and each page size is 4096
#32*8*2*4096*256*4096/(1024*1024*1024)
# this gives 2TB

page_read_time = 16 #in us
ssd_block_start= 0
#ssd_block_end  = 32*8*2*4096*256 #number of pages - 4 M
ssd_block_end  = 4096*256 #number of pages - 4 M
ssd_page_size  = 4096           #in bytes
ssd_numdev     = 1
ssd_mode       = 1 #0 is write, 1 is read
ssd_stride     = 3 #
arbiter_time   = 0.00 #10ns - 10 cycles

ppn_start = ssd_block_start
for i in range(0, num_pattern):
    accel_time = accel_ccycle * accel_tpc
    #print(start_time, '0'),

    start_time = start_time + accel_time

    if access_pattern == 'random':
        ppn_start = rand.randint(ssd_block_start, ssd_block_end)
    else:
        ppn_start = ppn_start + ssd_stride

    for p in range(0, img_numpages):
        start_time = round(start_time + rand.uniform(0.01, 0.04), 3)
        print("%.3f %s %ld %d %d" % (start_time, '0', (ppn_start+p), ssd_stride, ssd_mode))

print("%f %s %ld %d %d" % (start_time + accel_time, 0, 1222321, 1, 1))
