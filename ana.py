    def anagrams(self, strs):
        ret=set()
        for i in range(0,len(strs)):
            for j in range(i+1,len(strs)):
                if i in ret and j in ret:
                    continue
                if Solution.isanagram(strs[i],strs[j]):
                    ret.add(i)
                    ret.add(j)
        return [strs[i] for i in list(ret)]
    def isanagram(s, t):
        if len(s)!=len(t):
            return False
        chars={}
        for i in s:
            if i in chars:
                chars[i]+=1
            else:
                chars[i]=1
        for i in t:
            if i not in chars:
                return False
            else:
                chars[i]-=1
                if chars[i]<0:
                    return False
        for i in chars:
            if chars[i]!=0:
                return False
        return True
