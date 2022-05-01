#  MIT License
#
#  Copyright (c) 2022 Mathieu Imfeld
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

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from mrmat_python_api_fastapi.db import get_db
from .db import Resource
from .schema import ResourceSchema

router = APIRouter()


@router.get('/',
            name='list_resources',
            summary='List all known resources',
            description='Returns all currently known resources and their metadata',
            response_model=list[ResourceSchema])
async def get_all(db: Session = Depends(get_db)):
    resources = db.query(Resource).all()
    return resources


@router.get('/{resource_id}',
            name='get_resource',
            summary='Get a single resource',
            description='Return a single resource identified by its resource id')
async def get(resource_id: int):
    pass


@router.post('/',
             name='create_resource',
             summary='Create a resource',
             description='Create a resource owned by the authenticated user')
async def create():
    pass


@router.put('/{resource_id}',
            name='modify_resource',
            summary='Modify a resource',
            description='Modify a resource by its resource id')
async def modify(resource_id: int):
    pass


@router.delete('/{resource_id}',
               name='remove_resource',
               summary='Remove a resource',
               description='Remove a resource by its resource id')
async def remove(resource_id: int):
    pass
