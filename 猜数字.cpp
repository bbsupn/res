#include<iostream>
#include<ctime>
using namespace std;

int main()
{
	cout << "��ӭ���棡����ϷΪ�����֣�ȡֵ����Ϊ1-100" << endl;
	cout << "���ӵ��100��ʼ�������µĴ���Խ�ٷ���Խ�ߣ��´�һ�ο�15��\n�Ͽ��С�����һ�����԰ɣ�\n\n" << endl;
	system("pause");
	srand((unsigned int)time(NULL));
	int num = rand() % 100 + 1;
	int val = 0;
	int score = 100;
	int counter = 0;
	cout << "\nϵͳ������������ɣ���������Ҫ�µ����֣�" << endl;
	
	
	while (1)
	{
		cin >> val;
		if (val > num)
		{
			cout << "\n�´��ˣ������ԣ�\n" << endl;
			score=score - 15;
			counter++;
		}
		if (val < num)
		{
			cout << "\n��С�ˣ������ԣ�\n"<< endl;
			score=score - 15;
			counter++;
		}
		if (val == num)
		{
			cout << "\n�¶��ˣ�������շ���Ϊ��" << score << "\n" << "���´�����" << counter << endl;
			if (counter > 5)
				cout << "\n����ô���....Ҳ�������Ϊʲô�鲻������...\n" << endl;
			if (score < 0)
				cout << "\n��ô�����˸��ְ�ι����һ���ú�ϰ�������ˣ�����ڣ�\n" << endl;
			break;
		}

	}




	cout << "\n��Ϸ����\n";
	system("pause");
	return 0;
}