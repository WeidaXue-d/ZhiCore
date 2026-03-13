import collections

text = "如果你遇到障碍就左转，左转之后如果还有障碍，就继续左转。"
print(f"原始文本: {text}")


tokens = [ord(c) for c in text]
print(f"初始 Tokens (Unicode): {tokens}")

def get_stats(ids):
    """
    统计序列中相邻 Token 对出现的频率
    例如: [1, 2, 1, 2] -> {(1, 2): 2}
    """
    counts = collections.defaultdict(int)
    for pair in zip(ids, ids[1:]):
        counts[pair] += 1
    return counts

def merge(ids, pair, idx):
    """
    将序列中所有出现的 pair 替换为新的索引 idx
    例如: ids=[1, 2, 3, 1, 2], pair=(1, 2), idx=500 -> [500, 3, 500]
    """
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




stats = get_stats(tokens)

top_pair = max(stats, key=stats.get)
print(f"\n最高频相邻组合: {top_pair} (即: '{chr(top_pair[0])}{chr(top_pair[1])}')")
print(f"出现次数: {stats[top_pair]}")


new_token_id = 500
new_tokens = merge(tokens, top_pair, new_token_id)

print(f"\n合并后的 Tokens: {new_tokens}")
print(f"压缩效果: 从 {len(tokens)} 个降至 {len(new_tokens)} 个 Token")

result_display = []
for t in new_tokens:
    if t == new_token_id:
        result_display.append(f"[{chr(top_pair[0])}{chr(top_pair[1])}]")
    else:
        result_display.append(chr(t))
print(f"逻辑演示: {''.join(result_display)}")