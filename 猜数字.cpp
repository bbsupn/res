#include<iostream>
#include<ctime>
using namespace std;

int main()
{
	cout << "欢迎游玩！本游戏为猜数字，取值区间为1-100" << endl;
	cout << "玩家拥有100初始分数，猜的次数越少分数越高，猜错一次扣15分\n赶快和小伙伴们一起试试吧！\n\n" << endl;
	system("pause");
	srand((unsigned int)time(NULL));
	int num = rand() % 100 + 1;
	int val = 0;
	int score = 100;
	int counter = 0;
	cout << "\n系统随机数字已生成！请输入你要猜的数字：" << endl;
	
	
	while (1)
	{
		cin >> val;
		if (val > num)
		{
			cout << "\n猜大了，请重试！\n" << endl;
			score=score - 15;
			counter++;
		}
		if (val < num)
		{
			cout << "\n猜小了，请重试！\n"<< endl;
			score=score - 15;
			counter++;
		}
		if (val == num)
		{
			cout << "\n猜对了！你的最终分数为：" << score << "\n" << "共猜次数：" << counter << endl;
			if (counter > 5)
				cout << "\n猜这么多次....也许这就是为什么抽不出金光吧...\n" << endl;
			if (score < 0)
				cout << "\n怎么还有人负分啊喂！这一届的煤老板就是你了！脸真黑！\n" << endl;
			break;
		}

	}




	cout << "\n游戏结束\n";
	system("pause");
	return 0;
}