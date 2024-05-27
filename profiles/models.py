from djongo import models as djongo_models

class UserProfile(djongo_models.Model):
    _id = djongo_models.ObjectIdField(primary_key=True)
    name = djongo_models.CharField(max_length=100)
    email = djongo_models.EmailField(unique=True)
    bio = djongo_models.TextField(blank=True, null=True)
    created_at = djongo_models.DateTimeField(auto_now_add=True)
    updated_at = djongo_models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'profiles_userprofile'  # Specify the collection name in MongoDB
