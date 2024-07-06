FROM python:3.10-slim

WORKDIR /practics2024_finish_1
COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . /practics2024_finish_1

CMD ["python", "bot/CareerPath_Bot.py"]