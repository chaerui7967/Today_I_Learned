
# 제공된 데이터에서 숫자, 특수문자, 공백을 제거하고 소문자로 변환한다.
def makeNormalData(saleKind, saleNumber): # 판매된 물품 코드 문자열 배열, 판매된 물품의 개수
    retData = [] # 숫자, 공백, 특수문자가 제거된 소문자 문자열 배열.

    ################ 여기부터 코딩 (1) -------->
    for i in range(saleNumber):
        newkind = ''
        for k in range(len(saleKind[i])):
            if saleKind[i][k].isalpha():
                newkind += saleKind[i][k].lower()
        retData.append(newkind)
    ################ <------------- 여기까지코딩 (1)

    return retData



# 순서가 바뀐 글자의 순서를 올바른 순서로 바로 잡는다.
def correctLetterOrder(saleKind, saleNumber, products): # 판매된 물품 코드 문자열 배열, 판매된 물품의 개수, 편의점에서 판매하는 물품 코드 배열 (13종 고정)
    retData = [] # 글자의 순서가 올바른 순서로 정돈된 문자열 배열.

    ################ 여기부터 코딩 (2) -------->
    # 13종 제품을 각각 정렬
    tmpList = list(map(sorted, products))
    sortedProducts = list(map(''.join, tmpList))
    # 목록의 각 단어들을 정렬된 단어와 같은지 체크
    count = 0
    for kind in saleKind:
        kind = ''.join(sorted(kind))  # 문자 정렬, sorted시 문자열이 리스트로 바뀌어 정렬
        # 정렬된 단어가 미리 정렬된 sortedProducts의 어느것과 같은지 찾아서 product와 바꿈
        idx = sortedProducts.index(kind)  # 위치확인
        saleKind[count] = products[idx]
        count += 1

    retData = saleKind
    ################ <------------- 여기까지코딩 (2)

    return retData



# 중복된 물품을 제거하고 정렬한다.
def makeDistinctedData(saleKind, saleNumber): # 소문자로만 구성된 물품 코드 문자열 배열, 	판매된 물품의 개수
    retData = [] # 중복이 제거된 문자열 배열

    ################ 여기부터 코딩 (3) -------->
    kindSet = set(saleKind)  # 중복 제거
    retData = list(kindSet)  # 다시 리스트로

    def findMinIndex(arr):
        minIdx = 0
        for i in range(1, len(arr)):
            if (arr[minIdx][1] > arr[i][1]):
                minIdx = i
            elif (arr[minIdx][1] == arr[i][1]):
                if (arr[minIdx][0] > arr[i][0]):
                    minIdx = i
        return minIdx

    newData = []
    for _ in range(len(retData)):
        minPos = findMinIndex(retData)
        newData.append(retData[minPos])
        del (retData[minPos])

    retData = newData
    ################ <------------- 여기까지코딩 (3)

    return retData


# 편의점에서 판매하는 물품의 종류 (13종-고정)
products= ["coffee", "gimbap", "water", "ramen", "kimchi", "rice", "cigarettes", 
		"milk", "popcorn", "chocolate", "paper", "soju", "beer"]

## 전역 변수 선언 부분
saleNumber = 0 # 판매된 물품의 개수. 
saleKind= [] # 하루에  판매된 물품 목록.  예)  coffee, COFFEE, CO FFE E, coFfee, c#off$ee, cO f%%&fe*e

distinctionKind = [] # 판매된 물품의 구분된 목록. 예)  coffee, gimbap, water  등 
distinctionNumber = 0 #구분된 개수.  


def main() :
        global products, saleNumber, saleKind, distinctionKind, distinctionNumber

        loadData() # 데이터 읽어오기.

        ## 원본 출력
        print('(0) 오늘 판매된 물품 목록')
        printData(saleKind, saleNumber)
        
        ## 1. 데이터에서 공백및 특수문자를 제거한 후 소문자로 만든다. 
        saleKind = makeNormalData(saleKind, saleNumber)
        print(' (1) 목록에서 공백 및 특수문자 제거후 소문자로 만든 결과')
        printData(saleKind, saleNumber)

        ## 2. 물품의 이름을 바로 잡는다. 
        saleKind = correctLetterOrder(saleKind, saleNumber, products)
        print(' (2) 글자의 순서를 모두 수정한 결과')
        printData(saleKind, saleNumber)

        ## 3. 데이터에서 중복된 목록을 제거한다. 
        distinctionKind = makeDistinctedData(saleKind, saleNumber)
        print(' (3) 중복 목록을 제거하고 정렬한 결과(=오늘 판매된 제품 종류)')
        printData(distinctionKind, len(distinctionKind))
        
## 함수 선언 부분
def  loadData() : # 데이터 불러오기
    global products, saleNumber, saleKind, distinctionKind, distinctionNumber

    ###########
    # 제공 데이터 세트 1 
    # 18건 데이터. 
    ###########
    saleNumber = 20
    saleKind = \
             [  "coffee", "eeFFCo",  "amenr", "Ra Men",  "CO FFE E", 
		"coFfee", "c#off$ee", "cOe f%%&f*e", "bapgim", "rice", "RiCE", "*Ri&c@e", 
		"gim $bap", "BAP@gim", "*G*imba p", "water","FFCOEE", "WATER", "TERAW",  "*tW$a ER#" ]
    

def printData(kind, count) :
    global products, saleNumber, saleKind, distinctionKind, distinctionNumber
    printHeader()
    if len(kind) <= 0 :
            return
    for i in range(0, count) :
            print("%s " % kind[i])
    print()

def printHeader() :
    print("--------------")
    print("물품 종류")
    print("--------------")
    
## 메인 함수 호출 ##
if __name__ == "__main__" :
    main()