import heapq
from collections import defaultdict, Counter
from typing import Optional, Dict, Tuple

class Node:
    def __init__(self, char: Optional[str], freq: int):
        self.char = char
        self.freq = freq
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None

    def __lt__(self, other: "Node") -> bool:
        return self.freq < other.freq


def build_huffman_tree(text: str) -> Node:
    frequency = Counter(text)
    heap = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = Node(None, node1.freq+node2.freq)
        merged.left = node1
        merged.right = node2
        heapq.heappush(heap, merged)

    return heap[0]


def generate_codes(root: Optional[Node], prefix: str="", codes: Optional[Dict[str, str]]=None) -> Dict[str, str]:
    if codes is None:
        codes = {}

    if root is None:
        return codes

    if root.char is not None:
        codes[root.char] = prefix

    generate_codes(root.left, prefix+"0", codes)
    generate_codes(root.right, prefix+"1", codes)\

    return codes

def huffman_encoding(text: str) -> Tuple[str, Node]:
    root = build_huffman_tree(text)
    codes = generate_codes(root)
    encoded_text = "".join(codes[char] for char in text)
    return encoded_text, root


def huffman_decoding(encoded_text: str, root:Node) -> str:
    decoded_text = []
    current = root

    for bit in encoded_text:
        current = current.left if bit == "0" else current.right

        if current.char is not None:
            decoded_text.append(current.char)
            current = root

    return  "".join(decoded_text)

text = "hello huffman"
encoded, tree = huffman_encoding(text)
print(f"Encoded: {encoded}")

decoded = huffman_decoding(encoded, tree)
print(f"Decoded: {decoded}")


'''
Time complexity:
Building the tree -> O(n log n)
Encoding/Decoding -> O(m)

Space complexity:
    Heap -> O(n)
    Tree -> O(n)
    Encoded text -> O(m)
'''
