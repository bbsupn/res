#include<iostream>
using namespace std;

int main()
{


	short num1 = 10;
	cout << "short��ռ�ڴ�ռ�:" << sizeof(num1) << endl;

	int num2 = 10;
	cout << "int��ռ�ڴ�ռ�:" << sizeof(num2) << endl;

	long num3 = 10;
	cout << "long��ռ�ڴ�ռ�:" << sizeof(num3) << endl;

	long long num4 = 10;
	cout << "long long ��ռ�ڴ�ռ�:" << sizeof(num4) << endl;

	//short < int <= long <= long long

	system("pause");
	return 0;
}