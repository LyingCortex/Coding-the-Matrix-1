# version code 542eddf1f327+
coursera = 1
# Please fill out this stencil and submit using the provided submission script.

from mat import Mat
from vec import Vec



## 1: (Problem 4.17.1) Computing matrix-vector products
# Please represent your solution vectors as lists.
vector_matrix_product_1 = ...
vector_matrix_product_2 = ...
vector_matrix_product_3 = ...



## 2: (Problem 4.17.2) Matrix-vector multiplication to swap entries
# Represent your solution as a list of rowlists.
# For example, the 2x2 identity matrix would be [[1,0],[0,1]].

M_swap_two_vector = ...



## 3: (Problem 4.17.3) [z+x, y, x] Matrix-vector multiplication
three_by_three_matrix = ... # Represent with a list of rowlists.



## 4: (Problem 4.17.4) [2x, 4y, 3z] matrix-vector multiplication
multiplied_matrix = ... # Represent with a list of row lists.



## 5: (Problem 4.17.5) Matrix multiplication: dimension of matrices
# Please enter a boolean representing if the multiplication is valid.
# If it is not valid, please enter None for the dimensions.

part_1_valid = ... # True or False
part_1_number_rows = ... # Integer or None
part_1_number_cols = ... # Integer or None

part_2_valid = ...
part_2_number_rows = ...
part_2_number_cols = ...

part_3_valid = ...
part_3_number_rows = ...
part_3_number_cols = ...

part_4_valid = ...
part_4_number_rows = ...
part_4_number_cols = ...

part_5_valid = ...
part_5_number_rows = ...
part_5_number_cols = ...

part_6_valid = ...
part_6_number_rows = ...
part_6_number_cols = ...

part_7_valid = ...
part_7_number_rows = ...
part_7_number_cols = ...



## 6: (Problem 4.17.6) Matrix-matrix multiplication practice with small matrices
# Please represent your answer as a list of row lists.
# Example: [[1,1],[2,2]]
small_mat_mult_1 = ...
small_mat_mult_2 = ...
small_mat_mult_3 = ...
small_mat_mult_4 = ...
small_mat_mult_5 = ...
small_mat_mult_6 = ...



## 7: (Problem 4.17.7) Matrix-matrix multiplication practice with a permutation matrix
# Please represent your solution as a list of row lists.

part_1_AB = ...
part_1_BA = ...

part_2_AB = ...
part_2_BA = ...

part_3_AB = ...
part_3_BA = ...



## 8: (Problem 4.17.9) Matrix-matrix multiplication practice with very sparse matrices
# Please represent your answer as a list of row lists.

your_answer_a_AB = ...
your_answer_a_BA = ...

your_answer_b_AB = ...
your_answer_b_BA = ...

your_answer_c_AB = ...
your_answer_c_BA = ...

your_answer_d_AB = ...
your_answer_d_BA = ...

your_answer_e_AB = ...
your_answer_e_BA = ...

your_answer_f_AB = ...
your_answer_f_BA = ...



## 9: (Problem 4.17.11) Column-vector and row-vector matrix multiplication
column_row_vector_multiplication1 = Vec({0, 1}, {...})

column_row_vector_multiplication2 = Vec({0, 1, 2}, {...})

column_row_vector_multiplication3 = Vec({0, 1, 2, 3}, {...})

column_row_vector_multiplication4 = Vec({0,1}, {...})

column_row_vector_multiplication5 = Vec({0, 1, 2}, {...})



## 10: (Problem 4.17.13) Linear-combinations matrix-vector multiply
# You are also allowed to use the matutil module
def lin_comb_mat_vec_mult(M, v):
    '''
    Input:
      -M: a matrix
      -v: a vector
    Output: M*v
    The following doctests are not comprehensive; they don't test the
    main question, which is whether the procedure uses the appropriate
    linear-combination definition of matrix-vector multiplication. 
    Examples:
    >>> M=Mat(({'a','b'},{0,1}), {('a',0):7, ('a',1):1, ('b',0):-5, ('b',1):2})
    >>> v=Vec({0,1},{0:4, 1:2})
    >>> lin_comb_mat_vec_mult(M,v) == Vec({'a', 'b'},{'a': 30, 'b': -16})
    True
    >>> M1=Mat(({'a','b'},{0,1}), {('a',0):8, ('a',1):2, ('b',0):-2, ('b',1):1})
    >>> v1=Vec({0,1},{0:4,1:3})
    >>> lin_comb_mat_vec_mult(M1,v1) == Vec({'a', 'b'},{'a': 38, 'b': -5})
    True
    '''
    assert(M.D[1] == v.D)
    pass



## 11: (Problem 4.17.14) Linear-combinations vector-matrix multiply
def lin_comb_vec_mat_mult(v, M):
    '''
    Input:
      -v: a vector
      -M: a matrix
    Output: v*M
    The following doctests are not comprehensive; they don't test the
    main question, which is whether the procedure uses the appropriate
    linear-combination definition of vector-matrix multiplication. 
    Examples:
      >>> M=Mat(({'a','b'},{0,1}), {('a',0):7, ('a',1):1, ('b',0):-5, ('b',1):2})
      >>> v=Vec({'a','b'},{'a':2, 'b':-1})
      >>> lin_comb_vec_mat_mult(v,M) == Vec({0, 1},{0: 19, 1: 0})
      True
      >>> M1=Mat(({'a','b'},{0,1}), {('a',0):8, ('a',1):2, ('b',0):-2, ('b',1):1})
      >>> v1=Vec({'a','b'},{'a':4,'b':3})
      >>> lin_comb_vec_mat_mult(v1,M1) == Vec({0, 1},{0: 26, 1: 11})
      True
    '''
    assert(v.D == M.D[0])
    pass



## 12: (Problem 4.17.15) dot-product matrix-vector multiply
# You are also allowed to use the matutil module
def dot_product_mat_vec_mult(M, v):
    '''
    Return the matrix-vector product M*v.
    The following doctests are not comprehensive; they don't test the
    main question, which is whether the procedure uses the appropriate
    dot-product definition of matrix-vector multiplication. 
    Examples:
    >>> M=Mat(({'a','b'},{0,1}), {('a',0):7, ('a',1):1, ('b',0):-5, ('b',1):2})
    >>> v=Vec({0,1},{0:4, 1:2})
    >>> dot_product_mat_vec_mult(M,v) == Vec({'a', 'b'},{'a': 30, 'b': -16})
    True
    >>> M1=Mat(({'a','b'},{0,1}), {('a',0):8, ('a',1):2, ('b',0):-2, ('b',1):1})
    >>> v1=Vec({0,1},{0:4,1:3})
    >>> dot_product_mat_vec_mult(M1,v1) == Vec({'a', 'b'},{'a': 38, 'b': -5})
    True
    '''
    assert(M.D[1] == v.D)
    pass



## 13: (Problem 4.17.16) Dot-product vector-matrix multiply
# You are also allowed to use the matutil module
def dot_product_vec_mat_mult(v, M):
    '''
    The following doctests are not comprehensive; they don't test the
    main question, which is whether the procedure uses the appropriate
    dot-product definition of vector-matrix multiplication. 
    Examples:
      >>> M=Mat(({'a','b'},{0,1}), {('a',0):7, ('a',1):1, ('b',0):-5, ('b',1):2})
      >>> v=Vec({'a','b'},{'a':2, 'b':-1})
      >>> dot_product_vec_mat_mult(v,M) == Vec({0, 1},{0: 19, 1: 0})
      True
      >>> M1=Mat(({'a','b'},{0,1}), {('a',0):8, ('a',1):2, ('b',0):-2, ('b',1):1})
      >>> v1=Vec({'a','b'},{'a':4,'b':3})
      >>> dot_product_vec_mat_mult(v1,M1) == Vec({0, 1},{0: 26, 1: 11})
      True
      '''
    assert(v.D == M.D[0])
    pass



## 14: (Problem 4.17.17) Matrix-vector matrix-matrix multiply
# You are also allowed to use the matutil module
def Mv_mat_mat_mult(A, B):
    assert A.D[1] == B.D[0]
    pass



## 15: (Problem 4.17.18) Vector-matrix matrix-matrix multiply
def vM_mat_mat_mult(A, B):
    assert A.D[1] == B.D[0]
    pass



## 16: () Buttons
from solver import solve
from GF2 import one

def D(n): return {(i,j) for i in range(n) for j in range(n)}

def button_vectors(n):
  return {(i,j):Vec(D(n),dict([((x,j),one) for x in range(max(i-1,0), min(i+2,n))]
                           +[((i,y),one) for y in range(max(j-1,0), min(j+2,n))]))
                           for (i,j) in D(n)}

# Remind yourself of the types of the arguments to solve().

## PART 1

b1=Vec(D(9),{(7, 8):one,(7, 7):one,(6, 2):one,(3, 7):one,(2, 5):one,(8, 5):one,(1, 2):one,(7, 2):one,(6, 3):one,(0, 4):one,(2, 2):one,(5, 0):one,(6, 4):one,(0, 0):one,(5, 4):one,(1, 4):one,(8, 7):one,(0, 8):one,(6, 5):one,(2, 7):one,(8, 3):one,(7, 0):one,(4, 6):one,(6, 8):one,(0, 6):one,(1, 8):one,(7, 4):one,(2, 4):one})


#Solution given by solver.
x1 = ...

#residual
r1 = ...

#Is x1 really a solution? Assign True if yes, False if no.
is_good1 = ...

## PART 2

b2=Vec(D(9), {(3,4):one, (6,7):one})

#Solution given by solver
x2 = ...

#residual
r2 = ...

#Is it really a solution? Assign True if yes, False if no.
is_good2 = ...




## 17: (Problem 4.17.21) Solving 2x2 linear systems and finding matrix inverse
solving_systems_x1 = ...
solving_systems_x2 = ...
solving_systems_y1 = ...
solving_systems_y2 = ...
solving_systems_m = Mat(({0, 1}, {0, 1}), {...})
solving_systems_a = Mat(({0, 1}, {0, 1}), {...})
solving_systems_a_times_m = Mat(({0, 1}, {0, 1}), {...})
solving_systems_m_times_a = Mat(({0, 1}, {0, 1}), {...})



## 18: (Problem 4.17.22) Matrix inverse criterion
# Please write your solutions as booleans (True or False)

are_inverses1 = ...
are_inverses2 = ...
are_inverses3 = ...
are_inverses4 = ...

