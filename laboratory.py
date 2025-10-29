#import numpy as np
from collections import Counter
import random
columns_to_check = [3,4, 5, 11, 12]
# 행렬 초기화
matrix = []

# 위 2행은 0으로 채움
matrix = [['윤종수', '정명훈', '채문기', '성연호', '권태완', '서동우', 0, '권태우', '마경군', '곽동준', '김민우', '김태만', '이현준', '김태만'],
         ['김태만', '권태완', '이상민', '마경군', '정명진', '박현빈', '이현준', '마경군', '윤종수', '심재학', '박현빈', '정명진', '권태완', '채문기'],
         ['이현준', '성연호', '김민우', '심재학', '김태만', '채문기', '윤종수', '권태완', '박현빈', '권태우', '채문기', '마경군', '이상민', '곽동준'],
         ['이상민', '마경군', '서동우', '박현빈', '권태우', '곽동준', '심재학', '김민우', '성연호', '이현준', '서동우', '심재학', '서동우', '윤종수']]


print(matrix)

names = ["정명진", "마경군", "이현준", "이상민", 
         "박현빈", "윤종수", "권태완", "곽동준",
         "심재학", "김태만", "김민우", "성연호",
         "채문기", "권태우"
         ]


name_ranges = {
    "윤민준": range(7, 13),
    "정시원": range(7, 13),
    "박근태": range(1, 2),
    "유제상": range(1, 4),
    "곽동준": range(1, 3),
    "성연호": range(12, 15),
    "서동우": range(1, 3),
    "유송완": range(7, 14),
    "정명훈": range(8, 12),
    "윤종수": range(2, 7),
    "송승우": range(1, 4)
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
element_counts["정명진"] = 999
print(element_counts)

names = ["정명진", "마경군", "이현준", "이상민", 
         "박현빈", "윤종수", "권태완", "곽동준",
         "심재학", "김태만", "김민우", "성연호",
         "채문기", "권태우"
         ]


for name in names:
    if name not in element_counts:
        element_counts[name] = 0
        

print("초기값")
print(element_counts)
        
for col in range(len(matrix[0])):  # 각 column에 대해 반복
    print("루프 시작")
    for row in range(len(matrix)):  # 각 row에 대해 반복
        print("루프 시작2")
        print(col)
        print(row)
        if matrix[row][col] == 0:  # 0인 경우
            print("0 발견")
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
            print("유효이름:")
            print(valid_names)
            
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
                
print("중간확인")

print(matrix)

flattened_matrix_final = [element for row in matrix for element in row]

# 2. 각 요소의 개수를 세기
element_counts_final = Counter(flattened_matrix_final)

# 3. 요소를 개수에 따라 내림차순으로 정렬
sorted_counts_final = sorted(element_counts_final.items(), key=lambda x: x[1], reverse=True)

print("근무자별 최종 근무 횟수 (내림차순 정렬):")
for element, count in sorted_counts_final:
    print(f"{element}: {count}회")
    
for row in matrix:
    print(row)