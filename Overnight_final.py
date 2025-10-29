#import numpy as np
from collections import Counter
import random
columns_to_check = [4, 5, 11, 12, 18, 19]
rows_to_check = [2, 3, 4, 5]
selected_rows = [0, 1, 6, 7]

matrix =  [
    ['정명진', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ['김성수', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ['이상민', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ['전승원', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ['김태영', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ['김도윤', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ['김주완', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ['김동범', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

print(matrix)

def count_elements_in_rows(matrix, rows_to_check):
    # 카운트를 저장할 Counter 객체
    element_count = Counter()

    # 지정된 행들에 대해서만 반복
    for row_index in rows_to_check:
        # 해당 행의 각 요소를 카운트
        element_count.update(matrix[row_index])

    # 결과 출력
    for element, count in element_count.items():
        print(f"{element} : {count}회")

names = ["이다준", "김주완", "조규민", "김태영", "유송완", 
         "송승우", "전승원", "윤찬우", "박성빈", 
         "김성수", "정명훈", "정명진", "마경군", "이현준",
         "이상민", "박현빈",
         "김종수", "이선우", "서준호", "윤민준", "한경진", 
         "정시원", "김경일", "홍정표", "박근태", "유제상", 
         "곽동준", "심재학", "강명진", "김태만", "김민우",
         "성연호", "채문기"]

#4.1.기준 휴가자
name_ranges = {
    "김병지": range(15, 16),
    "인가빈": range(15, 16),
    "서준호": range(15, 16),
    "김태영": range(1, 5),
    "정명진": range(15, 16),
    "이현준": range(15, 16),
    "채문기": range(1, 4)
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

names = ["이다준", "김주완", "조규민", "김태영", "유송완", 
         "송승우", "전승원", "윤찬우", "박성빈", 
         "김성수", "정명훈", "정명진", "마경군", "이현준",
         "이상민", "박현빈",
         "김종수", "이선우", "서준호", "윤민준", "한경진", 
         "정시원", "김경일", "홍정표", "박근태", "유제상", 
         "곽동준", "심재학", "강명진", "김태만", "김민우",
         "성연호", "채문기"]
for name in names:
    if name not in element_counts:
        element_counts[name] = 0
        
for col in range(len(matrix[0])):  # 각 column에 대해 반복
    for row in range(2, 6):  # 2, 3, 4, 5번 row에 대해 반복
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
            valid_names = [name for name in names if name not in excluded_names]
            
            if not valid_names:  # valid_names가 비어 있을 경우
                print(f"{col + 1}일차, {row + 1}번초: 부득이하게 연속 근무자 발생")
                
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

     
print("2번초, 3번초 투입 결과")           
for row in matrix:
    print(row)
    
names = ["이다준", "김주완", "조규민", "김태영", "유송완", 
         "송승우", "전승원", "윤찬우", "박성빈", 
         "김성수", "정명훈", "정명진", "마경군", "이현준",
         "이상민", "박현빈",
         "김종수", "이선우", "서준호", "윤민준", "한경진", 
         "정시원", "김경일", "홍정표", "박근태", "유제상", 
         "곽동준", "심재학", "강명진", "김태만", "김민우",
         "성연호", "채문기"]
for name in names:
    if name not in element_counts:
        element_counts[name] = 0 
        
for col in range(len(matrix[0])):  # 각 column에 대해 반복
    for row in selected_rows:  # 2, 3, 4, 5번 row에 대해 반복
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
            valid_names = [name for name in names if name not in excluded_names]
            
            if not valid_names:  # valid_names가 비어 있을 경우
                print(f"{col + 1}일차, {row + 1}번초: 부득이하게 연속 근무자 발생")
                
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
                            
all_names = {element for row in matrix for element in row if element != 0}
final_total_counts = Counter({name: 0 for name in all_names})

total_counts = Counter()

print("전체 투입 결과")                   
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

rows_to_check = [2,3,4,5]
print("2,3번초 근무 횟수는 다음과 같습니다")
count_elements_in_rows(matrix, rows_to_check)

print("휴가자의 경우 근무 횟수가 적게 설정될 수 있으나, 이는 시스템상의 오류가 아니며 소통과 공감 시간 논의 결과를 반영한 것임을 밝힙니다.")