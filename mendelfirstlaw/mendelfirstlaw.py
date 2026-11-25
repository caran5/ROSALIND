p = 0 
def mendelFirstLaw(k, m, n):
    pop = k + m + n
    p = prob = (4*(k*(k-1)+2*k*m+2*k*n+m*n)+3*m*(m-1))/(4*pop*(pop-1))
    print(p)
