

### initialize mpi
import mpi4py.rc
mpi4py.rc.initialize = False
from mpi4py import MPI
MPI.Init()
###



### the actual program

comm = MPI.COMM_WORLD   # the global communicator

rank = comm.Get_rank()  # get process ID withon comm

print("Hello world! this is rank ", rank)

###


### denote end of mpi calls
MPI.Finalize()
###  