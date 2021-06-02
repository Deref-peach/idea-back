from typing import Optional
import strawberry as stb

@stb.input
class CreateUser:
    hashed_password: str
    username: str
    fullname: str
    email: str
    resume: Optional[str]
    skills: Optional[list[dict[str, str]]]
    # TODO:  upload avatar stb.file_uploads.Upload


@stb.input
class UpdateUser:
    hashed_password: str
    username: str
    fullname: str
    email: str
    resume: Optional[str]
    skills: Optional[list[dict[str, str]]]
    # TODO:  upload avatar stb.file_uploads.Upload

@stb.input
class DeleteUser:
    hashed_password: str
    username: str
    email: str
