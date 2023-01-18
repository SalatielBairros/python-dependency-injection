from pydantic import BaseModel, validator

class LogRequest(BaseModel):    
    text: str
    
    @validator('text')
    def text_must_be_valid(cls, v: str):
        if v is None:
            raise ValueError('text must be informed')
        v = v.strip().lower()
        if len(v) < 1:
            raise ValueError('text must be valid')
        if(len(v.split(" ")) < 2):
            raise ValueError('text must have at least 2 words')
        
        return v