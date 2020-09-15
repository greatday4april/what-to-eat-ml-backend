
# %%
# from sklearn import feature_extraction
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics.pairwise import linear_kernel


def calc_similarities(restaurant_menus):
    """Calculate similarities with taget restaurant from description of restaurants.

    Args:
            Target restaurant is the first one.

    Returns:
        similairites (list): list of cosine-similarity (int) comapred with target restaurant.
            Ranging from 0 to 1, with higher value stands for more similarity.
            The first item will always be 1.
    """
    # pre process and form key word vector for each resturant
    vectorizer = CountVectorizer(stop_words='english')
    clean_restaurant_menus = remove_numbers(restaurant_menus)
    X = vectorizer.fit_transform(clean_restaurant_menus)

    # tf-idf on resturant menue matrix
    transformer = TfidfTransformer()
    tfidf = transformer.fit_transform(X)
    tfidf_array = tfidf.toarray()

    # calculate similarity with first resturant using cosine_similarity
    target = tfidf_array[0]
    similarities = linear_kernel([target], tfidf_array)

    return similarities


def rank_similarities(similarities, restaurant_ids):
    """Combine similarities list with respective restaurant_ids, and rank them by similarity.

    Args:
        similarities (list): cosine similarities compared with target (first) restaurant
        restaurant_ids (list): restaurant_ids corresponding to similarities.

    Returns:
        similarities_ids (list): list of (similarity, id) tuple ranked by similarity.
    """
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


def remove_numbers(restaurant_menus):
    """Remove all words containing numbers / not alpha.

    Args:
        restaurant_menus (list): list of string represent each restaurtant.

    Returns:
        output (list): list of string with non-alphabet words deleted.
    """
    output = []
    for menu in restaurant_menus:
        clean_menu = ""
        for word in menu.split():
            if word.isalpha():
                clean_menu += " " + word
        output.append(clean_menu)
    return output


def main():
    corpus = [
        "aaa bbb b12 ccc",
        "ccc ddd e43",
        "aaa ccc ddd bbb bbb",
        "bbb bbb ddd aaa e43"
    ]
    ids = [1, 2, 3, 4]
    similairites = calc_similarities(corpus)
    print(rank_similarities(similairites, ids))


if __name__ == '__main__':
    main()
