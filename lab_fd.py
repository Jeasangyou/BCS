from collections import Counter
import random

columns_to_check = [4, 5, 11, 12]
# 행렬 초기화
matrix = []

# 위 2행은 0으로 채움
for _ in range(2):
    matrix.append([0] * 14)

# 아래 2행은 1로 채움
for _ in range(2):
    matrix.append([1] * 14)

print(matrix)

names = ["김종수", "이선우", "서준호", "윤민준", "한경진", 
         "정시원", "김경일", "홍정표", "이다준", "김주완", 
         "조규민", "김태영", "유송완", "송승우", "전승원",
         "윤찬우", "박성빈"]

name_ranges = {
    "김종수": range(7, 12),
    "서준호": range(1, 5),
    "윤민준": range(2, 5),
    "홍정표": range(5, 12),
    "김태만": list(range(1, 3)) + list(range(7, 12)),
    "이다준": list(range(1, 3)),
    "김주완": range(2, 4),
    "조규민": range(7, 12),
    "정명진": range(1, 5),
    "이현준": range(1, 5),
    "권태완": range(1, 4)
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

names = ["김종수", "이선우", "서준호", "윤민준", "한경진", 
         "정시원", "김경일", "홍정표", "이다준", "김주완", 
         "조규민", "김태영", "유송완", "송승우", "전승원",
         "윤찬우", "박성빈"]


for name in names:
    if name not in element_counts:
        element_counts[name] = 0
        
for col in columns_to_check:  # 각 column에 대해 반복
    for row in range(len(matrix)):  # 각 row에 대해 반복
        if matrix[row][col] == 1:  # 0인 경우
            # 해당 column의 numbers_to_names에 있는 이름 제외
            excluded_names = set(number_to_names.get(col + 1, []))
            
            # 해당 column의 0이 아닌 요소 제외
            column_elements = {matrix[r][col] for r in range(len(matrix)) if matrix[r][col] != 1 and matrix[r][col] != 0}
            excluded_names.update(column_elements)
            
            # 이웃한 column의 요소들도 제외
            if col > 0:  # 왼쪽 이웃 column 확인
                column_elements_left = {matrix[r][col - 1] for r in range(len(matrix)) if matrix[r][col] != 1 and matrix[r][col] != 0}
                excluded_names.update(column_elements_left)
            if col < len(matrix[0]) - 1:  # 오른쪽 이웃 column 확인
                column_elements_right = {matrix[r][col + 1] for r in range(len(matrix)) if matrix[r][col] != 1 and matrix[r][col] != 0}
                excluded_names.update(column_elements_right)
            
            # matrix에 남아있는 모든 이름 중 제외된 이름 제거
            valid_names = [name for name in element_counts.keys() if name not in excluded_names]
            
            if not valid_names:  # valid_names가 비어 있을 경우
                print(f"{col + 1}일차, {row + 1}번초: 부득이하게 연속 근무자 발생")
                
                # 이웃한 column에 있는 이름도 포함하도록 재설정
                excluded_names = set(number_to_names.get(col + 1, []))  # 초기화 후 다시 설정
                column_elements = {matrix[r][col] for r in range(len(matrix)) if matrix[r][col] != 1 and matrix[r][col] != 0}
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
                print(replacement_name)
                
                # 0을 대체하고, 개수 업데이트
                print(row)
                print(col)
                matrix[row][col] = replacement_name
                element_counts[replacement_name] += 1

                
print(matrix)