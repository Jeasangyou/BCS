#import numpy as np
from collections import Counter
import random


# 사수 or 조장 집단 입력
names = ["이승찬", "오상훈", "정재훈", "박승준", "이승민", 
         "장명규", "김민혁", "안강현", "이동건", "김지혁", 
         "이성빈", "이다준", "김주완", "조규민", "이태민", 
         "오준석", "조석연", "심현호", "김동범", "양태강", 
         "김도윤", "김태영", "유송완", "송승우", "전승원",
         "윤찬우", "박성빈", "김성수", "정명훈"]

matrix = [[0 for _ in range(23)] for _ in range(8)]
index = 0
for i in range(23):
    for j in range(8):
        matrix[j][i] = names[index % len(names)]  # 이름 목록 순환
        index += 1
        
print("초기 행렬:")
for row in matrix:
    print(row)
    
for col in range(23):  # 23개의 column에 대해 반복
    # 해당 column의 요소 가져오기
    column_elements = [matrix[row][col] for row in range(8)]
    
    # 요소별 개수 계산
    element_counts = Counter(column_elements)
    
    # 두 번 이상 나오는 요소 찾기
    duplicates = {element: count for element, count in element_counts.items() if count > 1}
    
    if duplicates:
        print(f"{col + 1}일차 (index {col}) 에서 2회 근무자 발생, 수정 필요: {duplicates}")
        
        # row1(0번 row) 제외 중복 제거
        for row in range(1, 8):  # row1만 제외하므로 row2부터 확인
            if matrix[row][col] in duplicates:
                print(f"    - {col + 1}일차 row {row + 1}에서 '{matrix[row][col]}' 제거")
                matrix[row][col] = 0  # 중복된 요소를 0으로 변경
    else:
        print(f"{col + 1}일차 2회 근무자 없습니다.")
    
for col in range(len(matrix[0]) - 1):  # 마지막 column은 비교할 이웃이 없으므로 -1
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
    
changes = []
for col in range(len(matrix[0])):  # 각 column에 대해 반복
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

#전체 근무자의 근무 횟수 계산
flattened_matrix = [element for row in matrix for element in row if element != 0]
element_counts = Counter(flattened_matrix)

# 휴가자 대체; 가장 근무 횟수가 적은 사람부터 차례대로 대체하도록
for col in range(len(matrix[0])):  # 각 column에 대해 반복
    for row in range(len(matrix)):  # 각 row에 대해 반복
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
                print(f"{col + 1}일차, {row + 1}번초: 부득이하게 연속 불침번 발생")
                
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


print("최종 근무 시간표는 다음과 같습니다:")                
for row in matrix:
    print(row)
    
# 1. 행렬의 모든 요소를 하나의 리스트로 평탄화(flatten)
flattened_matrix_final = [element for row in matrix for element in row]

# 2. 각 요소의 개수를 세기
element_counts_final = Counter(flattened_matrix_final)

# 3. 요소를 개수에 따라 내림차순으로 정렬
sorted_counts_final = sorted(element_counts_final.items(), key=lambda x: x[1], reverse=True)

print("근무자별 최종 근무 횟수 (내림차순 정렬):")
for element, count in sorted_counts_final:
    print(f"{element}: {count}회")
    
print("근무 기간 내 휴가자의 경우 근무 횟수가 적어질 수 있으며, 이는 시스템 오류가 아닙니다.")