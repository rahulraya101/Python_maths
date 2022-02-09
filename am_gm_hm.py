import functools
import operator

def means(values):
    # your code here
    am = sum(values)/ len(values)
    p = 1

    # gm = (1.2.3....n)^1/2 
    gm = functools.reduce(operator.mul, values)**(1/len(values))
    #print(gm)
    # 
    #print("Last value of provided array:", values[-1])    
    #for i in values:
    #    p = p * i
    #print("Last p:", p)
    #gm = p ** (1/len(values))
    
    hm = len(values) / sum([1/i for i in values])

    #hm = gm**2/am
    return am, gm, hm
    #for i in values:
        #p = 1/(p * i)
    #hm = len (values)/sum(p)
    #return 1, 2, 3 
data = [20.6, 35.2, 16.2, 28.5, 25.0, 17.6, 8.2, 1.8, 15.3, 7.2]
am, gm, hm = means(data)
print(f"AM = {am}")
print(f"GM = {gm}")
print(f"HM = {hm}")
