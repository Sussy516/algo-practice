class _TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, _TrieNode] = {}
        self.is_end = False


class Trie:
    """Prefix tree supporting insert, exact word search, and prefix queries."""

    def __init__(self) -> None:
        self._root = _TrieNode()

    def insert(self, word: str) -> None:
        node = self._root
        for ch in word:
            node = node.children.setdefault(ch, _TrieNode())
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self._walk(word)
        return node is not None and node.is_end

    def starts_with(self, prefix: str) -> bool:
        return self._walk(prefix) is not None

    def _walk(self, text: str) -> _TrieNode | None:
        node = self._root
        for ch in text:
            node = node.children.get(ch)
            if node is None:
                return None
        return node
