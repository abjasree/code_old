class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_dict = {}
        for i in magazine:
            if i not in magazine_dict.keys():
                magazine_dict[i] = 1
            magazine_dict[i] += 1
            
        note_dict = {}
       
        for j in ransomNote:
            if j not in magazine_dict.keys():
                return False
            if j not in note_dict.keys():
                note_dict[j] = 1
            note_dict[j] += 1
            if note_dict[j] > magazine_dict[j]:
                return False
        return True
            
        