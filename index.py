from collections import Counter
import random

rows_to_check = [1,2,5,6]
rows_not_to_check = [0,3,4,7]

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

matrix1 = [
    ['곽동준', '정명훈', '이다준', '김주완', '이선우', '박영선', '박성빈', '김성수', '김종수', '정시원', '박근태', '홍정표', '박영선', '이성빈', 0, 0, 0, 0, 0, 0],
    ['강명진', '유송완', '이선우', '정명훈', '서준호', '김경일', '윤민준', '유제상', '정명훈', '윤민준', '서준호', '박성빈', '강명진', 0, 0, '이성빈', 0, 0, 0, 0],
    ['전승원', '김주완', '심재학', '박영선', '정시원', '홍정표', '유송완', '윤찬우', '곽동준', '홍정표', '김성수', '김주완', '정명진', 0, 0, 0, 0, '이성빈', 0, 0],
    ['이다준', '박영선', '정명진', '유송완', '박성빈', '정명훈', '김주완', '홍정표', '조규민', '곽동준', '이다준', '김경일', '김종수', 0, 0, 0, 0, 0, 0, '이성빈']
]

matrix2 = [
    ['서준호', '송승우', '김경일', '전승원', '조규민', '강명진', '심재학', '한경진', '김태영', '이선우', '유제상', '이성빈', '서준호', 0, 0, 0, 0, 0, 0, 0],
    ['정명진', '박근태', '박성빈', '김성수', '이다준', '곽동준', '김종수', '김경일', '송승우', '강명진', '한경진', '전승원', '이선우', 0, 0, 0, 0, 0, 0, 0],
    ['한경진', '김태영', '조규민', '유제상', '윤찬우', '송승우', '조규민', '박근태', '이다준', '박영선', '김종수', '김태영', '정시원', 0, 0, 0, 0, 0, 0, 0],
    ['김종수', '유제상', '한경진', '송승우', '심재학', '전승원', '김태영', '강명진', '박성빈', '김경일', '조규민', '곽동준', '송승우', 0, 0, 0, 0, 0, 0, 0]
]

matrix = matrix1 + matrix2

name_ranges = {
    "김동범": range(1, 6),
    "조석연": range(14, 19),
    "서준호": range(14, 19),
    "윤민준": range(1, 5),
    "김성수": range(14, 19),
    "전승원": range(14, 19)
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


for row in matrix1:
    print(row)
    


print("여기부터 통합")
for row in matrix:
    print(row)
    
flattened_matrix = [element for row in matrix for element in row if element != 0]
element_counts = Counter(flattened_matrix)

print(element_counts)

for col in range(len(matrix[0])):  # 각 column에 대해 반복
    for row in range(len(matrix)) :  # 2, 3, 4, 5번 row에 대해 반복
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
                
for col in range(len(matrix[0])):  # 각 column에 대해 반복
    for row in range(len(matrix)) :  # 2, 3, 4, 5번 row에 대해 반복
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
                
                
                
                
print("투입 결과")           
for row in matrix:
    print(row)
    
flattened_matrix = [element for row in matrix for element in row if element != 0]
element_counts = Counter(flattened_matrix)

print(element_counts)

print("2,3번초 근무 횟수는 다음과 같습니다")
count_elements_in_rows(matrix, rows_to_check)