from django.test import TestCase
from .models import Location,Profile,Post,Comment
from django.contrib.auth.models import User

# Create your tests here.
class LocationTestClass(TestCase):
    def setUp(self):
        self.place = Location(location='Moringa')

    def test_instance(self):
        self.assertTrue(isinstance(self.place,Location))

    def tearDown(self):
        Location.objects.all().delete()

    def test_save_method(self):
        self.place.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)

    def test_delete_method(self):
        self.place.delete_location('Moringa')
        locations = Location.objects.all()
        self.assertTrue(len(locations)==0)

class CommentTestClass(TestCase):
    def setUp(self):
        self.new_user = User.objects.create_user(username='thomas',password='nstgrmtoto29')
        self.comment = Comment(comment='Test Comment',username=self.new_user,post=1)

    def test_instance(self):
        self.assertTrue(isinstance(self.comment,Comment))

    def tearDown(self):
        Comment.objects.all().delete()

    def test_save_method(self):
        self.comment.save_comment()
        comments = Comment.objects.all()
        self.assertTrue(len(comments)>0)

    
