#include<iostream>
using namespace std;

int main()
{

	//1.����
	int a = 0;
	cout << "������ͱ���a��ֵ:" << endl;
	cin >> a;
	cout << "���ͱ���a:" << a << endl;
	//2.������
	float f = 3.14f;
	cout << "��������ͱ���f��ֵ:" << endl;
	cin >> f;
	cout << "�����ͱ���f:" << f << endl;
	//3.�ַ���
	char str = ' ';
	cout << "����ַ��ͱ���str��ֵ:" << endl;
	cin >> str;
	cout << "�ַ��ͱ���str:" << str << endl;
	//4.�ַ�����
	char str1[] = "";
	cout << "����ַ�������str1��ֵ:" << endl;
	cin >> str1;
	cout << "�ַ�������str1:" << str1 << endl;
	//5.bool����  ֻҪ��0������
	bool flag = false;
	cout << "���bool������ֵ:" << endl;
	cin >> flag;
	cout << "bool flag=" << flag << endl;

	system("pause");
	return 0;
}