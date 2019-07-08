#word problems usually use trie based data structure
#word break problem
public boolean wordBreak(String s, Set<String> wordDict) {
    int[] pos = new int[s.length()+1];
 
    Arrays.fill(pos, -1);
 
    pos[0]=0;
 
    for(int i=0; i<s.length(); i++){
        if(pos[i]!=-1){
            for(int j=i+1; j<=s.length(); j++){
                String sub = s.substring(i, j);
                if(wordDict.contains(sub)){
                    pos[j]=i;
                }
            } 
        }
    }
 
    return pos[s.length()]!=-1;
}

#word wrap
def word_wrap(arr, dp, N, i):
    if i > len(arr): return 0
    minn=0
    for j in xrange(N):
        if dp[i+j]: minn=min(minn, word_wrap(arr,dp,N,i+j+1)+(N-j)^3)
    return minn

dp=[False]*(len(arr))
for i in arr:
    if i+1>len(arr) or arr[i+1]==' ': dp[i]=True
word_wrap(arr,dp,N,0)


#https://leetcode.com/problems/word-ladder/
#word ladder
def one_diff(self,w1,w2):
  c=0
  for i in xrange(len(w1)):
  if w1[i:i+1]!=w2[i:i+1]: c+=1
  if c==1:return True
  else: return False
        
  def ladderLength(self, beginWord, endWord, wordList):
    if endWord not in wordList: return 0
    result=1
    q=[]
    visited=[False]*len(wordList)
    q.append(beginWord)
    while q:
      times=len(q)
      result+=1
      for i in xrange(len(q)):
        w=q.pop(0)
        for i in xrange(len(wordList)):
          if visited[i]==False and one_diff(w,wordList[i]) and w!=wordList[i]:
            if wordList[i]==endWord: return result
              q.append(wordList[i])
              visited[i]=True
    return 0

