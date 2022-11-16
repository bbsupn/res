#include<iostream>
using namespace std;

int main()
{

	int a1 = 10;
	int b1 = 3;

	cout << a1 + b1 << endl;
	cout << a1 - b1 << endl;
	cout << a1 * b1 << endl;
	cout << a1 / b1 << endl;
	//除数不能是0
	double d1 = 0.5;
	double d2 = 0.22;
	cout << d1 / d2 << endl;//小数可以相除运算，结果也可以是小数

	cout << a1 % b1 << endl;
	//小数不可以做取模运算


	//1.前置递增
	int a = 10;
	++a;
	cout << a << endl;
	//2.后置递增
	int b = 10;
	b++;
	cout << b << endl;
	//3.前置和后置的区别
	//前置递增 先让变量+1 然后进行表达式运算
	int a2 = 10;
	int b2 = ++a2 * 10;
	cout << a2 << endl;
	cout << b2 << endl;
	//后置递增 先进行表达式运算 后让变量+1
	int a3 = 10;
	int b3 = a3++ * 10;
	cout << a3 << endl;
	cout << b3 << endl;




	system("pause");
	return 0;
}