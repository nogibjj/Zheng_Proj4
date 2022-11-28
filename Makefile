install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black *.py

lint:
	pylint --disable=R,C *.py

deploy:
	aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws/i6h0i6s9
	docker build -t zheng-zhang .
	docker tag zheng-zhang:latest public.ecr.aws/i6h0i6s9/zheng-zhang:latest
	docker push public.ecr.aws/i6h0i6s9/zheng-zhang:latest

all: install format lint deploy