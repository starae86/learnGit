import orm
from Model import User, Blog, Comment
import asyncio

def test(loop):
    yield from orm.create_pool(loop=loop,user='root', password='1657', database='webapp')

    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

    yield from u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()
# for x in test():
#     pass