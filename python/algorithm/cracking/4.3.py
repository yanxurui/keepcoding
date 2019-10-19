# -*- coding:utf-8 -*-
import math
class MinimalBST:
    def buildMinimalBST(self, vals):
        # write code here
        if len(vals) == 0:
            return 0
        return int(math.log(len(vals), 2))+1
