#include<iostream>
using namespace std;


int main()
{

	int a, b, c;
	cout << "这有三只小猪需要称体重比较谁最重，需要你提供一下他们的体重数据：" << endl;
	system("pause");
	cout << "请输入第一只小猪的体重：" << endl;
	cin >> a;
	cout << "请输入第二只小猪的体重：" << endl;
	cin >> b;
	cout << "请输入第三只小猪的体重：" << endl;
	cin >> c;
	
	if (a > b)
		if (a > c)
			cout << "\n结果是：第一只小猪最重\n" << endl;
		else
			cout << "\n结果是：第三只小猪最重\n" << endl;
	else
		if (b > c)
			cout << "\n结果是：第二只小猪最重\n" << endl;
		else
			cout << "\n结果是：第三只小猪最重\n" << endl;



	system("pause");
	return 0;
}