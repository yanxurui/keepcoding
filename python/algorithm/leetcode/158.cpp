/**
 * The read4 API is defined in the parent class Reader4.
 *     int read4(char *buf4);
 */

class Solution {
public:
    /**
     * @param buf Destination buffer
     * @param n   Number of characters to read
     * @return    The number of actual characters read
     */
    int read(char *buf, int n) {
        int i = 0;

        while (i < n)
        {
            if (i4 < n4)
            {
                buf[i++] = buf4[i4++];
            }
            else
            {
                i4 = 0;
                n4 = read4(buf4);
                if (n4 == 0)
                {
                    break;
                }
            }
        }

        return i;
    }

    private: char buf4[4];
    private: int i4 = 0, n4 = 0;
};