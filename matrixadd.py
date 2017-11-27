import numpy as np

def matrixadd(m1,m2):
    ## arg : m1 as a np.array, m2 as a np.array
    (i_m1,j_m1)=np.shape(m1)
    (i_m2,j_m2)=np.shape(m2)
    m3=np.eye(i_m1,j_m1)
    if (i_m1 != i_m2) or (j_m1 != j_m2):
        print('m1=',m1)
        print('m2=',m2)
        print('Dimension of m1 and m2 is different!')
        return 0;
    else:
        for i in range(i_m1):
            for j in range(j_m1):
                m3[i,j]=m1[i,j]+m2[i,j]
    return m3;
## Randomly generate the test matrix
aaa=np.array( [ np.random.randint(gg) for gg in range(1,26) ])
bbb=np.array( [ np.random.randint(gy) for gy in range(1,26) ])
## Reshape the test matrix
aaa=aaa.reshape(1,25)
bbb=bbb.reshape(25,1)
## by np.array operation
##print(aaa+bbb)

ccc = matrixadd(aaa,bbb)

print(ccc)

                
