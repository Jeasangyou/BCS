#import numpy as np
from collections import Counter
import random
# 사수 or 조장 집단 입력
names = ["이승찬", "오상훈", "정재훈", "박승준", "이승민", 
         "장명규", "김민혁", "안강현", "이동건", "김지혁", 
         "이성빈", "이다준", "김주완", "조규민"]

excluded_columns = [5, 6, 12, 13, 14, 15, 16, 17, 19, 20]

#조장 집단
#names = ["이태민", "오준석", "조석연", "심현호", "김동범", 
 #        "양태강", "김도윤", "김태영", "유송완", "송승우", 
  #       "전승원", "윤찬우", "박성빈", "김성수", "정명훈"]

# 20250113~20250204 총 23일(주/야간)-->23*2 행렬. 
matrix = [[0 for _ in range(23)] for _ in range(2)]
index = 0
for i in range(2):
    for j in range(23):
        matrix[i][j] = names[index % len(names)]  # 이름 목록 순환
        index += 1

# 최초 시간표 출력
for row in matrix:
    print(row)
    
#하루에 2번 근무 서는 경우 배제    
for col in range(23):  # 23개의 column에 대해 반복
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

# 결과 출력
#print("\n수정된 행렬:")
#for row in matrix:
    #print(row)
        
# 이름과 해당하는 범위
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

# 숫자에 해당하는 이름을 담을 딕셔너리
number_to_names = {}

# 휴가 스케쥴 작성
for number in range(1, 24):
    names_for_number = []
    for name, number_range in name_ranges.items():
        if number in number_range:
            names_for_number.append(name)
    number_to_names[number] = names_for_number

# 결과 출력
for number, names in number_to_names.items():
    print(f"{number}일차 휴가자: {', '.join(names)}")

#휴가자가 근무표에 포함된 경우 근무 제외
changes = []

for col in range(len(matrix[0])):  # 각 column에 대해 반복
    col_index = col + 1  # 실제 column 번호 (1부터 시작)
    valid_names = number_to_names.get(col_index, [])
    
    for row in range(len(matrix)):  # 각 row에 대해 반복
        if matrix[row][col] in valid_names:  # 조건 확인
            changes.append((col_index, row + 1, matrix[row][col]))  # 변경 사항 기록
            matrix[row][col] = 0  # 요소를 0으로 변경

# 4. 결과 출력
#print("수정 시간표:")
#for row in matrix:
    #print(row)

print("\n변경된 근무자:")
for change in changes:
    print(f"{change[0]}일차, Row {change[1]}: {change[2]} 근무 제외")

#전체 근무자의 근무 횟수 계산
flattened_matrix = [element for row in matrix for element in row if element != 0]
element_counts = Counter(flattened_matrix)
print(element_counts)

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
            
            if valid_names:
                # 최소 등장 횟수를 가진 이름들 찾기
                min_count = min(element_counts[name] for name in valid_names)
                least_common_names = [name for name in valid_names if element_counts[name] == min_count]
                
                # 최소 등장 횟수를 가진 이름 중 하나를 무작위로 선택
                replacement_name = random.choice(least_common_names)
                
                # 0을 대체하고, 개수 업데이트
                matrix[row][col] = replacement_name
                element_counts[replacement_name] += 1

duplicates_found = False
for col in range(len(matrix[0]) - 1):  # 마지막 column은 비교할 이웃이 없으므로 -1
    for row in range(len(matrix)):  # 각 row에 대해 반복
        if matrix[row][col] == matrix[row][col + 1]:  # 이웃하는 column에 같은 값이 있을 경우
            print(f"Row {row + 1}, Column {col + 1}과 Column {col + 2}에서 같은 값이 존재: {matrix[row][col]}")
            duplicates_found = True
            
if not duplicates_found:
    print("연속 근무자 없습니다.")


# 4. 결과 출력

# 원하는 column 번호 (0-based index)
columns_to_check = [5, 6, 12, 13, 14, 15, 16, 17, 19, 20]  #휴일 column (0-based index)

# 행렬 전체에서 등장한 모든 이름 추출
all_names = {element for row in matrix for element in row if element != 0}

# 사람별 등장 횟수를 세기 위한 Counter 초기화 (모든 이름 0회로 초기화)
total_counts = Counter({name: 0 for name in all_names})

# 선택된 column에서 요소별 등장 횟수 계산
for col in columns_to_check:
    for row in range(len(matrix)):
        person = matrix[row][col]
        if person != 0:  # 0은 제외
            total_counts[person] += 1


max_count = max(total_counts.values())
min_count = min(total_counts.values())
max_names = [name for name, count in total_counts.items() if count == max_count]
min_names = [name for name, count in total_counts.items() if count == min_count]

# Step 3: 교체 조건 확인
if max_count - min_count >= 2:
    # Step 4: 교체 조건을 만족하는 위치 찾기
    def find_valid_position(name, exclude_cols):
        """유효한 위치를 찾는 함수"""
        for col in range(len(matrix[0])):
            if col in exclude_cols:
                continue
            for row in range(len(matrix)):
                # 현재 열 및 인접한 열의 다른 행들에서 해당 이름이 존재하지 않아야 함
                neighbors = {matrix[r][c] for r in range(len(matrix)) for c in [col - 1, col + 1] if 0 <= c < len(matrix[0])}
                same_column_elements = {matrix[r][col] for r in range(len(matrix))}

                # 기존의 조건 추가: max_names가 특정 열에 위치한 경우 그 열에서만 교체 가능
                if name not in neighbors and name not in same_column_elements and name not in number_to_names.get(col + 1, []):
                    if max_name in max_names and col not in columns_to_check:
                        return row, col
                    if min_name in min_names and col in columns_to_check:
                        return row, col

            return None, None
    # 각 max_name에 대해 min_names의 요소들과 각각 교체할 위치를 찾는다
    for max_name in max_names:
        is_replaced = False  # 교체 여부를 추적하는 변수

        for min_name in min_names:
            max_name_positions = [(row, col) for col in range(len(matrix[0]))
                                  for row in range(len(matrix)) if matrix[row][col] == max_name]
            min_name_positions = [(row, col) for col in range(len(matrix[0]))
                                  for row in range(len(matrix)) if matrix[row][col] == min_name]

            # 교체할 수 있는지 확인
            for max_pos in max_name_positions:
                max_row, max_col = max_pos
                for min_pos in min_name_positions:
                    min_row, min_col = min_pos

                    # 유효한 위치 찾기
                    new_max_row, new_max_col = find_valid_position(min_name, {max_col})
                    new_min_row, new_min_col = find_valid_position(max_name, {min_col})

                    # 유효한 위치가 있으면 교체
                    if new_max_row is not None and new_min_row is not None:
                        matrix[max_row][max_col], matrix[new_max_row][new_max_col] = matrix[new_max_row][new_max_col], matrix[max_row][max_col]
                        matrix[min_row][min_col], matrix[new_min_row][new_min_col] = matrix[new_min_row][new_min_col], matrix[min_row][min_col]

                        print(f"{max_name}을 {min_name}과 교체했습니다.")
                        is_replaced = True
                        break  # 교체 후 더 이상 이 min_name을 사용하지 않음

                if is_replaced:
                    break  # max_name에 대해 교체가 완료되면 더 이상 교체할 필요 없음

        if not is_replaced:
            print("교체 실패")
else:
    print("주말 근무 균등화 완료")


#print(total_counts)
# 결과 출력

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
#for person, count in final_total.items():
#    print(f"휴일 근무->{person}: {count}회")

# 1. 행렬의 모든 요소를 하나의 리스트로 평탄화(flatten)
flattened_matrix_final = [element for row in matrix for element in row]

# 2. 각 요소의 개수를 세기
element_counts_final = Counter(flattened_matrix_final)

# 3. 요소를 개수에 따라 내림차순으로 정렬
sorted_counts_final = sorted(element_counts_final.items(), key=lambda x: x[1], reverse=True)

print("근무자별 최종 근무 횟수 (내림차순 정렬):")
for element, count in sorted_counts_final:
    print(f"{element}: {count}회")
    
# 결과 출력
print("최종 근무 시간표는 다음과 같습니다:")
for row in matrix:
    print(row)