#include <iostream>
#include <set>

using namespace std;


// very slow, ~3s
class Queens {
public:
    int nQueens(int n) {
        // write code here
        int rst = 0;
        set<int> cols = set<int>();
        set<int> xy_diff = set<int>();
        set<int> xy_sum = set<int>();
        dfs(n, cols, xy_diff, xy_sum, rst);
        return rst;
    }
private:
    void dfs(int n, set<int> &cols, set<int> &xy_diff, set<int> &xy_sum, int & rst)
    {
        int x = cols.size();
        if(x==n)
        {
            ++rst;
        }
        else
        {
            for (int y=0;y<n;++y)
            {
                if(cols.find(y)==cols.end() && xy_diff.find(x-y)==xy_diff.end() && xy_sum.find(x+y)==xy_sum.end())
                {
                    cols.insert(y);
                    xy_diff.insert(x-y);
                    xy_sum.insert(x+y);
                    dfs(n, cols, xy_diff, xy_sum, rst);
                    cols.erase(y);
                    xy_diff.erase(x-y);
                    xy_sum.erase(x+y);
                }
            }
        }
    }
};


// very fast, ~0.3s
class Queens2 {
public:
    int nQueens(int n) {
        // write code here
        int count=0;
        int *a=new int[n+1];
        Queens1(a,1,n,count);
        return count;
         
    }
    void Queens1(int a[],int i,int n,int &count){
        if(i>n){
            count++;
            return ;
        }
        for(int j=1;j<=n;j++){
            a[i]=j;
            if(Place(a,i))
                Queens1(a,i+1,n,count);
        }
    }
    bool Place(int *a,int i){
        for(int j=1;j<i;j++)
            if((a[j]==a[i])||(a[j]-a[i]==(j-i))||(a[j]-a[i]==i-j))
            return 0;
       return 1;
    }
};

int main()
{
    int n;
    cin >> n;
    Queens2 Q = Queens2();
    cout << Q.nQueens(n) << endl;
    return 0;
}
