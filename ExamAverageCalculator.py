

# Define the totalPrice function that calculates and returns the average score
def totalPrice(num_students):
    total_score = 0  # Initialize total score to 0

    # Loop through each student and ask for their exam score
    for i in range(1, num_students + 1):
        score = float(input(f"Enter the exam score for student {i}: "))
        total_score += score  # Add the student's score to the total

    average_score = total_score / num_students  # Calculate the average score
    return average_score  # Return the average score

def main():
    num_students = 5  # Number of students for which to calculate the average score
    
    # Call the totalPrice function and store the result in avg_score
    avg_score = totalPrice(num_students)
    
    # Print the average score
    print(f"The average exam score for {num_students} students is: {avg_score}")

if __name__ == "__main__":
    main()
