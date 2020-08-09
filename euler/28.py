def sum_diagonals(N):
    m = (N-1)//2
    return 1+ 8*m*(m+1)*(2*m+1)//3 + 2*m*(m+1)+4*m


print(sum_diagonals(1001))
