//����
//���α׷����� �� �� ���� �߿��� �� �� �ϳ��� ��ȣ�� ������ ���ߴ� ���̴�.
//��, ���� ��ȣ�� ������ �׻� �ݴ� ��ȣ�� �ְ�, �ݴ� ��ȣ�� ������ ���� ��ȣ�� �־�� �Ѵ�.
//�ùٸ� ��ȣ�� Ȯ���ϱ� ���� ���� �⺻���� ��� �� �ϳ��� ���� ��ȣ�� �ݴ� ��ȣ�� ������ ���� ���̴�.
//�Ұ�ȣ�� �̷���� ���ڿ��� �־����� ��ȣ�� ������ ����ϴ� ���α׷��� �ۼ��Ͻÿ�.
#include<iostream>
#include<string>
using namespace std;

int main() {
	//1.���� ����
	string strg;
	int startBracket = 0;
	int endBracket = 0;

	//2. ()���ڿ� �Է�
	cout << "()�� �� ���ڿ��� �Է��ϼ���";
	getline(cin, strg);

	//3.���ڿ� �ɰ���
	for (int i = 0; i < strg.size(); i++) {
		if (strg[i] == '(')
			startBracket++;
		else if (strg[i] == ')')
			endBracket++;
	}
	//4.���
	cout << "( ������" << startBracket << "�� �Դϴ�." << endl;
	cout << ") ������" << endBracket << "�� �Դϴ�." << endl;

	return 0;
}