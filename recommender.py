from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.metrics.pairwise import linear_kernel
from utils.rakuten_menu_api_utils import get_menus

SIMARITY_THRETHOLD = 0.7


def get_similar_restaurant_ids(reference_restaurant_id, candidate_ids):
    vectorizer = CountVectorizer()
    candidate_ids.append(reference_restaurant_id)
    restaurant_menus = [
        [menu_item['menu_item_name'] for menu_item in get_menus(candidate_id)] for candidate_id in candidate_ids
    ]
    transformed = vectorizer.fit_transform(restaurant_menus)

    transformer = TfidfTransformer()
    tfidf = transformer.fit_transform(transformed)
    tfidf_array = tfidf.toarray()

    target = candidate_ids[-1]
    similarities = linear_kernel([target], tfidf_array)

    similarities_array = similarities[0]
    similarity_ids = [(similarities_array[idx], candidate_ids[idx])
                      for idx in range(len(candidate_ids)) if similarities_array[idx] >= SIMARITY_THRETHOLD]
    similarity_ids.sort(reverse=True)

    return [
        similarity[1] for similarity in similarity_ids if similarity[1] != reference_restaurant_id
    ]
