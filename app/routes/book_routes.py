from flask import Blueprint, abort, make_response

books_bp = Blueprint("books_bp", __name__, url_prefix="/books")
