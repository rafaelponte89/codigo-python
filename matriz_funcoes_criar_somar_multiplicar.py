ma = []
mb = []
mr = []


def criar_matriz(l,c,n=0):
    ' Cria matrizes de acordo com dimensões informadas de l = linhas e com c = colunas'
    i = 0
    j = 0
    m = []
    
    while i < l:
        m.append([])
        while j < c:
            n = int(input('MATRIZ {2} X {3}  linha:{0} coluna:{1} '.format(i,j,l,c)))
            m[i].append(n)
            j +=1
            
        i +=1
        j = 0
    print()
    return m


def somar_matriz(ma,mb):
    ' Soma matrizes'
    i = 0
    j = 0
    m = []
    while i < len(ma):
        m.append([])
        while j < len(ma[i]):
            m[i].append(ma[i][j]+mb[i][j])
            j += 1
        i += 1
        j = 0
    return m
            
def multiplicar_matriz(ma,mb):
    ' Multiplicação de matrizes - o numero de linhas da primeira matriz (ma) deve ser igual ao numero de colunas da segunda matriz (mb)'
    la = 0
    ca = 0
    lb = 0
    cb = 0
    i  = 0
    m = []
    resultado = 0
    
    while la < len(ma):
        m.append([]) # cria linha da matriz resultado
        
        while cb < len(mb[0]):
            
            while lb < len(mb):
                resultado += (ma[la][ca] * mb[lb][cb]) 
                ca +=1                                # percorre colunas da matriz ma
                lb +=1                                # percorre linhas da matriz mb
                
            m[i].append(resultado)                    # anexa resultado na linha atual e cria a coluna
            lb = 0                                    # volta ao inicio da linha da matriz mb     
            ca = 0                                    # volta ao inicio da coluna da matriz ma  
            cb += 1                                   # muda a posição para a proxima coluna de mb          
            resultado = 0                               
            
        la += 1                                       # muda a posição para a proxima linha de ma  
        cb = 0                                        # volta ao inicio da coluna da matriz mb  
        i += 1                                        # cria numeração para a proxima linha da matriz resultado
        
    return m    

ma = [[1,5,-2],
      [8,3,0],
      [4,-1,2]]

m2 = [[1,2],
      [3,4]]
def duplicar_colunas(nc=2):
    ' Duplica, triplica ... conforme o número solicitado as "n" primeiras colunas da matriz - da esquerda para a direita '
    l = 0
    c = 0
    
    while l < len(ma):
        while c < nc:
            ma[l].append(ma[l][c])
            c +=1 
        c = 0
        l +=1
    print(ma)
    
def aplicar_regraSarrus(ma):
    
    dp = 0
    ds = 0
    
    duplicar_colunas() 
  
    
    
    # Calcula a diagonal principal da matriz
    
    l = 0
    c = 0
    t = 1
    
    while c < len(ma):
        while l < len(ma):
            t *= ma[l][c] #  acumula o produto da diagonal
            l += 1
            c += 1
            
        if l == len(ma):
            c -=1
       
        dp += t # soma o produto acumulado
        l = 0
        c -= 1
        t = 1
     
    # Calcula a diagonal secundária
    
    c = len(ma[0])-1
    l = 0  
    i = 0
    while i < len(ma) :
        
        while l < len(ma):

            t *= ma[l][c]
            l +=1 
            c-=1
        
        if l == len(ma):
            c = len(ma[0])-1
            i +=1
            c -=  i
        
        ds += t
        l=0
        t = 1
        
            

    print('Diagonal Principal:', dp)
    print('Diagonal Secundária:', ds)
    print('Determinadnte',dp-ds)   
    
    
    

aplicar_regraSarrus(ma)
ra = 2 + \
    3
for i in [1,2,3,4,5]:
    
    print(i)    
print(ra)
#print(somar_matriz(criar_matriz(2,2), criar_matriz(2,2)))
 
    
