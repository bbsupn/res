#include<iostream>
using namespace std;


int main()
{

	//1.字符型
	char ch = 'a';
	cout << ch << endl;

	//所占内存大小
	cout << "char字符型变量所占内存:" << sizeof(char) << endl;

	//char ch2 = "b";   创建字符型变量的时候，要用单引号
	//char ch2 = 'abcdef';创建字符型变量的时候，单引号内只能有一个字符


	//对应ASCII码
	cout << (int)ch << endl;

	system("pause");
	return 0;
}