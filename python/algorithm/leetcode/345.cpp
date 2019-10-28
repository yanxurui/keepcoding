class Solution {
private:
        bool vowel(char c)
        {
            if (c=='a' || c == 'e' || c == 'i' || c == 'o' || c == 'u')
                return true;
            if (c=='A' || c == 'E' || c == 'I' || c == 'O' || c == 'U')
                return true;
            return false;
        }
public:
    string reverseVowels(string s) {
        int i=0, j=s.size()-1;
        char tmp;
        while(1)
        {
            while(i < j && !vowel(s[i]))
                i++;
            while(i < j && !vowel(s[j]))
                j--;
            if(i>j)
                break;
            tmp = s[i];
            s[i] = s[j];
            s[j] = tmp;
            i++;
            j--;
        }
        return s;

    }
};