import sys

def calculate_score(file_name):
    # Your logic to calculate the score for the file
    # Currently, it assigns a score of 10 to every program
    score = 10
    return score

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python calculate_score.py <file_name>")
        sys.exit(1)
    
    file_name = sys.argv[1]
    score = calculate_score(file_name)
    print(f"The score for {file_name} is {score}")
