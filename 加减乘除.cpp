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
	//����������0
	double d1 = 0.5;
	double d2 = 0.22;
	cout << d1 / d2 << endl;//С������������㣬���Ҳ������С��

	cout << a1 % b1 << endl;
	//С����������ȡģ����


	//1.ǰ�õ���
	int a = 10;
	++a;
	cout << a << endl;
	//2.���õ���
	int b = 10;
	b++;
	cout << b << endl;
	//3.ǰ�úͺ��õ�����
	//ǰ�õ��� ���ñ���+1 Ȼ����б��ʽ����
	int a2 = 10;
	int b2 = ++a2 * 10;
	cout << a2 << endl;
	cout << b2 << endl;
	//���õ��� �Ƚ��б��ʽ���� ���ñ���+1
	int a3 = 10;
	int b3 = a3++ * 10;
	cout << a3 << endl;
	cout << b3 << endl;




	system("pause");
	return 0;
}