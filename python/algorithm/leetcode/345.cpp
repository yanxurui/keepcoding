class Solution {
public:
    string reverseVowels(string s) {
        int i=0, j=s.size()-1;
        char tmp;
        while(1)
        {
            while(i < j && (s[i]=='a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u'))
                i++;
            while(i < j && (s[j]=='a' || s[j] == 'e' || s[j] == 'i' || s[j] == 'o' || s[j] == 'u'))
                j--;
            if(i>j)
                break;
            tmp = s[i];
            s[i] = s[j];
            s[j] = tmp;
            i++;
            j--;
        }
    }
};