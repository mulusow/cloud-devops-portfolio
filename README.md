# cloud-devops-portfolio

A small web API that I build up into a full cloud DevOps project while learning:
containerized with Docker, tested and shipped with GitHub Actions, and deployed
to AWS with Terraform.

## Roadmap

| Stage | What gets added | Status |
| --- | --- | --- |
| Linux and Git | Flask API with `/health`, worked on through pull requests | In progress |
| Docker | `Dockerfile` and `compose.yaml` with a database | Not started |
| AWS | Image in ECR, running on ECS Fargate behind a load balancer | Not started |
| CI/CD | GitHub Actions: test and build on every PR, deploy on merge | Not started |
| Terraform | All AWS infrastructure defined as code | Not started |

## Repo layout

```
app/                 Flask API and its tests
notes/               weekly learning log
.github/workflows/   CI/CD pipelines (later)
terraform/           AWS infrastructure as code (later)
```

## Run it locally

```bash
cd app
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py            # then open http://localhost:5000/health
python -m pytest         # run the tests
```

## Learning log

I keep a short note each week in [`notes/`](notes/): what I did, what broke,
and how I fixed it.
