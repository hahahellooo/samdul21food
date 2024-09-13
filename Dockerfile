FROM python:3.11

WORKDIR /code

COPY src/samdul21food/main.py /code/
                                                    
RUN pip install --no-cache-dir --upgrade git+https://github.com/hahahellooo/samdul21food.git@0.1.0

# 모델 서빙을 위해 API 구동을 위한 FastAPI RUN
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"] 
