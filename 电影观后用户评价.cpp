#include<iostream>
using namespace std;


int main()
{

	int score;
	cout << "��Ϊ���ε�Ӱ��֣�[0-10]" << endl;
	cin >> score;
	switch (score)
	{
	case 10:
		cout << "����Ϊ������Ӱ��10������9�ֵĺÿ�" << endl;
		break;
	case 9:
		cout << "����Ϊ�������Ӱ" << endl;
		break;
	case 8:
		cout << "����Ϊ�ǱȽ�����ĵ�Ӱ" << endl;
		break;
	case 7:
		cout << "����Ϊ�ⳡ��Ӱ�ܲ���" << endl;
		break;
	case 6:
		cout << "����Ϊ�ⳡ��Ӱ����" << endl;
		break;
	case 5:
		cout << "����Ϊ�ⳡ��Ӱһ��" << endl;
		break;
	case 4:
		cout << "����Ϊ�ⳡ��Ӱ��ǿ˵�ù�ȥ";
		break;
	case 3:
		cout << "����Ϊ�ⳡ��Ӱ����ÿ�" << endl;
		break;
	case 2:
		cout << "�����ⳡ��Ӱ�е�ͷ��" << endl;
		break;
	case 1:
		cout << "��û�м���������õ�Ƭ��" << endl;
		break;
	case 0:
		cout << "����Ϊ�⿰�ȴ���" << endl;
		break;

	default:cout << "�����ֵ���ڷ�Χ�ڣ��û�Ĭ�Ϻ���" << endl;
		break;
	}
	cout << "\n����������ϣ���л���Ĳ��룡\n" << endl;
	system("pause");
	return 0;
}