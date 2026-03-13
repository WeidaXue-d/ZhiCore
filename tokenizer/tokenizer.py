import collections

class ZhiTokenizer:
    def __init__(self):
        
        self.vocab = {i: bytes([i]) for i in range(256)} 
        
        self.merges = {} 

    def train(self, text, vocab_size):
        """
        简化版训练：输入文本，迭代合并直到达到目标词表大小
        """
        tokens = list(text.encode("utf-8"))
        num_merges = vocab_size - 256
        
        print(f"开始训练 ZhiCore 分词器...")
        for i in range(num_merges):
            stats = self._get_stats(tokens)
            if not stats:
                break
            
            pair = max(stats, key=stats.get)
            idx = 256 + i
            
            self.merges[pair] = idx
            
            self.vocab[idx] = self.vocab[pair[0]] + self.vocab[pair[1]]
           
            tokens = self._merge(tokens, pair, idx)
            print(f"合并第 {i+1} 次: {pair} -> {idx} (词表大小: {len(self.vocab)})")
        
        self.tokens = tokens

    def _get_stats(self, ids):
        counts = collections.defaultdict(int)
        for pair in zip(ids, ids[1:]):
            counts[pair] += 1
        return counts

    def _merge(self, ids, pair, idx):
        newids = []
        i = 0
        while i < len(ids):
            if i < len(ids) - 1 and ids[i] == pair[0] and ids[i+1] == pair[1]:
                newids.append(idx)
                i += 2
            else:
                newids.append(ids[i])
                i += 1
        return newids

    def encode(self, text):
        """将文本转为 ID 序列"""
        tokens = list(text.encode("utf-8"))
        
        for pair, idx in self.merges.items():
            tokens = self._merge(tokens, pair, idx)
        return tokens

    def decode(self, ids):
        """将 ID 序列还原为文本"""
        
        part_bytes = [self.vocab[idx] for idx in ids]
        b = b"".join(part_bytes)
        # errors='replace' 
        return b.decode("utf-8", errors="replace")

# --- 测试运行 ---
if __name__ == "__main__":
    tokenizer = ZhiTokenizer()
    
   
    raw_text = "遇到障碍就左转，左转之后如果还有障碍，就继续左转。"
    tokenizer.train(raw_text, vocab_size=265) # 基础256个 + 9次合并

    print("\n--- 分词测试 ---")
    test_str = "遇到障碍就左转"
    encoded = tokenizer.encode(test_str)
    print(f"输入: {test_str}")
    print(f"编码 (IDs): {encoded}")
    
    decoded = tokenizer.decode(encoded)
    print(f"解码 (恢复): {decoded}")