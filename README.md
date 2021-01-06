# Plagiarism Checker

_This is Simple project for checking plagiarism of text documents using cosine similarity_

_Cosine Similarity_:
```
    Cosine similarity is a measure of similarity between two non-zero vectors of an inner product space that measures the cosine of the angle between them.
```
```
On Demo we have used three textfiles on the
same directory with app.py , once we run the app
it will open all textfile and tries to find the
similarities between them by using cosine similarity 
```

```
I used TfidfVectorizer to convert text to vectors so as
I can compute the cosine similarity
```

```
from sklearn.feature_extraction.text import TfidfVectorizer
```

```
I used scikit-learn to computer the cosine similarity
```

```
from sklearn.metrics.pairwise import cosine_similarity
```

```
Run the file using below command
```
```
python3 app.py
```

