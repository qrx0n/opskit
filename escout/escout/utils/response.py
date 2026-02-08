from escout.utils.session import session


def response(url):
    session_ = session()
    
    response = session_.get(url)
    response.html.render()

    return response
