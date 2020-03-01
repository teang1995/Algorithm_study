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
		현재 정렬된 배열은 i-gap까지이므로 i-gap번째부터 역순으로 조사한다.
		j값은 first 이상이어야 하고
		key 값보다 정렬된 배열에 있는 값이 크면 j번째를 j+gap번째로 이동한다.
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
			/*오름차순:0,1,2,3,4....*/
			inc_insertion_sort(array, i, n - 1, gap);
			/*내림차순:4,3,2,1,0....*/
			//des_insertion_sort(array, i, n - 1, gap);
		}
	}
}

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
	vector<int> answer(commands.size());
	vector<int> temp;
	int i = 0;
	int j = 0;
	int start = 0;	//슬라이싱 시작 위치
	int end = 0;	//슬라이싱 끝날 위치
	int index = 0;	//반환할 값
	//command의 갯수만큼 for문을 반복
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
