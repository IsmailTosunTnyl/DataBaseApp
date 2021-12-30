import urllib.parse as up
import psycopg2


def get_field_names(cur):
    return [i[0] for i in cur.description]


class Database:
    def __init__(self, url):
        up.uses_netloc.append("postgres")
        self.url = up.urlparse(url)
        self.conn = psycopg2.connect(database=self.url.path[1:],
                                     user=self.url.username,
                                     password=self.url.password,
                                     host=self.url.hostname,
                                     port=self.url.port
                                     )
        self.cur = self.conn.cursor()
        self.predefined_queries = ["select * from movies where rating >6;",
                                   "select * from director natural join movies_director natural join movies;",
                                   "select * from customer where active = true;",
                                   "select movies.title, awards.award_name from awards natural join movie_awards natural join movies;",
                                   "select distinct * from genres;",
                                   "select customer.name as customer_name, rating.rating as customer_rate, movies.title as movie_title from customer join rating using (customer_id) join movies using (movie_id);",
                                   "select * from actors join movie_actors using (actor_id) join movies using (movie_id);",
                                   "select * from genres join movie_genres using (genre_id) join movies using (movie_id) where genre_name = 'Comedy';",
                                   "select movies.title, awards.award_name from awards join movie_awards using (award_id) join movies using (movie_id) where award_name = 'Altın Portakal';",
                                   "select actors.name as actor_name, movies.title as movie_title, customer.name as customer_name, rating.rating as customer_rate from customer join rating using (customer_id) join movies using (movie_id) join movie_actors using (movie_id) join actors using (actor_id) where actors.name = 'Bee';"]

    def select_all(self, table_name):
        query = f"SELECT * from {table_name};"
        self.cur.execute(query)
        field_names = get_field_names(self.cur)

        return self.cur.fetchall(), field_names, query

    def execute_query(self, query):
        self.cur.execute(query)
        field_names = get_field_names(self.cur)

        return [self.cur.fetchall(), field_names, query]

if __name__=='__main__':
    pass