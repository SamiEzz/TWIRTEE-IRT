#include <stdbool.h>

#ifndef header_h_
#define header_h_

 
typedef struct {
	int m, n;
	double ** v;
} mat_t, *mat;
 
mat matrix_new(int m, int n);
 
void matrix_delete(mat m);
 
void matrix_transpose(mat m);

mat matrix_copy(int n, double a[][n], int m);
 
mat matrix_mul(mat x, mat y);
 
mat matrix_minor(mat x, int d);
 
/* c = a + b * s */
double *vmadd(double a[], double b[], double s, double c[], int n);
 
/* m = I - v v^T */
mat vmul(double v[], int n);
 
/* ||x|| */
double vnorm(double x[], int n);
 
/* y = x / d */
double* vdiv(double x[], double d, double y[], int n);
 
/* take c-th column of m, put in v */
double* mcol(mat m, double *v, int c);
void matrix_show(mat m);
void householder(mat m, mat *R, mat *Q);

void matrix_cofactors(mat m, mat temp, int p, int q, int n);
float matrix_det(mat m, int n);
void matrix_adjoint(mat m, mat adj);
bool matrix_inv(mat m,mat inv);





#endif
