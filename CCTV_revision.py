#import numpy as np
from collections import Counter
import random


# 사수 or 조장 집단 입력
names = ["이승찬", "오상훈", "정재훈", "박승준", "이승민", 
         "장명규", "김민혁", "안강현", "이동건", "김지혁", 
         "이성빈", "이다준", "김주완", "조규민"]
#조장 집단
#names = ["이태민", "오준석", "조석연", "심현호", "김동범", 
 #        "양태강", "김도윤", "김태영", "유송완", "송승우", 
  #       "전승원", "윤찬우", "박성빈", "김성수", "정명훈"]

excluded_columns = [5, 6, 12, 13, 14, 15, 16, 17, 19, 20]
matrix = [[1 for _ in range(23)] for _ in range(2)]
index = 0
for i in range(2):
    for j in range(23):
        if j in excluded_columns:  # 제외할 column은 0으로 유지
            continue
        matrix[i][j] = names[index % len(names)]  # 이름 목록 순환
        index += 1

print("초기 행렬:")
for row in matrix:
    print(row)
    
for col in range(23):  # 23개의 column에 대해 반복
    if col in excluded_columns:  # 제외할 column 건너뛰기
        continue
    # 해당 column의 요소 가져오기
    column_elements = [matrix[row][col] for row in range(2)]
    
    # 요소별 개수 계산
    element_counts = Counter(column_elements)
    
    # 두 번 이상 나오는 요소 찾기
    duplicates = {element: count for element, count in element_counts.items() if count > 1}
    
    if duplicates:
        print(f"{col + 1}일차 (index {col}) 에서 2회 근무자 발생, 수정 필요: {duplicates}")
        
        # row1(0번 row) 제외 중복 제거
        for row in range(1, 2):  # row1만 제외하므로 row2부터 확인
            if matrix[row][col] in duplicates:
                print(f"    - {col + 1}일차 row {row + 1}에서 '{matrix[row][col]}' 제거")
                matrix[row][col] = 0  # 중복된 요소를 0으로 변경
    else:
        print(f"{col + 1}일차 2회 근무자 없습니다.")
        
        
for col in range(len(matrix[0]) - 1):  # 마지막 column은 비교할 이웃이 없으므로 -1
    if col in excluded_columns:  # 제외할 column 건너뛰기
        continue
    # 현재 column과 다음 column의 모든 요소를 비교
    current_column = [matrix[row][col] for row in range(len(matrix))]
    next_column = [matrix[row][col + 1] for row in range(len(matrix))]
    
    # 두 column의 공통 요소 찾기
    duplicates = set(current_column) & set(next_column)
    
    if duplicates:
        for duplicate in duplicates:
            # 중복된 요소를 하나만 0으로 바꾸기 (우선 다음 column에서 변경)
            for row in range(len(matrix)):
                if matrix[row][col + 1] == duplicate:
                    matrix[row][col + 1] = 0
                    break  # 한 번만 변경 후 탈출

# 결과 출력
print("수정된 행렬:")
for row in matrix:
    print(row)
    
name_ranges = {
    "이승찬": range(1, 14),
    "장명규": range(8, 16),
    "김민혁": range(8, 16),
    "오준석": range(8, 13),
    "김동범": range(1, 8),
    "양태강": range(8, 13),
    "안강현": range(1, 4),
    "이동건": list(range(1, 5)) + list(range(8, 13)),
    "조규민": range(10, 16),
    "전승원": range(1, 7),
    "윤찬우": range(1, 6),
    "박성빈": range(1, 4),
    "김성수": range(1, 6)
}

number_to_names = {}
for number in range(1, 24):
    names_for_number = []
    for name, number_range in name_ranges.items():
        if number in number_range:
            names_for_number.append(name)
    number_to_names[number] = names_for_number

# 결과 출력
for number, names in number_to_names.items():
    print(f"{number}일차 휴가자: {', '.join(names)}")
    
changes = []

for col in range(len(matrix[0])):  # 각 column에 대해 반복
    if col in excluded_columns:  # 제외할 column 건너뛰기
        continue
    col_index = col + 1  # 실제 column 번호 (1부터 시작)
    valid_names = number_to_names.get(col_index, [])
    
    for row in range(len(matrix)):  # 각 row에 대해 반복
        if matrix[row][col] in valid_names:  # 조건 확인
            changes.append((col_index, row + 1, matrix[row][col]))  # 변경 사항 기록
            matrix[row][col] = 0  # 요소를 0으로 변경

print("\n변경된 근무자:")
for change in changes:
    print(f"{change[0]}일차, Row {change[1]}: {change[2]} 근무 제외")
    
for row in matrix:
    print(row)
    
flattened_matrix = flattened_matrix = [element for row in matrix for element in row if element != 0 and element != 1]
element_counts = Counter(flattened_matrix)


names = ["이승찬", "오상훈", "정재훈", "박승준", "이승민", 
         "장명규", "김민혁", "안강현", "이동건", "김지혁", 
         "이성빈", "이다준", "김주완", "조규민"]
for name in names:
    print(name)
    if name not in element_counts:
        element_counts[name] = 0

print(flattened_matrix)
print(element_counts)