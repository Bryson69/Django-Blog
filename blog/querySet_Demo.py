# Import Post & User model 
from blog.models import Post
from django.contrib.auth.models import User

# Returns all users from post table
User.objects.all()

# Returns first user from post table
User.objects.first()

# Returns last user from post table
User.objects.last()

# Filter
User.objects.filter(username='testUser').first()
# Returns --> <QuerySet [<User: testUser>]>

# User  in a variable
user = User.objects.filter(username='testUser').first()

# Access the variable
user
# Returns --> Name of first User 

# Attributes of user
# Return --> 1
user.id
# Returns --> 1
user.pk

# we get the firsr user by id=1 if id=2 thats a different user
user = User.objects.get(id=1)



# Create a post 

# First checking whether there are any posts
Post.objects.all()

# if there are none there will be an empty query set --> <QuerySet []>

# Creating a post
post_1 = Post(title='Blog 1', content='First Post Content!', author='user')

# Save the post
post_1.save()

# query the post table again
Post.objects.all()
# This should be the output if  yoiu dont have a dunder str  method<QuerySet [<Post: Post object (1)>]>


# Once we have the dunder str method in our models.py 
# re run the shelll command and import Post and User model
# then query the post objects
# the query should look like this
# --> <QuerySet [<Post: Blog 1>]>

# Add another post

user = User.objects.filter(username='testUser').first()
user

# we can use user.id 
post_2 = Post(title='BLog 2', content='Second Post Content', author_id=user.id)

# Save second post
post_2.save()

# Query the posts
Post.objects.all()
# --> <QuerySet [<Post: Blog 1>, <Post: Blog 2>]>


# 'First Post Content!'
post = Post.object.first()


# name of author
post.author()

# email of author
post.author.email()

# get the post of a particular user
user.post_set.all()

# create a post using post set
user.post_set.create(title='BLog 3', content='Third Post Content')

# now the above post belongs to the user --> testUser