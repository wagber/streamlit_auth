#Arquivo responsável pela conexão com meu banco de dados
import psycopg2
import os
from dotenv import load_dotenv
from contextlib import contextmanager

