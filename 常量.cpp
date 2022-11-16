#include<iostream>
using namespace std;


#define Day 7

int main()
{

	/*
	常量的定义方式
	1.#define 宏常量
	2.const修饰的变量
	*/

	cout << "一周总共有:" << Day << "天" << endl;

	const int b = 12;
	//b=24; 错误，const修饰的变量也是常量

	cout << "一年总共有：" << b << "个月份" << endl;

	system("pause");

	return 0;
}