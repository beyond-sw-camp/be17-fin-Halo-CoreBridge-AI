<h1 align="center">
    <img src="https://github.com/beyond-sw-camp/be17-fin-Halo-CoreBridge-BE/raw/dev/docs/assets/imgs/CoreBridge-icon.png" alt="CoreBridge 아이콘" width="30" height="30">
    CoreBridge
</h1>

<p align="center">
  <img src="https://github.com/beyond-sw-camp/be17-fin-Halo-CoreBridge-BE/raw/dev/docs/assets/imgs/CoreBridge-logo.png"  alt="CoreBridge 로고" height="500" />

  

<h3 align="center">3팀 - Halo</h3>

<br /><br />

# 👨‍💻 팀원 구성
<div align=center>
<table>
  <tr>
    <td>
      <a href="https://github.com/lesw1216">
        <img src="https://avatars.githubusercontent.com/u/96828250?v=4" width="150" style="max-width: 100%;">
      </a>
    </td>
    <td>
      <a href="https://github.com/atimaby28">
        <img src="https://avatars.githubusercontent.com/u/149382180?v=4" width="150" style="max-width: 100%;">
      </a>
    </td>
    <td>
      <a href="https://github.com/Hanryang-Kim">
        <img src="https://avatars.githubusercontent.com/u/214753184?v=4" width="150" style="max-width: 100%;">
      </a>
    </td>
    <td>
      <a href="https://github.com/junsun-yeam">
        <img src="https://avatars.githubusercontent.com/u/210853817?v=4" width="150" style="max-width: 100%;">
      </a>
    </td>
    <td>
      <a href="https://avatars.githubusercontent.com/u/206636155?v=4">
        <img src="https://avatars.githubusercontent.com/u/206636155?v=4" width="150" style="max-width: 100%;">
      </a>
    </td>
  </tr>
  <tr>
    <td align="center">
      <a href="https://github.com/lesw1216">이상우</a>
    </td>
    <td align="center">
      <a href="https://github.com/atimaby28">양승우</a>
    </td>
    <td align="center">
      <a href="https://github.com/Hanryang-Kim">김륜환</a>
    </td>
    <td align="center">
      <a href="https://github.com/junsun-yeam">염준선</a>
    </td>
    <td align="center">
      <a href="https://github.com/young1042">김영재</a>
    </td>
  </tr>
</table>
</div>
<br><br>

---

# 배포 접속 주소

## 프론트 

* [www.core-bridge.co.kr](https://www.core-bridge.co.kr/jobs)

## 백엔드

* [api.core-bridge.co.kr](https://api.core-bridge.co.kr)


---

<br /><br />

## 🚀 CoreBridge AI Pipeline


<img width="1542" height="665" alt="image" src="https://github.com/user-attachments/assets/ec6469a2-07e6-4eac-b1b9-9ccd5890b6c8" />

<br /><br />

AI 기반 실시간 채용 매칭 시스템의 **전체 파이프라인을 직접 설계·구현·자동화·모니터링**한 프로젝트입니다. 이력서 텍스트를 입력받아 요약 → 스킬 추출 → 임베딩 → 벡터 검색 → 매칭 → LLM 스코어링 → DB 저장까지 **총 8단계의 End-To-End AI Workflow**를 n8n을 이용해 구축했습니다.

처음에는 `/spring/ai` 파일에 있는 java spring 코드처럼 AI server로 직접 트리거 하였으나, 점차 `/spring/personal` 코드를 활용해 자동화 파이프라인 구축을 위해 노코드(no-code)기반 n8n 오픈소스 워크플로우 자동화 도구와 통신하는 방법을 사용하였습니다.  

<br /><br />

![Animation10](https://github.com/user-attachments/assets/c03c15a1-7da4-4e82-a985-931e2901cbb8)



<br /><br />

## 🎯 프로젝트 목표

- 채용 과정 중 서류 검토에 도움을 주어 서류 검토시간 단축
- LLM 기반 텍스트 이해 + 벡터 검색 기술로 JD-지원자 매칭 정확도 향상
- n8n을 이용해 파이프라인 자동화 및 오류 없는 흐름 구성
- Prometheus + Grafana 기반 실시간 성능 분석 및 병목 파악

<br /><br />

## 🧠 전체 아키텍처 개요

<img width="1417" height="328" alt="image" src="https://github.com/user-attachments/assets/e0fcd78c-a3e3-4bbf-b7eb-c6e56a04a4bc" />

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

<br /><br />

## Swagger

- http://175.197.41.64:33398/docs

<img width="1447" height="838" alt="image" src="https://github.com/user-attachments/assets/a248608a-8511-47d4-92b7-ff649266dc88" />

<br /><br />

- Scoring 예시

<img width="1420" height="854" alt="image" src="https://github.com/user-attachments/assets/c3f46466-c7d7-46f3-b344-a91795972e58" />

<br /><br />

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
- 정제된 결과를 Spring Backend를 통해 MariaDB에 저장  
- 이후 관리자 대시보드에서 활용

- MariaDB에 저장

<img width="1807" height="748" alt="image" src="https://github.com/user-attachments/assets/943d02e1-1d31-43a9-8730-1fcb3c51a353" />

<br /><br />

## 📊 모니터링 (Observability)
Prometheus + Pushgateway + Grafana로 AI Workflow 성능을 정량적으로 시각화했습니다.

[http://175.197.41.64:33377](http://175.197.41.64:33377/d/corebridge-n8n-pipeline-v1/-corebridge-n8n-ai-pipeline-dashboard?orgId=1&from=now-15m&to=now&timezone=browser&refresh=5s)


### 주요 지표

<img width="1580" height="813" alt="1" src="https://github.com/user-attachments/assets/f4a0c992-0dea-457e-88db-ab1c82c3b32f" />

<img width="1584" height="824" alt="2" src="https://github.com/user-attachments/assets/b2cf231a-054f-4fc4-a46c-884ad9a2fe16" />


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

<br /><br />

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







