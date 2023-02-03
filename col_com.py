import numpy as np
import torch
import array

### initialize mpi.
import mpi4py.rc
mpi4py.rc.initialize = False  
from mpi4py import MPI
MPI.Init()
###



### the actual program.

comm = MPI.COMM_WORLD   # the global communicator.

rank = comm.Get_rank()  # get process ID within comm.


## lowercase version for generic objects, uses pickle under the hood.

if rank == 0:
    mylist = [0,0,0]
else:
    mylist = None                    ## necessary! mylist needs to be known before bcast is called.


mylist = comm.bcast(mylist, root=0)     ## send arr from 0 to all processes.



mylist += [rank]                       

print("This is process {} and my list is \n{}".format(rank, mylist))



## uppercase version for contiguous memory blocks such as arrays. more efficient but less generic.

# if rank == 0:
#     arr = np.zeros((2,3))
# else:
#     arr = np.empty((2,3))     ## this time, arr needs not only be known but also be of correct type and size.

# comm.Bcast(arr, root=0)

# print("This is process {} and my array is \n{}".format(rank, arr))


### end of actual program.


### denote end of mpi calls.
MPI.Finalize()
###  