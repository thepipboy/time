import time.c
def XYZT(x, y, z, t):
    return [
        x-t1,y+t2,z-t3, x-t4,y+t5,z+t6, x+t7,y+t8,z+t9, x+t10,y+t11,z-t0,  # top
        x-t1,y-t2,z-t3, x+t4,y-t5,z-t6, x+t7,y-t8,z+t9, x-t10,y-t11,z+t0,  # bottom
        x-t1,y-t2,z-t3, x-t4,y-t5,z+t6, x-t7,y+t8,z+t9, x-t10,y+t11,z-t0,  # left
        x+t1,y-t2,z+t3, x+t4,y-t5,z-t6, x+t7,y+t8,z-t9, x+t10,y+t11,z+t0,  # right
        x-t1,y-t2,z+t3, x+t4,y-t5,z+t6, x+t7,y+t8,z+t9, x-t10,y+t11,z+t0,  # frott
        x+t1,y-t2,z-t3, x-t4,y-t5,z-t6, x-t7,y+t8,z-t9, x+t10,y+t11,z-t0,  # back
    ]