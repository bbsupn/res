#include<iostream>
using namespace std;

int main()
{


	short num1 = 10;
	cout << "short所占内存空间:" << sizeof(num1) << endl;

	int num2 = 10;
	cout << "int所占内存空间:" << sizeof(num2) << endl;

	long num3 = 10;
	cout << "long所占内存空间:" << sizeof(num3) << endl;

	long long num4 = 10;
	cout << "long long 所占内存空间:" << sizeof(num4) << endl;

	//short < int <= long <= long long

	system("pause");
	return 0;
}