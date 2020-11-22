from collections import deque


def minSubstringWithAllChars(s, t):

    if t == '':
        return ''
    
    ans = s
    target = set(t)
    
    last_pos = {}
    need_pos = deque()
    left_idx = None
    
    for idx, letter in enumerate(s):
        
        if letter in target:
            
            last_pos[letter] = idx
            need_pos.append((idx, letter))
            
            while left_idx is None or left_idx != last_pos[left_letter]:
                left_idx, left_letter = need_pos.popleft()

            if len(last_pos) == len(t) and idx - left_idx + 1 < len(ans):
                    ans = s[left_idx: idx + 1]

    return ans




