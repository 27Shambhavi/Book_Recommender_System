import pickle
import difflib

class BookRecommender:
    def __init__(self):
        # Load pickled data directly from project root
        self.books = pickle.load(open("books.pkl", "rb"))
        self.popular = pickle.load(open("popular.pkl", "rb"))
        self.pt = pickle.load(open("pt.pkl", "rb"))
        self.similarity_scores = pickle.load(open("similarity_scores.pkl", "rb"))

    def get_popular(self, n=10):
        """
        Return top n popular books from the popular.pkl file.
        """
        try:
            return self.popular.head(n).to_dict(orient="records")
        except Exception as e:
            print("Error loading popular books:", e)
            return []

    def recommend(self, book_title):
        # ✅ fuzzy match (case-insensitive, typo-tolerant)
        all_titles = self.pt.index.tolist()
        closest_matches = difflib.get_close_matches(book_title, all_titles, n=1, cutoff=0.6)

        if not closest_matches:
            return []

        # pick best match
        book_title = closest_matches[0]
        index = self.pt.index.get_loc(book_title)
        scores = list(enumerate(self.similarity_scores[index]))
        sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:6]  # top 5

        recommendations = []
        for i in sorted_scores:
            recommended_title = self.pt.index[i[0]]
            recommendations.append(recommended_title)

        return recommendations
