import database_library


def search_database(search_input):
    # Connect to the file database and retrieve the data
    data = database_library.fetch_data()

    # Initialize variables to store the matching results and matching words
    matching_results = 0
    matching_words = 0

    # Search through the data to find any rows that contain the search input in any of the columns
    for row in data:
        for column in row:
            if search_input in column:
                # If a match is found, increment the matching results and matching words
                matching_results += 1
                matching_words += len(search_input.split())

    # Return the total number of matching results and matching words
    return (matching_results, matching_words)


# Accept a search input from the user
search_input = input("Please enter your search query: ")

# Search the database for the search input
(matching_results, matching_words) = search_database(search_input)

# Print the results
print("Matching results: ", matching_results)
print("Matching words: ", matching_words)
