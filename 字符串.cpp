#include<iostream>
#include<string>//使用C++风格需要包含此头文件
using namespace std;


int main()
{

	//C风格字符串

	char str[] = "hello world";
	cout << str << endl;

	//C++风格字符串

	string str1 = "hello world";
	cout << str1 << endl;

	system("pause");
	return 0;
}