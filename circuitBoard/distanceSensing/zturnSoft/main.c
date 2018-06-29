#include <stdio.h>
#include <math.h>

#include "matlablite.h"

double in[][3] = {
	{ 12, -51,   4},
	{  6, 167, -68},
	{ -4,  24, -41},
	{ -1, 1, 0},
	{ 2, 0, 3},
};



int main()
{
	mat R, Q;
	mat x = matrix_copy(3, in, 5);
	householder(x, &R, &Q);
 
	puts("Q"); matrix_show(Q);
	puts("R"); matrix_show(R);
 
	// to show their product is the input matrix
	mat m = matrix_mul(Q, R);
	puts("Q * R"); matrix_show(m);
 
	matrix_delete(x);
	matrix_delete(R);
	matrix_delete(Q);
	matrix_delete(m);
	
	return 0;
}