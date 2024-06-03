class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if len(name) == 0:
            raise ValueError("Name must be longer than 0 characters.")
        
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name
    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        self._articles.append(new_article)
        return new_article

    def topic_areas(self):
        if not self._articles:
            return None
        return list(set(magazine.category for magazine in self.magazines()))
class Magazine:
    all = []
    def __init__(self, name, category):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        elif not 2 <= len(name) <= 16:
            raise ValueError("Name must be between 2 and 16 characters, inclusive.")
        else:
            self._name = name

        if not isinstance(category, str):
            raise TypeError("Category must be a string.")
        elif not len(category)>0:
            raise ValueError("Category must be a non-empty string.")
        else:
            self._category = category
        Magazine.all.append(self)
        self._articles = []


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("Name must be a string.")
        elif not 2 <= len(new_name) <= 16:
            raise ValueError("Name must be between 2 and 16 characters, inclusive.")
        else:
            self._name = new_name
            
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if not isinstance(new_category, str):
            raise TypeError("Category must be a string.")
        if len(new_category) ==0:
            raise ValueError("Category must not be empty")
        else:
            self._category = new_category

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))
    def add_article(self, author, title):
        new_article = Article(author, self, title)
        self._articles.append(new_article)
        return new_article
    def top_contributor(self):
        if not self._articles:
            return None
        return max(self._articles, key=lambda article: len(article.author.articles()))
    
    def article_titles(self):
        if not self._articles:
            return None
        else:
            return [article.title for article in self._articles]

    def contributing_authors(self):
        author_counts = {}
        for article in self._articles:
            if article.author in author_counts:
                author_counts[article.author] += 1
            else:
                author_counts[article.author] = 1
        contributing_authors = [author for author, count in author_counts.items() if count > 2]
        return contributing_authors if contributing_authors else None

    @classmethod
    def top_publisher(cls):
        if not cls.all:
            return None
        return max(cls.all, key=lambda mag: len(mag.articles()))
    
class Article:
    all = []
    def __init__(self, author, magazine, title):
        if isinstance(author, Author):
            self._author = author
        else:
            raise ValueError("Author must be an instance of Author.")
        if isinstance(magazine, Magazine):
            self._magazine = magazine
        else:
            raise ValueError("Magazine must be an instance of Magazine.")
        if not isinstance(title, str):
            raise TypeError("Title must be a string.")
        if not 5 <= len(title) <= 50:
            raise ValueError("Title must be a string between 5 and 50 characters.")
        else:
            self._title = title
        magazine._articles.append(self)
        author._articles.append(self)
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine
