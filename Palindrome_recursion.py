def power_modulo_recursive(A,B,C):
    if B==0:
        return 1%C
    else:
        temp=power_modulo_recursive(A,B,C)
        return (A*temp)%C
A=int(input())
B=int(input())
C=int(input())
result=power_modulo_recursive(A,B,C)
print(result)
