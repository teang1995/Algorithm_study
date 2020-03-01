#include <string>
#include <vector>
#include <iostream>

using namespace std;
void inc_insertion_sort(vector<int>& array, int first, int last, int gap)
{
	int i = 0;
	int j = 0;
	int key = 0;

	for (i = first + gap; i <= last; i = i + gap)
	{
		key = array[i];
		/*
		���� ���ĵ� �迭�� i-gap�����̹Ƿ� i-gap��°���� �������� �����Ѵ�.
		j���� first �̻��̾�� �ϰ�
		key ������ ���ĵ� �迭�� �ִ� ���� ũ�� j��°�� j+gap��°�� �̵��Ѵ�.
		*/
		for (j = i - gap; j >= first && array[j] > key; j = j - gap)
		{
			array[j + gap] = array[j];
		}
		array[j + gap] = key;
	}
}

void shell_sort(vector<int>& array)
{
	int i = 0;
	int gap = 0;
	int n = array.size();
	for (gap = n / 2; gap > 0; gap = gap / 2)
	{
		if ((gap % 2) == 0)
		{
			gap++;
		}
		for (i = 0; i < gap; i++)
		{
			/*��������:0,1,2,3,4....*/
			inc_insertion_sort(array, i, n - 1, gap);
			/*��������:4,3,2,1,0....*/
			//des_insertion_sort(array, i, n - 1, gap);
		}
	}
}

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
	vector<int> answer(commands.size());
	vector<int> temp;
	int i = 0;
	int j = 0;
	int start = 0;	//�����̽� ���� ��ġ
	int end = 0;	//�����̽� ���� ��ġ
	int index = 0;	//��ȯ�� ��
	//command�� ������ŭ for���� �ݺ�
	for (i = 0; i < commands.size(); i++)
	{
		start = commands[i][0];
		end = commands[i][1];
		index = commands[i][2];
		for (j = start - 1; j < end; j++)
		{
			temp.push_back(array[j]);
		}
		shell_sort(temp);
		answer[i] = temp[index - 1];
		temp.clear();
	}
	return answer;
}

int main()
{
	vector<vector<int>> commands = { {2,5,3},{4,4,1},{1,7,3} };
	cout << commands.size();
	return 0;
}