#include<iostream>
using namespace std;


int main()
{

	int a, b, c;
	cout << "������ֻС����Ҫ�����رȽ�˭���أ���Ҫ���ṩһ�����ǵ��������ݣ�" << endl;
	system("pause");
	cout << "�������һֻС������أ�" << endl;
	cin >> a;
	cout << "������ڶ�ֻС������أ�" << endl;
	cin >> b;
	cout << "���������ֻС������أ�" << endl;
	cin >> c;
	
	if (a > b)
		if (a > c)
			cout << "\n����ǣ���һֻС������\n" << endl;
		else
			cout << "\n����ǣ�����ֻС������\n" << endl;
	else
		if (b > c)
			cout << "\n����ǣ��ڶ�ֻС������\n" << endl;
		else
			cout << "\n����ǣ�����ֻС������\n" << endl;



	system("pause");
	return 0;
}