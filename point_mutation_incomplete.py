#import numpy as np
from collections import Counter
import random
columns_to_check = [0, 1, 7, 8, 14, 15, 21, 22]   #zero_based_index
# 2*27 행렬 생성


list1 = ['정재훈', '이승민', '이태민', '장명규', '김민혁', '박승준', '장명규', '김종수', '김주완', '이선우', '윤민준', '김지혁', '이다준', '정은혁', '이성빈', '이다준', '김주완', '박영선', '김주완', '서준호', '한경진', '이선우', '한경진', '이성빈', '한경진', '이성빈', '박영선', '김주완']
list2 = ['오상훈', '김민혁', '박승준', '이승민', '정재훈', '이태민', '이승민', '정은혁', '박영선', '한경진', '조규민', '박영선', '서준호', '김종수', '서준호', '김지혁', '조규민', '정은혁', '윤민준', '이선우', '김종수', '윤민준', '조규민', '이다준', '이선우', '정은혁', '서준호', '윤민준']

# Combine the two lists into a single list
combined_list = list1 + list2

# Manually create a 2x27 matrix
matrix = [combined_list[:27], combined_list[27:]]

# Print the matrix
for row in matrix:
    print(row)



name_ranges = {
    "이승찬": range(3, 13),
    "오상훈": range(2, 8),
    "이승민": range(5, 6),
    "심현호": range(17, 26),
    "유제상": range(1, 8),
    "김종수": range(15, 21),
    "김지혁": range(17, 29),
    "이성빈": range(17, 22),
    "김경일": range(24, 29)     #최종 근무일 이후 휴가일자는 미포함
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
    
target_name = "정은혁"

# matrix에서 target_name을 찾고, 해당 위치를 0으로 바꿈
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if matrix[row][col] == target_name:
            matrix[row][col] = 0

flattened_matrix = [
    matrix[row][col] 
    for col in columns_to_check 
    for row in range(len(matrix)) 
    if matrix[row][col] != 0
]
element_counts = Counter(flattened_matrix)

names = [
    "박영선", "김종수", "이선우", "서준호", "윤민준", "한경진", "조규민", 
    "김주완", "이다준", "이성빈", "김지혁"
]

for name in names:
    if name not in element_counts:
        element_counts[name] = 0

print(element_counts)
        
for col in columns_to_check:  # 각 column에 대해 반복
    for row in range(0,2):  # 각 row에 대해 반복
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
            print(valid_names)
            
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
                
flattened_matrix = [element for row in matrix for element in row if element != 0]
element_counts = Counter(flattened_matrix)

names = [
    "박영선", "김종수", "이선우", "서준호", "윤민준", "한경진", "조규민", 
    "김주완", "이다준", "이성빈", "김지혁"
]

for name in names:
    if name not in element_counts:
        element_counts[name] = 0
        
for col in range(len(matrix[0])):  # 각 column에 대해 반복
    for row in range(0,2):  # 각 row에 대해 반복
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
            print(valid_names)
            
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
                
                
for row in matrix:
    print(row)
    
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

# 결과 출력
for person, count in final_total.items():
    print(f"휴일 근무->{person}: {count}회")

print(element_counts)
for row in matrix:
    print(row)
    
names = names = [
    "박영선", "김종수", "이선우", "서준호", "윤민준", "한경진", "조규민", 
    "김주완", "이다준", "이성빈", "김지혁"
]


flattened_matrix_final = [element for row in matrix for element in row]

# 2. 각 요소의 개수를 세기
element_counts_final = Counter(flattened_matrix_final)

for name in names:
    if name not in element_counts:
        element_counts_final[name] = 0
# 3. 요소를 개수에 따라 내림차순으로 정렬
sorted_counts_final = sorted(element_counts_final.items(), key=lambda x: x[1], reverse=True)

print("근무자별 최종 근무 횟수 (내림차순 정렬):")
for element, count in sorted_counts_final:
    print(f"{element}: {count}회")