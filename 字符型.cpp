#include<iostream>
using namespace std;


int main()
{

	//1.�ַ���
	char ch = 'a';
	cout << ch << endl;

	//��ռ�ڴ��С
	cout << "char�ַ��ͱ�����ռ�ڴ�:" << sizeof(char) << endl;

	//char ch2 = "b";   �����ַ��ͱ�����ʱ��Ҫ�õ�����
	//char ch2 = 'abcdef';�����ַ��ͱ�����ʱ�򣬵�������ֻ����һ���ַ�


	//��ӦASCII��
	cout << (int)ch << endl;

	system("pause");
	return 0;
}