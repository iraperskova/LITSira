from aiohttp import web



routes=web.RouteTableDef()

@routes.get('/books')
async def books_list(request):
    return web.Response(text="books")

app=web.Application()
app.router.add_routes(routes)

web.run_app(app)
