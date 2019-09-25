#time for running the code or line

import timeit
s=timeit.timeit('"-".join(str(n) for n in range(100))',number=100000)
print('Time tacken by string:',s)

l=timeit.timeit('"-".join([str(n) for n in range(100)])',number=100000)
print('Time tacken by list :',l)

m=timeit.timeit('"-".join(map(str,range(100)))',number=100000)
print('Time tacken by map :',m)

#same as the built in magic
#%timeit"-".join(str(n) for n in range(100)) Only work in jupiter