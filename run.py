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

@routes.get('/books')
async def books_list(request):
    return web.json_response(BOOKS)

app=web.Application()
app.router.add_routes(routes)

web.run_app(app)
