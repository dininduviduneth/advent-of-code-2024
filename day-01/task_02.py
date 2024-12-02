from collections import Counter

def read_data_from_file(file_path):
    left_list = []
    right_list = []
    
    with open(file_path, 'r') as file:
        for line in file:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)
    
    return left_list, right_list

def calculate_similarity_score(left_list, right_list):
    # Count occurrences of each number in the right list
    right_count = Counter(right_list)
    
    # Calculate the similarity score
    similarity_score = sum(left * right_count[left] for left in left_list)
    
    return similarity_score

def main():
    file_path = 'data.txt'
    left_list, right_list = read_data_from_file(file_path)
    similarity_score = calculate_similarity_score(left_list, right_list)
    print(f"The similarity score between the lists is: {similarity_score}")

if __name__ == "__main__":
    main()