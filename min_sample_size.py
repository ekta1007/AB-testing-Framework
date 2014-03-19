# Ekta Grover, 19-03-2014
#Adapted from the php code here - http://www.abtester.com/calculator/

import math
perform=[[182,35],[180, 45],[189, 28],[188, 61]]
def convert(perform):
    return float(perform[1])/float(perform[0])

""" Z score works on control group vis a vis each target group"""
def zscore (perform,m) : # m is the index of the target group
   z = convert(perform[m])-convert(perform[0]) # Difference in means 
   s =(convert(perform[m])*(1-convert(perform[m])))/perform[m][0]+(convert(perform[0])*(1-convert(perform[0])))/perform[0][0]
   return float(z)/float(math.sqrt(s))
                
def cumnormdist(x) :
    b1 =  0.319381530
    b2 = -0.356563782
    b3 =  1.781477937
    b4 = -1.821255978
    b5 =  1.330274429
    p  =  0.2316419
    c  =  0.39894228
    h=math.exp(-x * x / 2.0)
    if(x >= 0.0) :
        t = 1.0 / ( 1.0 + p * x )
        return (1.0 - c * h * t *( t *( t * ( t * ( t * b5 + b4 ) + b3 ) + b2 ) + b1 ))
    else :
        t = 1.0 / ( 1.0 - p * x );
        return ( c * h * t *( t *( t * ( t * ( t * b5 + b4 ) + b3 ) + b2 ) + b1 ))
   
def ssize(conv):
    a = 3.84145882689 
    bs = [0.0625, 0.0225, 0.0025]
    res=[]
    for b in bs:
        res.append((int) ((1-conv)*a/(b*conv)))
    return res

# Calling the performance benchmarks 
print "%s %s %s %s " %("Conversion Rate","Z-Score".rjust(15),"Confidence".rjust(13),"Sample-Size".rjust(10))
for i in range(0,len(perform)):
   if i ==0 :
      print "%s %s " %((str(convert(perform[i])*100)+str('%')),str(ssize(convert(perform[i]))).rjust(40))
   if i >0:
      print  str(convert(perform[i])*100)+str('%'), zscore(perform,i),str(cumnormdist(zscore(perform,i))*100)+str('%') , ssize(convert(perform[i]))
