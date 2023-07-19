import dotenv
import pydantic


class ProjectConfig(pydantic.BaseSettings):
    """
    A project config class to store all project specific settings
    to be used both in tests and core part of the framework,
    like model, data, utils, etc. – i.e. serves as cross-cutting concern.
    Normally to be stored in a separate file.
    """

    admin_login: str
    admin_pwd: str

project_config = ProjectConfig(dotenv.find_dotenv())
