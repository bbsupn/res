#include<iostream>
using namespace std;


int main()
{

	int score;
	cout << "请为本次电影打分：[0-10]" << endl;
	cin >> score;
	switch (score)
	{
	case 10:
		cout << "您认为本场电影有10分甚至9分的好看" << endl;
		break;
	case 9:
		cout << "您认为是优秀电影" << endl;
		break;
	case 8:
		cout << "您认为是比较优秀的电影" << endl;
		break;
	case 7:
		cout << "您认为这场电影很不错" << endl;
		break;
	case 6:
		cout << "您认为这场电影还行" << endl;
		break;
	case 5:
		cout << "您认为这场电影一般" << endl;
		break;
	case 4:
		cout << "您认为这场电影勉强说得过去";
		break;
	case 3:
		cout << "您认为这场电影不大好看" << endl;
		break;
	case 2:
		cout << "您看这场电影有点头疼" << endl;
		break;
	case 1:
		cout << "您没有见过比这更烂的片了" << endl;
		break;
	case 0:
		cout << "您认为这堪比催吐" << endl;
		break;

	default:cout << "输入的值不在范围内！用户默认好评" << endl;
		break;
	}
	cout << "\n本次评价完毕，感谢您的参与！\n" << endl;
	system("pause");
	return 0;
}