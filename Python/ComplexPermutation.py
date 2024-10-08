import cmath
import math
import matplotlib.pyplot as plt
import numpy as np
import itertools



#Check if there are any collisions


#Generate a set of n basis vectors 
#These could be constricted in different ways to different subsets of numbers



basis1 = complex(5,6)
basis2 = complex(2,7)
basis3 = complex(3,9) 
   

basisVectors = [basis1, basis2, basis3]




def generateBasis(size, configuration):

    return size


#def generateModulus(size, config):
    config_dict = {
        1: allOnes(size),
        2: primes(size),
        3: primeFractions(size), 
        4: powersOf2(size),
        5: inversePowersOf2(size)
    }
    
    return size

def generateArgument(size, config):
    return size




def permute(a, b):        
    return a * b.conjugate()

#Dummy set
permutations = []

permutations.append(permute(permute(basis2, basis3), basis1))
permutations.append(permute(basis1, permute(basis2, basis3)))

permutations.append(permute(permute(basis1, basis3), basis2)) # = print(permute(permute(basis1, basis2), basis3))
permutations.append(permute(basis2, permute(basis1, basis3))) # = print(permute(basis3, permute(basis1, basis2)))

# Returns a list of all combinations of of basis vectors
# These will then be composed under some permutation operator that attempts to break their commutativity,
# uniquely mapping each permutation to a unique output point.
permutationList = list(itertools.permutations(basisVectors))




def permuteArray(permutationList):
    complexOutputs = []
    complexValue = complex(1,1)
    #for n in len(permutationList) - 1:       
    

    return []



def hasDuplicates(inputList):
    if(len(set(inputList)) != len(inputList)):
        return True
    else: 
        return False


def plotComplexNumbers(complexArray):
    x = [c.real for c in complexArray]
    y = [c.imag for c in complexArray]


    plt.scatter(x,y, color='blue')
    #plt.xlim((-limit,limit))
    #plt.ylim((-limit,limit))   

    plt.ylabel('Imaginary')
    plt.xlabel('Real')
    plt.show()  


def complex_plane2(z,axis_type=0):
    """Creates complex plane and shows complex numbers as vectors (complexors)
    
    Parameters
    ----------
    z : array of complex values
        array of complex values to be shown
    axis_type : int 
        three types of shapes of complex plane:
        0 : symple
        1 : with grid
        2 : moved axis to middle 
    -----------------------------------
    # Example
    z=[20+10j,15,-10-10j,5+15j]
    complex_plane2(z,2) """

    w=max(np.abs(z))
    fig, ax = plt.subplots()
        
    if axis_type==0: 
        plt.axis("off")
        plt.text(-0.15*w, 0.8*w, "Im", fontsize=14)
        plt.text( 0.8*w,-0.15*w, "Re", fontsize=14)
    elif axis_type==1: 
        plt.axis("on")
        plt.grid()
        plt.text(-0.15*w, 0.8*w, "Im", fontsize=14)
        plt.text( 0.8*w,-0.15*w, "Re", fontsize=14)
    else:
         # Move left y-axis and bottim x-axis to centre, passing through (0,0)
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('center')

        # Eliminate upper and right axes
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')

        # Show ticks in the left and lower axes only
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')

        ax.set_xlabel('                                                 Re []')
        ax.set_ylabel('                                                 Im []')

    plt.xlim(-w,w)
    plt.ylim(-w,w)
    plt.arrow(0, -w, 0, 1.9*w, head_width=w/20, head_length=w/20, fc='k', ec='k');
    plt.arrow(-w, 0, 1.9*w, 0, head_width=w/20, head_length=w/20, fc='k', ec='k');

    for i in range(len(z)):
        fi_a=np.angle(z[i])
        x=z[i].real -abs(w)/20*np.cos(fi_a)
        y=z[i].imag-abs(w)/20*np.sin(fi_a)
        plt.arrow(0, 0, x, y, head_width=w/20, head_length=w/20, fc='b', ec='b');
    plt.show()


        
print("Permutation Set: ", len(permutationList))

complex_plane2(permutations,1)

