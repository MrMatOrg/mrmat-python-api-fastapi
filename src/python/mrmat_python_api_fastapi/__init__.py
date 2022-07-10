#  MIT License
#
#  Copyright (c) 2022 MrMat
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

from .config import Config
app_config = Config.from_json_file()

from sqlalchemy.ext.declarative import declarative_base                     # pylint: disable=wrong-import-position
Base = declarative_base()

from mrmat_python_api_fastapi.apis.healthz import api_healthz               # pylint: disable=wrong-import-position
from mrmat_python_api_fastapi.apis.greeting.v1 import api_greeting_v1       # pylint: disable=wrong-import-position
from mrmat_python_api_fastapi.apis.greeting.v2 import api_greeting_v2       # pylint: disable=wrong-import-position
from mrmat_python_api_fastapi.apis.greeting.v3 import api_greeting_v3       # pylint: disable=wrong-import-position
from mrmat_python_api_fastapi.apis.resource.v1 import api_resource_v1       # pylint: disable=wrong-import-position


