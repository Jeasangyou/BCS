from collections import Counter
import random
columns_to_check = [4, 5, 11, 12, 18, 19]  
matrix1 = [[0 for _ in range(11)] for _ in range(2)]
matrix2 = [[0 for _ in range(14)] for _ in range(2)]

names = [
    "오준석", "심현호", "조석연", "김동범", "양태강", 
    "김도윤", "박상준", "정시원", "김경일", "홍정표", 
    "박근태", "유제상", "곽동준"
]


name_ranges = {
    "이선우": range(1, 6),
    "오상훈": range(1, 5),
    "이승민": range(2, 3),
    "심현호": range(16, 23),
    "유제상": range(1, 5),
    "박영선": range(1, 6),
    "김종수": range(12, 18),
}

# 숫자에 해당하는 이름을 담을 딕셔너리
number_to_names = {}

# 휴가 스케쥴 작성
for number in range(1, len(matrix1[0])+1):
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

names = [
    "오준석", "심현호", "조석연", "김동범", "양태강", 
    "김도윤", "박상준", "정시원", "김경일", "홍정표", 
    "박근태", "유제상", "곽동준"
]

for number in range(1, len(matrix1[0])+1):
    names_for_number = []
    for name, number_range in name_ranges.items():
        if number in number_range:
            names_for_number.append(name)
    number_to_names[number] = names_for_number

# 결과 출력
for number, names in number_to_names.items():
    print(f"{number}일차 휴가자: {', '.join(names)}")

flattened_matrix = [element for row in matrix1 for element in row if element != 0]
element_counts = Counter(flattened_matrix)

names = [
    "오준석", "심현호", "조석연", "김동범", "양태강", 
    "김도윤", "박상준", "정시원", "김경일", "홍정표", 
    "박근태", "유제상", "곽동준"
]

for name in names:
    if name not in element_counts:
        element_counts[name] = 0
        
for col in columns_to_check:  # 각 column에 대해 반복
    for row in range(len(matrix1)):  # 각 row에 대해 반복
        if matrix1[row][col] == 0:  # 0인 경우
            # 해당 column의 numbers_to_names에 있는 이름 제외
            excluded_names = set(number_to_names.get(col + 1, []))
            
            # 해당 column의 0이 아닌 요소 제외
            column_elements = {matrix1[r][col] for r in range(len(matrix1)) if matrix1[r][col] != 0}
            excluded_names.update(column_elements)
            
            # 이웃한 column의 요소들도 제외
            if col > 0:  # 왼쪽 이웃 column 확인
                column_elements_left = {matrix1[r][col - 1] for r in range(len(matrix1)) if matrix1[r][col - 1] != 0}
                excluded_names.update(column_elements_left)
            if col < len(matrix1[0]) - 1:  # 오른쪽 이웃 column 확인
                column_elements_right = {matrix1[r][col + 1] for r in range(len(matrix1)) if matrix1[r][col + 1] != 0}
                excluded_names.update(column_elements_right)
            
            # matrix에 남아있는 모든 이름 중 제외된 이름 제거
            valid_names = [name for name in element_counts.keys() if name not in excluded_names]
            
            if not valid_names:  # valid_names가 비어 있을 경우
                print(f"{col + 1}일차, {row + 1}번초: 부득이하게 연속 근무자 발생")
                
                # 이웃한 column에 있는 이름도 포함하도록 재설정
                excluded_names = set(number_to_names.get(col + 1, []))  # 초기화 후 다시 설정
                column_elements = {matrix1[r][col] for r in range(len(matrix1)) if matrix1[r][col] != 0}
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
                matrix1[row][col] = replacement_name
                element_counts[replacement_name] += 1

flattened_matrix = [element for row in matrix1 for element in row if element != 0]
element_counts = Counter(flattened_matrix)

names = [
    "오준석", "심현호", "조석연", "김동범", "양태강", 
    "김도윤", "박상준", "정시원", "김경일", "홍정표", 
    "박근태", "유제상", "곽동준"
]

for name in names:
    if name not in element_counts:
        element_counts[name] = 0
        
for col in range(len(matrix1[0])):  # 각 column에 대해 반복
    for row in range(0,2):  # 각 row에 대해 반복
        if matrix1[row][col] == 0:  # 0인 경우
            # 해당 column의 numbers_to_names에 있는 이름 제외
            excluded_names = set(number_to_names.get(col + 1, []))
            
            # 해당 column의 0이 아닌 요소 제외
            column_elements = {matrix1[r][col] for r in range(len(matrix1)) if matrix1[r][col] != 0}
            excluded_names.update(column_elements)
            
            # 이웃한 column의 요소들도 제외
            if col > 0:  # 왼쪽 이웃 column 확인
                column_elements_left = {matrix1[r][col - 1] for r in range(len(matrix1)) if matrix1[r][col - 1] != 0}
                excluded_names.update(column_elements_left)
            if col < len(matrix1[0]) - 1:  # 오른쪽 이웃 column 확인
                column_elements_right = {matrix1[r][col + 1] for r in range(len(matrix1)) if matrix1[r][col + 1] != 0}
                excluded_names.update(column_elements_right)
            
            # matrix에 남아있는 모든 이름 중 제외된 이름 제거
            valid_names = [name for name in element_counts.keys() if name not in excluded_names]
            
            if not valid_names:  # valid_names가 비어 있을 경우
                print(f"{col + 1}일차, {row + 1}번초: 부득이하게 연속 근무자 발생")
                
                # 이웃한 column에 있는 이름도 포함하도록 재설정
                excluded_names = set(number_to_names.get(col + 1, []))  # 초기화 후 다시 설정
                column_elements = {matrix1[r][col] for r in range(len(matrix1)) if matrix1[r][col] != 0}
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
                matrix1[row][col] = replacement_name
                element_counts[replacement_name] += 1
