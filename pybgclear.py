from PIL import Image as img
import numpy as np
import sys

buff = []
result = []
bgmask = []

def main ():

    openimg(sys.argv[1])
    findbg()
    clearbg()
    saveimg(sys.argv[1])
    
def openimg( szimg ):
    global buff
    
    buff=img.open(szimg)
    buff.show()
    
    
def findbg():
    global buff, bgmask
    
    clr_hist = np.zeros([25,25,25])
    buff = buff.convert('RGB')
    imdata = np.array(buff)
    bgmask = np.ones(buff.size)
    
    xlen = buff.size[0]
    ylen = buff.size[1]
    
    samples = []
    samples.append(imdata[0][0])
    samples.append(imdata[ylen-1][xlen-1])
    samples.append(imdata[ylen-1][0])
    samples.append(imdata[0][xlen-1])
    samples.append(imdata[ylen-4][xlen-4])
    samples.append(imdata[ylen-4][0])
    samples.append(imdata[0][xlen-4])    
    samples.append(imdata[4][4])
    
    for i in range(0,ylen):
        for j in range(0,xlen):            
            for sample in samples:
                
                #print(i,j)
                dR      = np.abs(float(sample[0]) -  float(imdata[i][j][0]))
                dG      = np.abs(float(sample[1]) -  float(imdata[i][j][1]))
                dB      = np.abs(float(sample[2]) -  float(imdata[i][j][2]))
                
                clr_R2 =  dR*dR + dG*dG + dB*dB 
                if clr_R2 < 300.0:
                    bgmask[j][i] = 0
                if (dR < 5.0) & (dG < 5.0) & (dB < 5.0):
                    bgmask[j][i] = 0
        


def clearbg():
    global buff, result, bgmask     
    result = np.array(buff.convert('RGBA'))    
    
    xlen = buff.size[0]
    ylen = buff.size[1]
    
    for i in range(0,ylen):
        for j in range(0,xlen):
            if bgmask[j][i] == False:
                result[i][j][3] = 0
                    
    

def saveimg(szimg):
    global buff, result
    outimg = img.fromarray(result)
    szout = szimg.replace('.jpg','') + '_output.png'
    outimg.save(szout)
    
    chk=img.open(szout)
    chk.show()



if __name__ == "__main__":
    main()

