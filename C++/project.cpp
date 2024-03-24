#include <iostream>
#include <cmath>
using namespace std;

const double PI= 3.14159265359;

void Transform_Denavit(float alpha, float theta, float d)
{
	float T[4][4]= {
		{0, 0, 0, 0},
		{0, 0, 0, 0},
		{0, 0, 0, 0},
		{0, 0, 0, 0}
	};
	
	T[0][0] = cos(theta);
	T[0][1] = -1*sin(theta);
	T[0][2] = 0;
	T[0][3] = alpha;
	
	T[1][0] = sin(theta)*cos(alpha);
	T[1][1] = cos(theta)*cos(alpha);
	T[1][2] = -1*sin(alpha);
	T[1][3] = -1*sin(alpha)*d;
	
	T[2][0] = sin(theta)*sin(alpha);
	T[2][1] = cos(theta)*sin(alpha);
	T[2][2] = cos(alpha);
	T[2][3] = cos(alpha)*d;
	
	T[3][3] = 1;
	
	
	cout <<"[\n";
	for(int m=0; m<4; m++)
	{
		for(int n=0; n<4; n++)
		{
			cout << " "<<T[m][n] <<"  ";
		}
		cout << endl;
	}
	cout <<"]";
	cout << endl << endl;
}


int main()
{
	int i;
	cout << "enter number of i: "; cin >> i;
	
	float A[i][4];
	float alpha[5], a[5], theta[5], d[5];
	float T[4][4];
	
	for(int m=0; m<i; m++)
	{
		for(int n=0; n<4; n++)
		{
			if(n==0)
			{
				cout << "please enter A["<<m+1<<"]["<<n+1<<"] as alpha("<<m<<"):(pi:3.14, pi/2:1.57) ";
				cin >> A[m][n];
				
				if(A[m][n] == 3.14)
					A[m][n] = PI;
					
				if(A[m][n] == 1.57)
					A[m][n] = PI/2;
					
				alpha[m] = A[m][n];
			}
			
			if(n==1)
			{
				cout << "please enter A["<<m+1<<"]["<<n+1<<"] as a("<<m<<"): ";
				cin >> A[m][n];
				a[m] = A[m][n];
			}
			
			if(n==2)
			{
				cout << "please enter A["<<m+1<<"]["<<n+1<<"] as theta("<<m<<"):(pi:3.14, pi/2:1.57) ";
				cin >> A[m][n];
				
				if(A[m][n] == 3.14)
					A[m][n] = PI;
					
				if(A[m][n] == 1.57)
					A[m][n] = PI/2;
					
				theta[m] = A[m][n];
			}
			
			if(n==3)
			{
				cout << "please enter A["<<m+1<<"]["<<n+1<<"] as d("<<m<<"): ";
				cin >> A[m][n];
				d[m] = A[m][n];
			}
		}
		cout << endl;	
	}	
	
	cout << "Denavit : [" << endl;
	for(int m=0; m<i; m++)
	{
		for(int n=0; n<4; n++)
		{
			cout << " "<<A[m][n] << "  ";
		}
		cout << endl;
	}
	cout <<"]\n\n";
	
	
	cout << "Transform : " << endl;
	for(int k=0; k<i; k++)
	{
		cout <<"("<<k<<","<<k+1<<")[T]: ";
		Transform_Denavit(alpha[k],theta[k],d[k]);
	}
}