# Importing modules
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# List Comprehension is used to get the .txt files from the current directory
student_files = [doc for doc in os.listdir() if doc.endswith('.txt')]      #Ex : ['fatma.txt', 'john.txt', 'juma.txt']


#Opening the files
student_notes =[open(File).read() for File in  student_files]

# lambda function to transform txt file into array format
vectorize = lambda Text: TfidfVectorizer().fit_transform(Text).toarray()

# lambda function to check the similarity between them using cosine Similarity 
similarity = lambda doc1, doc2: cosine_similarity([doc1, doc2])

vectors = vectorize(student_notes)
s_vectors = list(zip(student_files, vectors))

# Defining set()
plagiarism_results = set()

# This function is like main function to find the palagirism

def check_plagiarism():
    global s_vectors
    for student_a, text_vector_a in s_vectors:
        # creating new vectors
        new_vectors =s_vectors.copy()

        # Gives the current index of the array file
        current_index = new_vectors.index((student_a, text_vector_a))

        # Deleting the current index new_vector element
        del new_vectors[current_index]
        for student_b , text_vector_b in new_vectors:
            # Calculating the score
            sim_score = similarity(text_vector_a, text_vector_b)[0][1]
            student_pair = sorted((student_a, student_b))

            # Assigning the data as set
            score = (student_pair[0], student_pair[1],sim_score)

            # Adding the score to the set
            plagiarism_results.add(score)
    return plagiarism_results


# Loop 
for data in check_plagiarism():
    print("File name\tChecking with\tScore [0 to 100]",end="\n")
    a = format(data[2] * 100,'.2f')
    print(data[0],"\t",data[1],"\t",a,"%",end="\n\n")
