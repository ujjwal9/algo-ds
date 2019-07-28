#word problems usually use trie based data structure
#word break problem
def word_break(s, word_dict,n=len(s)):
    pos=[-1]*(n+1)
    pos[0]=0
    for i in xrange(n):
        if pos[i]!=-1:
            for j in xrange(i+1, n):
                if word_dict[s[i:j]] is not None:
                    pos[j]=i
    return pos[n]!=-1

#word wrap. Given a sequence of words, and a limit on the number of characters that can be put in 
#one line (line width). Put line breaks in the given sequence such that the lines are printed neatly.
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
#Transform One String to Another using Minimum Number of Given Operation. BFS
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

#word boggle. Better if done with trie data structure
def dfs(i,j,n,m,matrix,word);
  visited[i][j]=True
  if word in words: result.append(word)
  if i+1<n and visited[i+1][j] is not False: dfs(i+1,j,n,m,matrix,word+matrix[i+1][j])
  if i-1<=0 and visited[i-1][j] is not False: dfs(i-1,j,n,m,matrix,word+matrix[i-1][j])
  if j+1<m and visited[i][j+1] is not False: dfs(i,j+1,n,m,matrix,word+matrix[i][j+1])
  if j-1<=0 and visited[i][j-1] is not False: dfs(i,j-1,n,m,matrix,word+matrix[i][j-1])

n,m=len(matrix),len(matrix[0])
result=[]
for i in xrange(n):
  for j in xrange(m):
    visited=[[False for _ in xrange(m)] for - in xrange(n)]
    dfs(i,j,visited,"") 