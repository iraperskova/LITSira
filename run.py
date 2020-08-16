from aiohttp import web

BOOKS = [{
  'id': 1,
  'title': 'Test book 1',
  'description': 'Test book 1 description'
}, {
  'id': 2,
  'title': 'Test book 1',
  'description': 'Test book 1 description'
}, {
  'id': 3,
  'title': 'Test book 1',
  'description': 'Test book 1 description'
}]

routes=web.RouteTableDef()

def find_book(book_id):
    books=list(filter(lambda b: b['id']==book_id, BOOKS))

    try:
        return books[0]
    except IndexError:
        return None     

@routes.get('/books')
async def books_list(request):
    return web.json_response(BOOKS)

@routes.get('/books/{id}')
async def books_details(request):
    book_id=int(request.match_info.get('id'))
    book=find_book(book_id)
    return web.json_response(book)


app=web.Application()
app.router.add_routes(routes)

web.run_app(app)
