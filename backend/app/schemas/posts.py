''' Pydantic Objects for Posts '''

from pydantic import BaseModel

class PostBase(BaseModel):
    '''
    PostBase is the base object of all posts.

    It requires at least a title and text
    '''
    title: str
    content: str

class CreatePost(PostBase):
    '''
    Child object of PostBase to create posts.
    '''
    class Config:
        ''' enabling from_attributes to write/read from sqlalchemy '''
        from_attributes = True
