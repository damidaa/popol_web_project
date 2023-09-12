from django.db import models

class Post(models.Model):
    title = models.CharField('포스트 제목',max_length=100)
    content = models.TextField('포스트 내용')
    thumbnail = models.ImageField('썸네일 이미지', upload_to='post', blank=True)
    link_url = models.URLField('이미지 링크 URL', blank=True)  # 이미지의 링크 URL을 저장하는 필드

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE) #on_~ , ~할때로 생각
    content = models.TextField('댓글 내용')

    def __str__(self):
        return f"{self.post.title}의 댓글 (ID: {self.id})"


# Create your models here.
