print("Welcome to the frequency counter!")
print("This program counts the frequency of each word in a given text and tells you which word appears most frequently.")
text = input("Enter the text directly or type 'file' to read from a file: ").strip()
if text.lower() == 'file':
    filename = input("Enter the filename (with extension): ").strip()
    try:
        with open(filename, 'r') as file:
            text = file.read()
    except FileNotFoundError:
        print("File not found. Please check the filename and try again.")
        exit()
    words = text.split()
    frequency = {}
    for word in words:
        word = word.lower().strip('.,!?;"\'()[]{}')  # Normalize the word
        if word:
            frequency[word] = frequency.get(word, 0) + 1
    if frequency:
        most_frequent_word = max(frequency, key=frequency.get)
        print("\nWord Frequencies:")
        for word, count in frequency.items():
            print(f'"{word}": {count}')
        print(f'\nThe most frequent word is "{most_frequent_word}" which appears {frequency[most_frequent_word]} times.')
    else:
        print("No words found in the provided text.")
    save_option = input("Would you like to save the results to a file? (yes/no): ").strip().lower()
    if save_option == 'yes':
        output_filename = input("Enter the output filename (with extension): ").strip()
        try:
            with open(output_filename, 'w') as file:
                file.write("Word Frequencies:\n")
                for word, count in frequency.items():
                    file.write(f'"{word}": {count}\n')
                file.write(f'\nThe most frequent word is "{most_frequent_word}" which appears {frequency[most_frequent_word]} times.\n')
            print(f"Results saved to {output_filename}")
        except Exception as e:
            print(f"Error saving to file: {e}")
    else:
        print("Results not saved.")

elif text:  # If the user entered text directly
    words = text.split()
    frequency = {}
    for word in words:
        word = word.lower().strip('.,!?;"\'()[]{}')  # Normalize the word
        if word:
            frequency[word] = frequency.get(word, 0) + 1
    if frequency:
        most_frequent_word = max(frequency, key=frequency.get)
        print("\nWord Frequencies:")
        for word, count in frequency.items():
            print(f'"{word}": {count}')
        print(f'\nThe most frequent word is "{most_frequent_word}" which appears {frequency[most_frequent_word]} times.')
    else:
        print("No words found in the provided text.")
else:
    print("No input provided.")