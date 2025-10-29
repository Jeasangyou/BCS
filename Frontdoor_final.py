#import numpy as np
from collections import Counter
import random
columns_to_check = [5, 6, 9, 11, 12, 13, 14, 15, 16, 17, 19, 20, 26, 27]
# 행렬 초기화


# 위 2행은 0으로 채움
matrix = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]




print(matrix)

names = ["정현호", "김병지", "임민택", 
         "김승헌", "곽산휘", "인가빈", "김경민",
         "손현서", "박현수", "노준범", "마경군", 
         "이현준", "이상민", "박현빈",
         "윤종수", "권태완", "박찬영", "한상혁",
         "홍석준", "김태만", "김민우", "성연호",
         "채문기", "권태우", "서동우", "최성민"]
 
    

#names = ["이태민", "오준석", "조석연",
#         "심현호", "김동범", "양태강", "김도윤",
#         "박상준", "조규민", "김태영", "유송완",
#         "송승우", "전승원", "윤찬우",
#         "박성빈", "김성수", "정명훈", "정명진",
#         "서준호", "윤민준", "정시원", "김경일", 
#         "홍정표", "박근태", "유제상", "곽동준",
#         "심재학"]


name_ranges = {
    "이태민": list(range(1, 9)) + list(range(15, 32)),
    "오준석": list(range(1, 6)) + list(range(22, 32)),
    "조규민": list(range(1, 9)) + list(range(15, 32)),
    "조석연": range(4, 6),
    "김도윤": range(5, 8),
    "김승헌": range(8, 12),
    "서준호": range(25, 32),
    "윤민준": list(range(10, 12)) + list(range(22, 27)),
    "김민우": range(5, 9),
    "김태영": range(1, 5),
    "송승우": range(4, 6),
    "전승원": range(4, 6),
    "김성수": range(17, 20),
    "권태완": range(1, 6),
    "홍석준": range(1, 10)
}

# 숫자에 해당하는 이름을 담을 딕셔너리
number_to_names = {}

# 휴가 스케쥴 작성
for number in range(1, len(matrix[0])+1):
    names_for_number = []
    for name, number_range in name_ranges.items():
        if number in number_range:
            names_for_number.append(name)
    number_to_names[number] = names_for_number

# 결과 출력
for number, names in number_to_names.items():
    print(f"{number}일차 휴가자: {', '.join(names)}")
    
flattened_matrix = [element for row in matrix for element in row if element != 0]
element_counts = Counter(flattened_matrix)
element_counts["김도윤"] = 999
element_counts["정명진"] = 999
element_counts["한경진"] = 999
print(element_counts)


names = ["정현호", "김병지", "임민택", 
         "김승헌", "곽산휘", "인가빈", "김경민",
         "손현서", "박현수", "노준범", "마경군", 
         "이현준", "이상민", "박현빈",
         "윤종수", "권태완", "박찬영", "한상혁",
         "홍석준", "김태만", "김민우", "성연호",
         "채문기", "권태우", "서동우", "최성민"]
 

for name in names:
    if name not in element_counts:
        element_counts[name] = 0
        

print("초기값")
print(element_counts)
        
    
    
for col in columns_to_check:  # 각 column에 대해 반복
    for row in range(0, 4):  # 각 row에 대해 반복
        if matrix[row][col] == 0:  # 0인 경우
            # 해당 column의 numbers_to_names에 있는 이름 제외
            excluded_names = set(number_to_names.get(col + 1, []))
            
            # 해당 column의 0이 아닌 요소 제외
            column_elements = {matrix[r][col] for r in range(len(matrix)) if matrix[r][col] != 0}
            excluded_names.update(column_elements)
            
            # 이웃한 column의 요소들도 제외
            if col > 0:  # 왼쪽 이웃 column 확인
                column_elements_left = {matrix[r][col - 1] for r in range(len(matrix)) if matrix[r][col - 1] != 0}
                excluded_names.update(column_elements_left)
            if col < len(matrix[0]) - 1:  # 오른쪽 이웃 column 확인
                column_elements_right = {matrix[r][col + 1] for r in range(len(matrix)) if matrix[r][col + 1] != 0}
                excluded_names.update(column_elements_right)
            
            # matrix에 남아있는 모든 이름 중 제외된 이름 제거
            valid_names = [name for name in element_counts.keys() if name not in excluded_names]
            
            if not valid_names:  # valid_names가 비어 있을 경우
                #print(f"{col + 1}일차, {row + 1}번초: 부득이하게 연속 근무자 발생")
                
                # 이웃한 column에 있는 이름도 포함하도록 재설정
                excluded_names = set(number_to_names.get(col + 1, []))  # 초기화 후 다시 설정
                column_elements = {matrix[r][col] for r in range(len(matrix)) if matrix[r][col] != 0}
                excluded_names.update(column_elements)

                # 이웃한 column은 제외하지 않음
                valid_names = [name for name in element_counts.keys() if name not in excluded_names]

            if valid_names:  # valid_names가 존재하는 경우
                # 최소 등장 횟수를 가진 이름들 찾기
                min_count = min(element_counts[name] for name in valid_names)
                least_common_names = [name for name in valid_names if element_counts[name] == min_count]
                
                # 최소 등장 횟수를 가진 이름 중 하나를 무작위로 선택
                replacement_name = random.choice(least_common_names)
                
                # 0을 대체하고, 개수 업데이트
                matrix[row][col] = replacement_name
                element_counts[replacement_name] += 1   

print("중간확인")
print(matrix)
            
                
flattened_matrix = [element for row in matrix for element in row if element != 0]
element_counts = Counter(flattened_matrix)
element_counts["김도윤"] = 999
element_counts["정명진"] = 999
element_counts["한경진"] = 999
print(element_counts)

names = ["정현호", "김병지", "임민택", 
         "김승헌", "곽산휘", "인가빈", "김경민",
         "손현서", "박현수", "노준범", "마경군", 
         "이현준", "이상민", "박현빈",
         "윤종수", "권태완", "박찬영", "한상혁",
         "홍석준", "김태만", "김민우", "성연호",
         "채문기", "권태우", "서동우", "최성민"]
 
for name in names:
    if name not in element_counts:
        element_counts[name] = 0

for col in range(len(matrix[0])):  # 각 column에 대해 반복
    for row in range(2, 4):  # 각 row에 대해 반복
        if matrix[row][col] == 0:  # 0인 경우
            # 해당 column의 numbers_to_names에 있는 이름 제외
            excluded_names = set(number_to_names.get(col + 1, []))
            
            # 해당 column의 0이 아닌 요소 제외
            column_elements = {matrix[r][col] for r in range(len(matrix)) if matrix[r][col] != 0}
            excluded_names.update(column_elements)
            
            # 이웃한 column의 요소들도 제외
            if col > 0:  # 왼쪽 이웃 column 확인
                column_elements_left = {matrix[r][col - 1] for r in range(len(matrix)) if matrix[r][col - 1] != 0}
                excluded_names.update(column_elements_left)
            if col < len(matrix[0]) - 1:  # 오른쪽 이웃 column 확인
                column_elements_right = {matrix[r][col + 1] for r in range(len(matrix)) if matrix[r][col + 1] != 0}
                excluded_names.update(column_elements_right)
            
            # matrix에 남아있는 모든 이름 중 제외된 이름 제거
            valid_names = [name for name in element_counts.keys() if name not in excluded_names]
            
            if not valid_names:  # valid_names가 비어 있을 경우
                print(f"{col + 1}일차, {row + 1}번초: 부득이하게 연속 근무자 발생")
                
                # 이웃한 column에 있는 이름도 포함하도록 재설정
                excluded_names = set(number_to_names.get(col + 1, []))  # 초기화 후 다시 설정
                column_elements = {matrix[r][col] for r in range(len(matrix)) if matrix[r][col] != 1}
                excluded_names.update(column_elements)

                # 이웃한 column은 제외하지 않음
                valid_names = [name for name in element_counts.keys() if name not in excluded_names]

            if valid_names:  # valid_names가 존재하는 경우
                # 최소 등장 횟수를 가진 이름들 찾기
                min_count = min(element_counts[name] for name in valid_names)
                least_common_names = [name for name in valid_names if element_counts[name] == min_count]
                print("최소 근무 인원:")
                print(least_common_names)
                
                # 최소 등장 횟수를 가진 이름 중 하나를 무작위로 선택
                replacement_name = random.choice(least_common_names)
                
                # 0을 대체하고, 개수 업데이트
                matrix[row][col] = replacement_name
                element_counts[replacement_name] += 1

print("중간확인2")
print(matrix)
flattened_matrix = [element for row in matrix for element in row if element != 0]
element_counts = Counter(flattened_matrix)
element_counts["김도윤"] = 999
element_counts["정명진"] = 999
element_counts["한경진"] = 999
print(element_counts)

names = ["정현호", "김병지", "임민택", 
         "김승헌", "곽산휘", "인가빈", "김경민",
         "손현서", "박현수", "노준범", "마경군", 
         "이현준", "이상민", "박현빈",
         "윤종수", "권태완", "박찬영", "한상혁",
         "홍석준", "김태만", "김민우", "성연호",
         "채문기", "권태우", "서동우", "최성민"]
 

for name in names:
    if name not in element_counts:
        element_counts[name] = 0
        
for col in range(len(matrix[0])):  # 각 column에 대해 반복
    for row in range(0,1):  # 각 row에 대해 반복
        if matrix[row][col] == 0:  # 0인 경우
            # 해당 column의 numbers_to_names에 있는 이름 제외
            excluded_names = set(number_to_names.get(col + 1, []))
            
            # 해당 column의 0이 아닌 요소 제외
            column_elements = {matrix[r][col] for r in range(len(matrix)) if matrix[r][col] != 0}
            excluded_names.update(column_elements)
            
            # 이웃한 column의 요소들도 제외
            if col > 0:  # 왼쪽 이웃 column 확인
                column_elements_left = {matrix[r][col - 1] for r in range(len(matrix)) if matrix[r][col - 1] != 0}
                excluded_names.update(column_elements_left)
            if col < len(matrix[0]) - 1:  # 오른쪽 이웃 column 확인
                column_elements_right = {matrix[r][col + 1] for r in range(len(matrix)) if matrix[r][col + 1] != 0}
                excluded_names.update(column_elements_right)
            
            # matrix에 남아있는 모든 이름 중 제외된 이름 제거
            valid_names = [name for name in element_counts.keys() if name not in excluded_names]
            
            if not valid_names:  # valid_names가 비어 있을 경우
                #print(f"{col + 1}일차, {row + 1}번초: 부득이하게 연속 근무자 발생")
                
                # 이웃한 column에 있는 이름도 포함하도록 재설정
                excluded_names = set(number_to_names.get(col + 1, []))  # 초기화 후 다시 설정
                column_elements = {matrix[r][col] for r in range(len(matrix)) if matrix[r][col] != 0}
                excluded_names.update(column_elements)

                # 이웃한 column은 제외하지 않음
                valid_names = [name for name in element_counts.keys() if name not in excluded_names]

            if valid_names:  # valid_names가 존재하는 경우
                # 최소 등장 횟수를 가진 이름들 찾기
                min_count = min(element_counts[name] for name in valid_names)
                least_common_names = [name for name in valid_names if element_counts[name] == min_count]
                
                # 최소 등장 횟수를 가진 이름 중 하나를 무작위로 선택
                replacement_name = random.choice(least_common_names)
                
                # 0을 대체하고, 개수 업데이트
                matrix[row][col] = replacement_name
                element_counts[replacement_name] += 1
                
         
names = ["정현호", "김병지", "임민택", 
         "김승헌", "곽산휘", "인가빈", "김경민",
         "손현서", "박현수", "노준범", "마경군", 
         "이현준", "이상민", "박현빈",
         "윤종수", "권태완", "박찬영", "한상혁",
         "홍석준", "김태만", "김민우", "성연호",
         "채문기", "권태우", "서동우", "최성민"]
 

for name in names:
    if name not in element_counts:
        element_counts[name] = 0

element_counts["김도윤"] = 999
element_counts["정명진"] = 999
element_counts["한경진"] = 999
for col in range(len(matrix[0])):  # 각 column에 대해 반복
    for row in range(1,2):  # 각 row에 대해 반복
        if matrix[row][col] == 0:  # 0인 경우
            # 해당 column의 numbers_to_names에 있는 이름 제외
            excluded_names = set(number_to_names.get(col + 1, []))
            
            # 해당 column의 0이 아닌 요소 제외
            column_elements = {matrix[r][col] for r in range(len(matrix)) if matrix[r][col] != 0}
            excluded_names.update(column_elements)
            
            # 이웃한 column의 요소들도 제외
            if col > 0:  # 왼쪽 이웃 column 확인
                column_elements_left = {matrix[r][col - 1] for r in range(len(matrix)) if matrix[r][col - 1] != 0}
                excluded_names.update(column_elements_left)
            if col < len(matrix[0]) - 1:  # 오른쪽 이웃 column 확인
                column_elements_right = {matrix[r][col + 1] for r in range(len(matrix)) if matrix[r][col + 1] != 0}
                excluded_names.update(column_elements_right)
            
            # matrix에 남아있는 모든 이름 중 제외된 이름 제거
            valid_names = [name for name in element_counts.keys() if name not in excluded_names]
            
            if not valid_names:  # valid_names가 비어 있을 경우
                #print(f"{col + 1}일차, {row + 1}번초: 부득이하게 연속 근무자 발생")
                
                # 이웃한 column에 있는 이름도 포함하도록 재설정
                excluded_names = set(number_to_names.get(col + 1, []))  # 초기화 후 다시 설정
                column_elements = {matrix[r][col] for r in range(len(matrix)) if matrix[r][col] != 0}
                excluded_names.update(column_elements)

                # 이웃한 column은 제외하지 않음
                valid_names = [name for name in element_counts.keys() if name not in excluded_names]

            if valid_names:  # valid_names가 존재하는 경우
                # 최소 등장 횟수를 가진 이름들 찾기
                min_count = min(element_counts[name] for name in valid_names)
                least_common_names = [name for name in valid_names if element_counts[name] == min_count]
                
                # 최소 등장 횟수를 가진 이름 중 하나를 무작위로 선택
                replacement_name = random.choice(least_common_names)
                
                # 0을 대체하고, 개수 업데이트
                matrix[row][col] = replacement_name
                element_counts[replacement_name] += 1
                
print("최종확인")
print(matrix)


all_names = {element for row in matrix for element in row if element != 0}
final_total_counts = Counter({name: 0 for name in all_names})

total_counts = Counter()

# 선택된 column에서 요소별 등장 횟수 계산
final_total = Counter({name: 0 for name in all_names})

# 선택된 column에서 요소별 등장 횟수 계산
for col in columns_to_check:
    for row in range(len(matrix)):
        person = matrix[row][col]
        if person != 0:  # 0은 제외
            final_total[person] += 1

first_row = matrix[0]
counts = Counter(first_row)
print("1번초 횟수:")
print(counts)

second_row = matrix[1]
counts = Counter(second_row)
print("2번초 횟수:")
print(counts)

third_row = matrix[2]
counts = Counter(third_row)
print("3번초 횟수:")
print(counts)

fourth_row = matrix[3]
counts = Counter(fourth_row)
print("4번초 횟수:")
print(counts)

elements = []
for row in matrix:
    for col in columns_to_check:
        if col < len(row):  # 안전하게 인덱스 확인
            value = row[col]
            if value != '':  # 빈 문자열은 무시 (필요 시 조건 제거 가능)
                elements.append(value)

# 등장 횟수 세기
counts = Counter(elements)

# 결과 출력
print("주말 근무:")
print(counts)

for row in matrix:
    print(row)

flattened_matrix_final = [element for row in matrix for element in row]

# 2. 각 요소의 개수를 세기
element_counts_final = Counter(flattened_matrix_final)

# 3. 요소를 개수에 따라 내림차순으로 정렬
sorted_counts_final = sorted(element_counts_final.items(), key=lambda x: x[1], reverse=True)

print("근무자별 최종 근무 횟수 (내림차순 정렬):")
for element, count in sorted_counts_final:
    print(f"{element}: {count}회")
