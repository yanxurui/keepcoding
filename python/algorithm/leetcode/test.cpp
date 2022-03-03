#include <vector>
#include <iostream>

using namespace std;
int main()
{
	vector<int> map(128,0);
	map[1]++;
	cout << map[0] << endl;
	cout << map[1] << endl;
	return 0;
}