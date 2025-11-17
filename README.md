# be17-fin-Halo-CoreBridge-AI


## 🚀 CoreBridge AI Pipeline


<img width="1542" height="665" alt="image" src="https://github.com/user-attachments/assets/ec6469a2-07e6-4eac-b1b9-9ccd5890b6c8" />

<br />

AI 기반 실시간 채용 매칭 시스템의 **전체 파이프라인을 직접 설계·구현·자동화·모니터링**한 프로젝트입니다. 이력서 텍스트를 입력받아 요약 → 스킬 추출 → 임베딩 → 벡터 검색 → 매칭 → LLM 스코어링 → DB 저장까지 **총 8단계의 End-To-End AI Workflow**를 n8n을 이용해 구축했습니다.


## 🎯 프로젝트 목표

- 채용 과정 중 서류 검토에 도움을 주어 서류 검토시간 단축
- LLM 기반 텍스트 이해 + 벡터 검색 기술로 JD-지원자 매칭 정확도 향상
- n8n을 이용해 파이프라인 자동화 및 오류 없는 흐름 구성
- Prometheus + Grafana 기반 실시간 성능 분석 및 병목 파악

## 🧠 전체 아키텍처 개요

<img width="1417" height="328" alt="image" src="https://github.com/user-attachments/assets/e0fcd78c-a3e3-4bbf-b7eb-c6e56a04a4bc" />

<br />

```
1단계: 웹훅 수신 재개(n8n) → 텍스트 추출 Resume Input (Webhook)
2단계: AI 요약 생성(FastAPI를 통한 Ollama LLM)
3단계: 스킬 추출(FastAPI를 통한 Ollama LLM)
4단계: 문장 임베딩(FastAPI + nomic-embed-text)
5단계: 벡터 스토리지(Redis with RediSearch)
6단계: JD 매칭(코사인 유사도기반 검색)
7단계: 후보 점수 매기기(LLM 기반 분석)
8단계: Spring boot를 통해 Mariadb에 저장(Spring Boot Backend & Mariadb)
```

## Swagger

- http://175.197.41.64:33398/docs

<img width="1447" height="838" alt="image" src="https://github.com/user-attachments/assets/a248608a-8511-47d4-92b7-ff649266dc88" />

<br />

<img width="1420" height="854" alt="image" src="https://github.com/user-attachments/assets/c3f46466-c7d7-46f3-b344-a91795972e58" />

<br />

## 🔄 파이프라인 단계별 설명


### 1️⃣ Resume Input (Webhook)
- n8n Webhook 트리거로 이력서 JSON 수신  
- 원본 텍스트 및 메타데이터 전처리

### 2️⃣ Summary Generation (LLM)
- FastAPI → Ollama LLM 호출  
- `llama3` 모델로 이력서 핵심 요약 생성  
- 평균 처리시간: 20~60초 (LLM 병목 구간)

### 3️⃣ Skill Extraction (LLM)
- LLM 기반 스킬 리스트 자동 추출  
- JSON 리스트 기반 데이터 구조화

### 4️⃣ Sentence Embedding
- nomic-embed-text 모델로 768-dim 벡터 생성  
- 처리시간 평균: 300~800ms

### 5️⃣ Vector Store (Redis Stack)
- RediSearch + HNSW 인덱스로 벡터 저장  
- 대규모 검색에 최적화된 구조

### 6️⃣ JD Matching
- Redis vector search로 JD와 cosine similarity 매칭  
- 처리속도: 1~10ms 수준

### 7️⃣ LLM Scoring
- 지원자 → JD 매칭 결과에 대한 LLM 재평가  
- 인과 기반 평가(why matched?)

### 8️⃣ Result Persistence (Spring Boot)
- 정제된 결과를 Spring Backend에 저장  
- 이후 관리자 대시보드에서 활용


## 📊 모니터링 & 관찰성 (Observability)
Prometheus + Pushgateway + Grafana로 AI Workflow 성능을 정량적으로 시각화했습니다.

[http://175.197.41.64:33377](http://175.197.41.64:33377/d/corebridge-n8n-pipeline-v1/-corebridge-n8n-ai-pipeline-dashboard?orgId=1&from=now-15m&to=now&timezone=browser&refresh=5s)

### 주요 지표
- `ai_workflow_total_processing_ms`  
- `ai_service_summary_latency_ms`  
- `ai_service_skills_latency_ms`  
- `ai_service_embedding_latency_ms`  
- `ai_service_redis_latency_ms`  
- `ai_service_match_latency_ms`  
- `ai_service_score_latency_ms`  

### Grafana 대시보드 주요 기능
- 전체 파이프라인 처리시간 실시간 확인  
- 단계별 병목 지점 한눈에 확인  

## 🧱 기술 스택

### 🏗️ Backend & API
- FastAPI  
- Spring Boot + JPA  
- Ollama LLM Runtime  
- nomic-embed-text (Embedding Model)

### 📦 Data & Vector DB
- Redis Stack  
- RediSearch (Vector Search)

### 🔄 Workflow Orchestration
- n8n  
- Webhook Trigger  
- JavaScript Function Nodes

### 🐋 Infrastructure
- Docker (자원이 한정되어 있었기(CPU 환경) 때문에 Kubernetes에 올리지 않았습니다)

### 📊 Observability
- Prometheus  
- Pushgateway  
- Grafana  

## 📈 성과 및 개선 효과
- 이력서 분석 작업 100% 자동화  
- JD 매칭 속도 50~300ms로 단축  
- LLM 병목 파악 후 개선 방향성 명확화  
- 서비스 장애 관찰성 확보  
- k8s 기반 확장성 있는 AI 서비스 운영 가능

