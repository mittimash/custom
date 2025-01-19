from tables import Users, Navigation, Posts

class Database():
    def __init__(self):
        self.users = Users
        self.users.create_table()
        self.posts = Posts
        self.posts.create_table()

    def create_user(self, username, password, email):
        try:
            is_username_in_base = self.users.select().where(self.users.username == username).get()
            if is_username_in_base:
                return False
        except:
            pass

        try:
            is_email_in_base = self.users.select().where(self.users.email == email).get()
            if is_email_in_base:
                return False
        except:
            pass

        self.users.create(
            username=username,
            password = password,
            email = email,
        )

    def get_user(self, user, password):
        try:
            ask = self.users.select().where(
                                            (self.users.username == user) &
                                            (self.users.password == password)
                                         ).get()
        except self.users.DoesNotExist:
            return False

        return True

    def create_post(self, username, title, content):
        self.posts.create(
            user=username,
            title=title,
            content=content
        )

    def get_posts(self, user):
        try:
            ask = self.posts.select().where(
                        (self.posts.user == user)
                        )
        except self.posts.DoesNotExist:
            return False

        res = []
        for i in ask:
            res.append({'title': i.title, 'content': i.content})

        return res