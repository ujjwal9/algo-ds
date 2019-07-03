//Whenever there is a question of word search use trie
class TrieNode{
	HashMap<Character, TrieNode> children = new HashMap<>();
	String content;
	boolean isWord;
}

class Trie{
	private TrieNode root;

	void insert(String word){
		TrieNode current = root;
		for (int i = 0 ; i < word.length() ; i++){
			TrieNode node = current.children.get(word.charAt(i));
			if (node == null)
				node.put(word.charAt(i), new TrieNode())
			current=node;
		}
		current.isWord=true;
	}

	boolean find(String word){
		TrieNode current = root;
		for (int i = 0 ; i < word.length() ; i++){
        	TrieNode node = current.children.get(word.charAt(i));
        	if (node == null) {
            	return false;
        	}
        	current = node;
    	}
    	return current.isEndOfWord();
	}

	boolean delete(String word, TrieNode current, int i){
		if(i==word.length()){
			if(current.isWord==false) return false;
			else{
				current.isWord=false
				return current.children.isEmpty()
			}
		}
		if(current.children.get(word.charAt(i)) == null) return false;
		boolean shouldDeleteCurrentNode = delete(word, current.children.get(word.charAt(i)), i+1);
		if(shouldDeleteCurrentNode){
			current.children.remove(word.charAt(i));
			return current.children.isEmpty();
		}
		return false;
	}
}

//Print all valid words that are possible using Characters of Array
//Given a continuous stream of strings, maintain strings such that duplicate are eliminated on the fly

