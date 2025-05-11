from flask import Blueprint, abort, make_response, request, Response
from app.models.book import Book
from ..db import db
from .route_utilities import validate_model, create_model, get_models_with_filters

bp = Blueprint("books_bp", __name__, url_prefix="/books")

@bp.post("")
def create_book():
    request_body = request.get_json()
    return create_model(Book, request_body)
    # try: 
    #     new_book = Book.from_dict(request_body)
    
        
    # except KeyError as error:
    #     response = {"message": f"Invalid request: missing {error.args[0]}"}
    #     abort(make_response(response, 400))
        
    # db.session.add(new_book)
    # db.session.commit()

    # return new_book.to_dict(), 201

@bp.get("")
def get_all_books():
    return get_models_with_filters(Book, request.args)
    # query = db.select(Book)

    # title_param = request.args.get("title")
    # if title_param:
    #     query = query.where(Book.title.ilike(f"%{title_param}%"))
    
    # description_param = request.args.get("description")
    # if description_param:
    #     query = query.where(Book.description.ilike(f"%{description_param}%"))
    # query = query.order_by(Book.id)
    # books = db.session.scalars(query)

    # books_response = []
    # for book in books:
    #     books_response.append(book.to_dict())
    # return books_response

@bp.get("/<book_id>")
def get_one_book(book_id):
    book = validate_model(Book, book_id)

    return book.to_dict()

@bp.put("/<book_id>")
def update_book(book_id):
    book = validate_model(Book, book_id)
    request_body = request.get_json()

    book.title = request_body["title"]
    book.description = request_body["description"]
    db.session.commit()

    # return Response(status=204, mimetype="application/json") # causing errors with new test?
    return {"message":f"Book #{book.id} successfully updated"}, 200

@bp.delete("/<book_id>")
def delete_book(book_id):
    book = validate_model(Book, book_id)
    db.session.delete(book)
    db.session.commit()

    # return Response(status=204, mimetype="application/json")
    return make_response({"message":f"Book #{book.id} successfully deleted"}, 200)