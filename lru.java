// implemented using a Dll and a map
class Entry{
	int value;
	int key;
	Entry left;
	Entry right;
	public Entry(int key, int value, Entry left, Entry right){
		this.value = value;
		this.key = key;
		this.left = left;
		this.right = right;
	}
}
public class LRUCache{
	HashMap<Integer, Entry> map;
	Entry start, end;
	int LRU_size;

	public LRUCache(int size){
		LRU_size=size;
		map = new HashMap();
	}

	public void updateOrAddEntry(int key, int value){
		if(map.containskey(key)){
			Entry entry = map.get(key);
			entry.value = value;
			removeNode(entry);
			addAtTop(entry);
		}
		else{
			Entry newNode = new Entry(key, value, null, null);
			if (map.size() > LRU_size){
				map.remove(end.key);
				removeNode(end);
				addAtTop(newNode);
			}
			else{
				addAtTop(newNode);
			}
			map.put(key, newNode);
		}
	}

	public int getEntry(int key){
		if (map.containskey(key)){
			Entry entry = map.get(key);
			removeNode(entry);
			addAtTop(entry);
			return entry.value;
		}
		return -1;
	}

	public void removeNode(Entry node){
		if (node.left != null) node.left.right = node.right;
		else start = node.right;
		if(node.right != null) node.right.left = node.left;
		else end = node.left;
	}

	public void addAtTop(Entry node){
		node.right = start;
		node.left = null;
		if (start != null ) start.left = node;
		start = node;
		if (end == null ) end = start;
	}

}