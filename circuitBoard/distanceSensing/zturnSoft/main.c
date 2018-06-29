#include <stdio.h>
#include <math.h>

#include "matlablite.h"


// x, y, z = 06, 06, 1995
double Bmat[][1] = {2037,5757,1581,-1047,-3510};

double Amat[][3] = { 
	{12, -5, 1},
	{2, -40, 3},
	{-70, 1, 1},
	{89, 69, -1},
	{20, 60, -2},
	
};



int main()
{

	// sizeof(Amat[0])/sizeof(Amat[0][0]) = 3
	// sizeof(Bmat)/sizeof(Bmat[0]) = 5 (nombre d'anchors)
	mat A = matrix_copy(sizeof(Amat[0])/sizeof(Amat[0][0]),Amat,sizeof(Amat)/sizeof(Amat[0]));
	mat B = matrix_copy(1,Bmat,sizeof(Bmat)/sizeof(Bmat[0]));

	int rank=A->n;
	mat R, Q;
	
	householder(A, &R, &Q);
 	puts("Q"); matrix_show(Q);
	puts("R"); matrix_show(R);
 	// to show their product is the input matrix
	mat Rm1=matrix_new(R->n,R->m);
	if(matrix_inv(R,Rm1)==0){
		printf("matrice singuliere, impossible de l'inverser");
	}
	else{
		//mat Rm1=matrix_inv
		mat Qt=Q;
		matrix_transpose(Qt);
		mat x1=matrix_mul(Rm1,Qt);
		mat x=matrix_mul(x1,B);
		puts("X :");matrix_show(x);
	};


 	matrix_delete(A);
	matrix_delete(R);
	matrix_delete(Q);
	
	return 0;
}
