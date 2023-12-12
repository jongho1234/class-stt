
from typing import List
from lexrankr import LexRank
import sys
from konlpy.tag import Kkma
from main import name

#name = 'c600289e5db8bb997197'
    # open 구문 포맷
f = open(f"{name}_out.txt", "r")
    ### 파일 읽는 코드 ###
f.close()

    # with open 구문 포맷
with open(f"{name}_out.txt", "r") as f:
    example = f.read()

print(example)
kkma = Kkma()
text = example
text += ' --'



# 형태소 분석
result = kkma.pos(text)
print(result)
indices = [i for i, item in enumerate(result) if item[1].startswith('EF')]
print(indices)
for num in indices :
    position = text.find(f'{result[num][0][1:]} {result[num+1][0]}')
    if position >=  0 :
        text = text[:position+2] + '.' + text[position+2:]

print(text)

class MyTokenizer:
    def __call__(self, text: str) -> List[str]:
        tokens: List[str] = text.split()
        return tokens
your_text = text
    
    
    # 1. init
mytokenizer: MyTokenizer = MyTokenizer()
lexrank: LexRank = LexRank(mytokenizer)

    # 2. summarize (like, pre-computation)
lexrank.summarize(your_text)

    # 3. probe (like, query-time)
summaries: List[str] = lexrank.probe()
with open(f'{name}_text.txt', 'w') as f:
    for summary in summaries:
        f.write('- ' + summary + '\n')
        
sys.stdout.close() #-- 텍스트 저장시 사용


