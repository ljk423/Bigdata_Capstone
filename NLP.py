apple-> NameError: name 'apple' is not defined
"apple" -> 'apple' "apple's" -> "apple's"
변수명 첫문자로 숫자 안됨 ex) 2x = 1 -> SyntaxError: invalid syntax
.capitalize() -> 첫단어 첫글자만 대문자 .title() -> 모든단어의 첫글자 대문자
s.count(찾을거) -> 빈도수, s.find(찾을거,인덱스) -> 특정 인덱스위치부터 검색 인덱스 없으면 앞부터
s.find() 검색 문자열 없으면 -1 출력 rfind -> 뒤에서 부터 검색 (인덱스는 같음)
s.index() : find와 비슷하게 동작하지만 없을경우 ValueError: substring not found
s.strip() : 좌우 공백문자 제거 rstrip lstrip 각각 오 왼

u = '\t spam\n and ham      '
u
# '\t spam\n and ham      '
print(u)
	 # spam
 # and ham

s.replace(a, b) a를 b로 바꿔줌

s.split() 좌,우, 사이 공백문자 제거후 리스트로 분리!!!
# u = '\n\t     spam    and ham     \n'
print(u)
	     # spam    and ham
u.split()
# ['spam', 'and', 'ham']
type(u.split())
# <class 'list'>
s.split(a) : a를 기준으로 분리

u.split(' ')
# ['\n\t', '', '', '', '', 'spam', '', '', '', 'and', 'ham', '', '', '', '', '\n']

u.split('and')
# ['\n\t     spam    ', ' ham     \n']

'aaabca'.split('a')
# ['', '', '', 'bc', '']

":".join(z)
# 'spam:and:ham'

print("\n".join(z))
# spam
# and
# ham

x = [1,2,3,4,5]
x
# [1, 2, 3, 4, 5]
y = ["언어", "컴퓨터", "python"] #쌍따옴표로 넣어도
y
# ['언어', '컴퓨터', 'python'] #출력은 홑따옴표
x+y
# [1, 2, 3, 4, 5, '언어', '컴퓨터', 'python']

인덱스 에러 -> IndexError: list index out of range
리스트에서 인덱스 값을 가지고 접근하면 값만 출력 되지만 b[1:] 이런식으로 슬라이싱으로 접근하면 [200] 같이 리스트로 출력됨

a = 'abcdef'
a[-1:]
# 'f'
a[:-1]
# 'abcde'
a[::-1]
# 'fedcba'

extend는 ()안에 튜플, 리스트, 사전 중 어떤것이 들어와도 값이 extend되지만
예를 들어 s.append({1,2}) 하면 [1,2,3,{1,2}] 이렇게 들어오게 된다.

#리스트 메쏘드는 연결해서 쭉 쓸 수가 없음
s.append의 결과가 리스트가 아니라 s가 바뀌는 것이기 때문임
s = s.append(4)
이렇게 하고 s를 출력하면 s는 아무것도 출력이 안됨
s에는 None이라는 값이 저장됨 (id 는 할당 됨)
리스트는 index 만 가능하고 find 불가능 

파이썬3에서는 정수/정수 = 실수 나옴

a = ['a', 'c', 'b', 'd', 'b', 'a']
a
# ['a', 'c', 'b', 'd', 'b', 'a']
set(a) # 중복제거됨
# {'d', 'c', 'b', 'a'}
sorted(set(a)) # 셋은 순서 없기 때문에 정렬하면 리스트로 바뀜
# ['a', 'b', 'c', 'd']

def add(a, b):
    return a+b
add{1,2}
  File "<input>", line 1
    add{1,2}
       ^
SyntaxError: invalid syntax
add(1,2)
3
add[1,2]
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: 'function' object is not subscriptable

{1,2} + {2,3}
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'set' and 'set' 집합(사전) + 다른거 도 안됨

from nltk.book import*
type(text1) -> <class 'nltk.text.Text'>

text1.concordance('the') -> 'the'를 포함하는 문자열 검색 앞의 25개를 출력해줌
text1.concordance('the', width = 20, lines = 5) #찾는게 홀수면 the를 예로들때 8 + 3 + 8 해서 19개 출력
type(text1.concordance('the', width=20, lines=5)) -> <class 'NoneType'>

text1.common_contexts(['monstrous', 'doleful', 'careful']) -> most_and

text1.similar('monstrous') common_contexts 기준으로 한 유의어 추

text4.dispersion_plot(['citizens', 'democracy', 'freedom', 'duties', 'America'])

len(text3) -> 토큰
len(set(text3)) - > 타입
len(set(text3)) / len(text3) : 타입-토큰 비율 (lexical_diversity)
round(a,b) a를 소수점 b자리까지 반올림

text3.count('smote') -> 절대빈도
100 * (text3.count('smote') / len(text3)) -> 상대빈도

fdist1 = FreqDist(text1)
# FreqDist({',': 18713, 'the': 13721, '.': 6862, ....
type(fdist1)
# <class 'nltk.probability.FreqDist'>
-> collections 모듈의 collections.Counter()함수와 동일함 이건 타입이 <class ‘collections.Counter’> 임
FreqDist의 내부구조는 딕셔너리와 같아서 몇몇 사전에 사용되는 것들이 적용 가능함

fdist1.most_common(20)
# [(',', 18713), ('the', 13721), ('.', 6862), ('of', 6536)....
출력 데이터 구조는 리스트. 원소는 어휘와 데이터 쌍인 튜플

V = set(text1) # 타입들만 모음(중복제거)
long_words = [w for w in V if len(w) > 15] : text1에 등장하는 단어들 중 중복을 제거한 V 중 길이가 15 보다 큰것
type(long_words) -> <class 'list'>

fdist5 = FreqDist(text5)
len(fdist5) #타입개수
# 6066
sorted(w for w in set(text5) if len(w)> 7 and fdist5[w] > 7) : 단어 길이가 7 보다크고 빈도가 7 보다 큰 것
# ['#14-19teens', '#talkcity_adults', '((((((((((', '........', 'Question', 'actually', 'anything', 'computer', 'cute.-ass', 'everyone', 'football', 'innocent', 'listening', 'remember', 'seriously', 'something', 'together', 'tomorrow', 'watching']

x는 리스트
sum(x,x) -> TypeError: can only concatenate list(not 'int')to lis
sum(1) or sum(1,2) -> TypeError: 'int' object is not iterable
sum('python') -> TypeError: unsupported operand type(s) for +: 'int' and 'str'

range()의 타입은 range

# 정규표현식 ##

re.match('1', '1234') -> <re.Match object; span=(0, 1), match='1'> # 여기서 span은 일치하는 문자의 슬라이싱 범위를 뜻함
# 일치하는 것이 없으면 출력하지 않음
re.match('[2-9]','1234') -> 출력없음 (매치는 앞에서부터)
re.match('[0-9]','1234') -> 출력없음 (매치는 앞에서부터)
# <re.Match object; span=(0, 1), match='1'>
re.match('[1-9]','1234')
# <re.Match object; span=(0, 1), match='1'>
type(re.match('1','1234'))
# <class 're.Match'>

re.match('12','1234').group() -> '12'
type(re.match('[0-9]','1234').group()) -> '1'
# <class 'str'>

re.match('.','1234').group() -> '1' : 두번째 논항에 . 들어가면 문자열 .임 즉 첫번째 논항에만 정규표현 적용
re.match('0','1234').group() -> 논타입에 group 메소드 적용한거라 에러뜸. AttributeError: 'NontType' object has no attribute 'group'

# ‘abc\tabc12.’ - ‘어휘경계abc어휘경계\t어휘경계abc12어휘경계.'
re.match('\s+[0-9]+', '\t\n1234\n').group( ) 공백연쇄 뒤에 숫자연쇄
# '\t\n1234'
re.match('\s+\d+', '\t\n1234\n').group( ) 같은거
# '\t\n1234'
re.match('\W+\w+', '\t\n1234\n').group( ) 숫자또는 자연어 외 문자연쇄 뒤에 숫자또는 자연어 연쇄
# '\t\n1234'

# re.search -> 얘는 매치와 다르게 처음부터 일치해도 되고 중간부터 일치해도 됨
re.search('\S+','\t\n1234\n').group() 공백문자외 연쇄 -> '1234'

re.search('.','\t\n1234\n').group()
# '\t'
re.search('(.)','\t\n1234\n').group()
# '\t'
re.search('.','\t\n1234\n').groups() -> 그루핑이 되지 않은 경우에는 출력할 그룹이 없으니까 출력이 안됨
# ()
re.search('(.)','\t\n1234\n').groups()
# ('\t',) -> 튜플은 출력될때 원소가 하나면 뒤에 콤마찍혀서 출력됨!!!
re.search('(ab)(\D+)','\t\n123abc12\nab').groups()
# ('ab', 'c')
re.search('(ab)(\D+)','\t\n123abc12\nab').group() 그루핑하고 group쓰면 무용지물
# 'abc'
re.search('ab\D+','\t\n123abc12\nab').groups() 그루핑 안하고 groups쓰면 안댐, match였으면 에러
# ()

'abc'.split('+')
# ['abc']
'abc'.split(' ')
# ['abc']
'abc'.split('')
Traceback (most recent call last):
  File "<input>", line 1, in <module>
ValueError: empty separator

m = re.search('(\w+)\s+=\s+(\w+)','a = 456')
m.group()
# 'a = 456'
m.group(1) 특정 위치 문자열만 따로 뽑을 수 있음 (학생명 - 성적) 이런식으로 분리할 수 있다는 뜻
# 'a'
m.group(2)
# '456'
m.groups() 그룹 순서에 따라 튜플로 출력
# ('a', '456')

튜플은 x[1]=100 이런식으로 값 대체 안됨. TypeError: 'tuple' object does not support item assignment

findall -> 일치하는 모든것을 리스트로 출력함
re.findall('\d+','123 abc 456 def')
# ['123', '456']
즉 얜 타입 자체가 리스트임 -> 뒤에 .group()못씀 AttributeError: 'list' object has no attribute 'group'

sub -> 앞에 있는 정규표현식의 규칙에 따라 두번째의 주어진 값을 세번째에 적용하여 대치시켜라

re.sub('\w+','ZZ','\t\n1234\n')
# '\t\nZZ\n'
re.sub('\w','ZZ','\t\n1234\n')
# '\t\nZZZZZZZZ\n'

re.sub('\w(\w)\w', 'ZZ', '\t\n1234\n') sub에서는 그룹핑이 별 소용없다
# '\t\nZZ4\n'
re.sub('\w(\w)(\w)\w', 'ZZ', '\t\n1234\n')
# '\t\nZZ\n'
re.sub('\w(\w+)\w', 'ZZ', '\t\n1234\n')
# '\t\nZZ\n'

### Gutenberg corpus ####
import nltk
nltk.corpus.gutenberg.fileids() -> 타입 : 리스트
from nltk.corpus import gutenberg -> 이렇게 호출해도 됨
gutenberg.fileids()

a = gutenberg.raw('austen-emma.txt')
type(a)
# <class 'str'>
>>> a[:40]
# '[Emma by Jane Austen 1816]\n\nVOLUME I\n\nCH'
len(a) -> 공백문자 포함 '문자수'가 되어버림

b = gutenberg.words('austen-emma.txt')
type(b)
# <class 'nltk.corpus.reader.util.StreamBackedCorpusView'>
b
# ['[', 'Emma', 'by', 'Jane', 'Austen', '1816', ']', ...] -> 리스트가 아니라 요약돼서 나옴
type(b[:10]) -> 슬라이싱 하면 리스트로 바뀜
# <class 'list'>

type(b[:]) -> 이건 슬라이싱이지만 다른 자료형으로 바뀜
# <class 'nltk.collections.LazySubsequence'>
b[:]
# ['[', 'Emma', 'by', 'Jane', 'Austen', '1816', ']', ...]
type(b)
# <class 'nltk.corpus.reader.util.StreamBackedCorpusView'>
b
# ['[', 'Emma', 'by', 'Jane', 'Austen', '1816', ']', ...]
type(b[:-1])
# <class 'nltk.collections.LazySubsequence'>
type(b[:10])
#<class 'list'>

c = gutenberg.sents('austen-emma.txt')
c
[['[', 'Emma', 'by', 'Jane', 'Austen', '1816', ']'], ['VOLUME', 'I'], ...]
type(c)
#<class 'nltk.corpus.reader.util.StreamBackedCorpusView'>
c[:4]
[['[', 'Emma', 'by', 'Jane', 'Austen', '1816', ']'], ['VOLUME', 'I'], ['CHAPTER', 'I'], ['Emma', 'Woodhouse', ',', 'handsome', ',', 'clever', ',', 'and', 'rich', ',', 'with', 'a', 'comfortable', 'home', 'and', 'happy', 'disposition', ',', 'seemed', 'to', 'unite', 'some', 'of', 'the', 'best', 'blessings', 'of', 'existence', ';', 'and', 'had', 'lived', 'nearly', 'twenty', '-', 'one', 'years', 'in', 'the', 'world', 'with', 'very', 'little', 'to', 'distress', 'or', 'vex', 'her', '.']]
type(c[:4])
#<class 'list'>
len(c) -> 문장수

for fileid in gutenberg.fileids():
    num_chars = len(gutenberg.raw(fileid))
    num_words = len(gutenberg.words(fileid))
    num_sents = len(gutenberg.sents(fileid))
    num_vocab = len(set(w.lower() for w in gutenberg.words(fileid))) #list에서 주로 사용하는 형태이나 여기서도 set으로 묶어서 사용가능
    print(round(num_chars/num_words), # 평균 어휘길이
            round(num_words/num_sents), # 평균 문장길이
            round(num_words/num_vocab), fileid # 평균 토큰-타입 비율

    aa = re.sub('\W', '', gutenberg.raw('austen-emma.txt')) # 공백문자, 문장부호 제거
    aa = re.sub('\d', '', aa) # 숫자제거
    type(aa)
    #<class 'str'>

bb = [w for w in gutenberg.words('austen-emma.txt') if w.isalpha() == True]

for i in gutenberg.sents('austen-emma.txt'):
    t.append([w for w in i if w.isalpha() == True]) # extend하면 원소 단위로 들어가서 문장단위로 못들어감

t[:4]
#[['Emma', 'by', 'Jane', 'Austen'], ['VOLUME', 'I'], ['CHAPTER', 'I'], ['Emma', 'Woodhouse', 'handsome', 'clever', 'and', 'rich', 'with', 'a', 'comfortable', 'home', 'and', 'happy', 'disposition', 'seemed', 'to', 'unite', 'some', 'of', 'the', 'best', 'blessings', 'of', 'existence', 'and', 'had', 'lived', 'nearly', 'twenty', 'one', 'years', 'in', 'the', 'world', 'with', 'very', 'little', 'to', 'distress', 'or', 'vex', 'her']]

for fileid in gutenberg.fileids():
    chars = re.sub('\W', '', gutenberg.raw(fileid))
    chars = re.sub('\d', '', chars)
    words = [w for w in gutenberg.words(fileid)
        if w.isalpha() == True]
    sents = []
    for i in gutenberg.sents(fileid):
        sents.append([w for w in i if w.isalpha() == True])
    vocab = set(w.lower() for w in gutenberg.words(fileid))
    print(round(len(chars) / len(words), 2), #평균 어휘 길이 : 어휘 난이도
          round(len(words) / len(sents), 2), #평균 문장길이
          round(len(words) / len(vocab), 2), fileid)#토큰-타입 비율 : 얼마나 반복? (어휘 다양성)

chars = re.sub('\W', '', gutenberg.raw())
chars = re.sub('\d', '', chars)
len(chars) # 코퍼스 전체 문자수
# 8927255
words = [w for w in gutenberg.words() if w.isalpha() == True]
len(words) # 코퍼스 전체 단어수
# 2135400
sents = []
for i in gutenberg.sents():
    sents.append([w for w in i if w.isalpha() == True])

len(sents) # 코퍼스 전체 문장수
# 98552

a = nltk.Text(gutenberg.words('austen-emma.txt'))
a
# <Text: Emma by Jane Austen 1816>
type(a)
# <class 'nltk.text.Text'>
a.concordance('surprize') #최대 25개만 출력되고 변수에 저장 불가하다 -> 해결법?

#검색어포함 문장추출
a = nltk.Text(gutenberg.sents('austen-emma.txt'))
type(a)
# <class 'nltk.text.Text'>
b = [''.join(i) for i in a for j in i if j.lower() == 'surprize']
# 전체 문장단위 a 에서 각 문장 i를 받아와 어휘단위 j로 쪼개서 surprize가 있으면 띄어쓰기로 조인해라
# (a가 문장단위로 쪼개져있긴 하지만 리스트 내에서 단어단위로 구분되어있기 때문)
len(b)
# 37

### 코퍼스 ####
from nltk.corpus import brown
brown.categories() # -> 리스트타입
brown.words(categories='news') # -> <class 'nltk.corpus.reader.util.ConcatenatedCorpusView'>
brown.words(categories=['news', 'editorial']) #타입 똑같음 이건 특정파일에서 불러

words = brown.words(categories=['news', 'editorial'])
type(words)
# <class 'nltk.corpus.reader.util.ConcatenatedCorpusView'>
Freq = nltk.FreqDist(w.lower() for w in words)
Freq
# FreqDist(
# {'the': 10347, ',': 7954, '.': 6511, 'of': 4854, 'to': 3727, 'and': 3543, 'a': 3293, 'in': 3111, 'for': 1510,
# 'is': 1485, ...})
type(Freq)
# <class 'nltk.probability.FreqDist'>
modals=['can','could','may','might','must','will']
for i in modals:
    print(i + ':', Freq[i])

cfd = nltk.ConditionalFreqDist((genre, word) #condition역할을 하는 변수, conditon별 어
            for genre in brown.categories()
            for word in brown.words(categories=genre))
type(cfd)
# <class 'nltk.probability.ConditionalFreqDist'>
genres = ['news', 'religion', 'hobbies']
modals = ['can', 'could', 'may', 'might']
cfd.tabulate(conditions=genres, samples=modals)

from nltk.corpus import inaugural
type(inaugural)
# <class 'nltk.corpus.util.LazyCorpusLoader'>
type(inaugural.fileids()) -> 리스트 fileids s붙음

cfd = nltk.ConditionalFreqDist( (target, fileid[:4])
          for fileid in inaugural.fileids()
          for w in inaugural.words(fileid)
          for target in ['america', 'citizen']
          if w.lower().startswith(target))
type(cfd)
# <class 'nltk.probability.ConditionalFreqDist'>

inaugural.words(inaugural.fileids()[:1])
# ['Fellow', '-', 'Citizens', 'of', 'the', 'Senate', ...]
type(inaugural.words(inaugural.fileids()[:1]))
# <class 'nltk.corpus.reader.util.StreamBackedCorpusView'>

wordlist = PlaintextCorpusReader(path,'.*') -> 모든문자 0회또는 1회이상 반복
wordlist
# <PlaintextCorpusReader in '/Users/leejunki/Desktop/19년 1학기/정보처리와자연언어처리/05_test'>
type(wordlist)
# <class 'nltk.corpus.reader.plaintext.PlaintextCorpusReader'>
wordlist = PlaintextCorpusReader(path,'^h')
wordlist.fileids()
# []
wordlist = PlaintextCorpusReader(path,'^h+')
wordlist.fileids()
# []
wordlist = PlaintextCorpusReader(path,'^h.+')
wordlist.fileids()
# ['hu01.txt', 'hu02.txt', 'hu03.txt', 'hu04.txt']

from nltk.corpus.reader.plaintext import CategorizedPlaintextCorpusReader
my = CategorizedPlaintextCorpusReader(path,'.*',cat_pattern='^(\w\w).+') #3번째 논항 중요
type(my)
# <class 'nltk.corpus.reader.plaintext.CategorizedPlaintextCorpusReader'>
my.categories()
# ['hu', 'na']
len(my.words(categories='hu'))
# 9549

from nltk.corpus import stopwords
def content(text):
    stopwords = nltk.corpus.stopwords.words('english')
    content = [w for w in text if w.lower() not in stopwords]
    return(len(content)/len(text)) # stopwords를 제외한 content word의 비율을 산출

type(stopwords.words('english'))
# <class 'list'>

# contentword의 비율이 높다는건 난이도가 높다는 뜻
round(content(my.words(categories = 'hu')),3)
# 0.594
round(content(my.words(categories = 'na')),3)
# 0.597 -> 자연과학은 복합명사를 이어붙이기 때문에 content워드의 비율이 높음
names = nltk.corpus.names
names.fileids()
# ['female.txt', 'male.txt']
type(names)
# <class 'nltk.corpus.reader.wordlist.WordListCorpusReader'>
male_names = names.words('male.txt')
type(male_names)
# <class 'list'> # gutenberg의 type은 <class 'nltk.corpus.reader.util.StreamBackedCorpusView'>임
female_names = names.words('female.txt')
[w for w in male_names if w in female_names][:5] #남녀 공통으로 사용하는 이름
# ['Abbey', 'Abbie', 'Abby', 'Addie', 'Adrian']
cfd = nltk.ConditionalFreqDist( (fileid, name[-1]) # 이름의 끝나는 단어
        for fileid in names.fileids() # male.txt, female.txt를 하나씩 가져와
        for name in names.words(fileid)) # 거기서 이름 추출해서 하나씩

##### wordnet #####

wn.synsets('motorcar') # 복수의 개수이므로 synsets!
# [Synset('car.n.01')]
type(wn.synsets('motorcar'))
# <class 'list'>
type(wn.synsets('motorcar')[0])
# <class 'nltk.corpus.reader.wordnet.Synset'>
wn.synsets('motorcar')[0]
# Synset('car.n.01')
wn.synset('car.n.01').lemma_names() # 하나의 의미를 골라내므로 synset 단수형
['car', 'auto', 'automobile', 'machine', 'motorcar']
type(wn.synset('car.n.01').lemma_names())
# <class 'list'>
wn.synset('car.n.01').definition()
# 'a motor vehicle with four wheels; usually propelled by an internal combustion engine'
type(wn.synset('car.n.01').definition())
# <class 'str'>
for synset in wn.synsets('car'):
    print(synset.lemma_names())
#
# ['car', 'auto', 'automobile', 'machine', 'motorcar']
# ['car', 'railcar', 'railway_car', 'railroad_car']
# ['car', 'gondola']
# ['car', 'elevator_car']
# ['cable_car', 'car']

wn.synset('car.n.01').hyponyms() #하위어 엠뷸런스 택시 이런거
wn.synset('car.n.01').hypernyms() # 상위어 motor_vehicle.n.01
wn.synset('body.n.01').part_meronyms() # 부분어 팔 다리 순환계..
wn.synset('tree.n.01').member_holonyms() # 전체어 forest
wn.synset('walk.v.01').entailments() # 전제 step

dog = wn.synset('dog.n.01')
cat = wn.synset('cat.n.01')
dog.path_similarity(cat) #유사도 계산 -> 노드간의 거리. ontology가 아닌 어휘지
# 0.2


a = '''
iii iii
iii iii'''
a
# '\niii iii\n\niii iii'
print(a)
#
# iii iii
#
#
# iii iii

a = {'a' : 1, 'b' : 1, 'c':2}
a
# {'a': 1, 'b': 1, 'c': 2}
a.keys()
# dict_keys(['a', 'b', 'c'])
type(a.keys())
# <class 'dict_keys'>
list(a.keys())
# ['a', 'b', 'c']
a.items()
# dict_items([('a', 1), ('b', 1), ('c', 2)])
a.values()
# dict_values([1, 1, 2])

#prefix r
print(r'c:\nbc\nbc') # \를 문자그대로 사용됨을 알려줌, 문자열 앞에만 붙일 수 잇음
# c:\nbc\nbc