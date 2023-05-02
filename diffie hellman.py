from random import randint
 
if __name__ == '_main_':
 
    P = 23
    G = 9
    print('The Value of P is :%d'%(P))
    print('The Value of G is :%d'%(G))
    a = 4
    print('The Private Key a for Mr.X is :%d'%(a))
    x = int(pow(G,a,P)) 
    b = 3
    print('The Private Key b for Mr.Y is :%d'%(b))
    y = int(pow(G,b,P)) 
    ka = int(pow(y,a,P))
    kb = int(pow(x,b,P))
     
    print('Secret key for the Mr.X is : %d'%(ka))
    print('Secret Key for the Mr.Y is : %d'%(kb))
