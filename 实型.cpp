#include<iostream>
using namespace std;


int main()
{
	float f1 = 3.14f;

	cout << "f1=" << f1 << endl;

	double d1 = 3.14;
	
	cout << "d1=" << d1 << endl;

	cout << "float��ռ�ڴ�ռ�;" << sizeof(f1) << endl;

	cout << "double��ռ�ڴ�ռ�:" << sizeof(d1) << endl;

	float f2 = 3e2; //3*10^2           3����10��2�η�
	cout << "f2=" << f2 << endl;

	float f3 = 3e-2; //3*0.1^2
	cout << "f3=" << f3 << endl;

	system("pause");
	return 0;
}