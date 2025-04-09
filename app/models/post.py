class Post:
    def __init__(self, id, title, content, author, created_at, status, category, tags):
        self.id = id
        self.title = title
        self.content = content
        self.author = author
        self.created_at = created_at
        self.status = status
        self.category = category
        self.tags = tags

class PostModel:
    def __init__(self):
        self.posts = []
        self.next_id = 1

    def create(self, post):
        # Logic to create a new post in the database
        post = Post(self.title, self.content, self.author, self.created_at, self.status, self.category, self.tags)
        self.posts.append(post)
        self.next_id += 1
        return post
    
    def all(self):
        # Logic to retrieve all posts from the database
        return self.posts
    
    def find(self, post_id):
        # Logic to find a post by its ID
        for post in self.posts:
            if post.id == post_id:
                return post
        return None
    
    def update(self, post_id, title, content, author, status, category, tags):      
        # Logic to update a post in the database
        post = self.find(post_id)
        if post:
            post.title = title
            post.content = content
            post.author = author
            post.status = status
            post.category = category    
            post.tags = tags
            return post
        return None
    
    def delete(self, post_id):
        # Logic to delete a post from the database
        post = self.find(post_id)
        if post:
            self.posts.remove(post)
            return True
        return False
    
    def pubished(self):
        # Logic to retrieve all published posts from the database
        return [post for post in self.posts if post.status == 'published']