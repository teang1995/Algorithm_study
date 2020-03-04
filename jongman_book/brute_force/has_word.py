#problem_id : BOGGLE
matrix = [["u", "r", "l", "p", "m"],
          ["x", "p", "r", "e", "t"],
          ["g", "i", "a", "e", "t"],
          ["x", "t", "n", "z", "y"],
          ["x", "o", "q", "r", "s"]]
dirs = [[-1, -1], [-1, 0], [-1, 1],
         [0, -1], [0, 1],
         [1, -1], [1, 0], [1, 1]]
def has_word (y,x,word):

    # 좌표가 범위 밖이라면 False 를 반환한다.
    if y > 4 or y < 0 or x > 4 or x < 0:
        print("좌표")
        return False
    # 단어가 한 글자라면
    elif len(word) == 1:
        print("한 글자" + word)
        # 좌표의 단어와 word 가 같다면 True 를 반환, 다르다면 False 를 반환.
        if matrix[y][x] == word:
            print("여길 왔다고?", y, x, word)
            return True
        else:
            return False
    # 단어가 한 글자가 아니고, 좌표가 범위 밖에 있지 않다면
    else :
        print(y,x,word)
        # 만약 해당 단어의 첫 글자와 좌표의 글자가 다르다면 False 를 반환
        if word[0] != matrix[y][x]:
            return False
        # 같다면
        else:
            for dir in dirs:
                if has_word(y + dir[0], x + dir[1], word[1:]):
                    return True

print(has_word(0,3,"pretty"))



