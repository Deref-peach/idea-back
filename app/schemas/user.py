from typing import Optional
import strawberry as stb

@stb.input
class CreateUser:
    password: str
    username: str
    fullname: str
    email: str
    resume: Optional[str]
    skills: Optional[list[dict[str, str]]]
    # TODO:  upload avatar stb.file_uploads.Upload
