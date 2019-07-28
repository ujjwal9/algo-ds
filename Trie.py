//Whenever there is a question of word search use trie
class TrieNode:
	def __init__(self):
		self.children = {}
		self.word=None
		self.isWord=False

class Trie:

	def __init__(self, root):
		self.root=TrieNode()

	def insert(word):
		current = root
		for i in xrange(len(word)):
			node=current.children[word[i]]
			if node is None: current.children[word[i]]=TrieNode()
			current=node[word[i]]
		current.isWord=True
		current.word=word

	def find(word):
		current=root
		for i in xrange(len(word)):
			node=current.children[word[i]]==None: return False
			if node is None: return False
			current=node
		return current.isWord

	def find_with_prefix(prefix, i, current=root):
		result=[]
		if i<=len(prefix):
			node = current.children[prefix[i]]
			if node is None: return []
			return find_with_prefix(prefix, i+1, node)
		else:
			for key in current.children:
				result+=find_with_prefix(prefix, i+1, current.children[key]) 
			return result+[current.word]


	def delete(word, current, i):
		if i==len(word):
			if current.isWord:
				current.isWord=False
				return current.children.isEmpty
			return False
		if current.children[word[i]] is False: return False
		shouldDelete=delete(word, current.children[word[i]], i+1)
		if shouldDelete:
			current.children.remove(word[i])
			return current.children.isEmpty()
		return False


========================================================================================
//Print all valid words that are possible using Characters of Array
//Given a continuous stream of strings, maintain strings such that duplicate are eliminated on the fly

//word boggle


