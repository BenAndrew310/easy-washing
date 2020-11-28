from flask import Flask,render_template,url_for,jsonify,flash,redirect,request
from flask_login import login_user, current_user, logout_user, login_required
from MANSYS import app, bcrypt
# from APS_Pocket.registration import Login
# from APS_Pocket.search_bar import SearchBar, Search
from MANSYS.models import User, Server1, Server2, Server3, Server4

