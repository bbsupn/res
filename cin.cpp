#include<iostream>
using namespace std;

int main()
{

	//1.整型
	int a = 0;
	cout << "请给整型变量a赋值:" << endl;
	cin >> a;
	cout << "整型变量a:" << a << endl;
	//2.浮点型
	float f = 3.14f;
	cout << "请给浮点型变量f赋值:" << endl;
	cin >> f;
	cout << "浮点型变量f:" << f << endl;
	//3.字符型
	char str = ' ';
	cout << "请给字符型变量str赋值:" << endl;
	cin >> str;
	cout << "字符型变量str:" << str << endl;
	//4.字符串型
	char str1[] = "";
	cout << "请给字符串变量str1赋值:" << endl;
	cin >> str1;
	cout << "字符串变量str1:" << str1 << endl;
	//5.bool类型  只要非0都是真
	bool flag = false;
	cout << "请给bool变量赋值:" << endl;
	cin >> flag;
	cout << "bool flag=" << flag << endl;

	system("pause");
	return 0;
}