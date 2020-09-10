from sklearn import feature_extraction
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics.pairwise import linear_kernel


def calc_similarities(restaurant_menus):
    # form vector for each resturant
    vectorizer = CountVectorizer(stop_words='english')
    X = vectorizer.fit_transform(restaurant_menus)

    print(vectorizer.get_feature_names())
    # tf-idf on resturant menue matrix
    transformer = TfidfTransformer()
    tfidf = transformer.fit_transform(X)
    tfidf_array = tfidf.toarray()

    # calculate similarity with first resturant using cosine_similarity
    target = tfidf_array[0]
    similarities = linear_kernel([target], tfidf_array)

    return similarities


def rank_similarities(similarities, restaurant_ids):
    # form pairs of similarity-id, and find most similar restaurants
    similairties_ids = []
    similairties_array = similarities[0]

    for i in range(len(restaurant_ids)):
        similarity = similairties_array[i]
        id = restaurant_ids[i]
        # construct tuple with similarity first
        similairty_id = (similarity, id)
        similairties_ids.append(similairty_id)

    similairties_ids.sort(reverse=True)

    return similairties_ids
