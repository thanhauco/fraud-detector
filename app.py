from flask import Flask, request, jsonify
from prometheus_client import generate_latest
import os
import pickle
from src.models import Transaction
from src.rules import RuleEngine
from src.db import init_db, get_db
from src.metrics import FRAUD_DETECTED, TX_PROCESSED

app = Flask(__name__)
# ... rest of app