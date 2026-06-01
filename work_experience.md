# Work Experience — Walter Wang

## AI Engineer
**ZEIL** | Jul 2025 – Present

### Auto-apply project

**Summary:** Event-driven system that scrapes job application forms from multiple ATS (Applicant Tracking System) vendors (e.g. SmartRecruiter, Best Start / QJumpers quick-apply), maps form fields and options with AI, and auto-fills applications at scale. Multi-tenant pipeline: Pub/Sub triggers dispatchers, Cloud Tasks enqueue scrape/apply jobs, Cloud Run workers run headless browser automation and AI-driven form filling; results and job data live in GCS and internal APIs.

**Architecture & flow**
- **Event-driven pipeline:** Pub/Sub → dispatchers → Cloud Tasks (scraper + applier queues) → Cloud Run / Cloud Functions.
- **Multi-tenant:** Per-ATS scrapers and appliers with shared GCP infra (Cloud Tasks, Pub/Sub, GCS, Secret Manager).
- **Headless browser automation:** Scrape application forms, expand dynamic fields, map options, then fill via AI (Gemini) with structured outputs.

**Key components & techniques**

| Area | Techniques / tech | Effect |
|------|-------------------|--------|
| **Languages & runtime** | Python — scrapers, appliers, workers, serverless handlers | Single language across pipeline; easy maintenance and deployment. |
| **Web scraping & browser** | Selenium (headless Chrome, WebDriverWait, XPath/By), undetected-chromedriver, BeautifulSoup, lxml, webdriver-manager, requests | Reliable form discovery and anti-detection for ATS (e.g. SmartRecruiter); HTML/XML parsing and API calls. |
| **AI / LLM** | Pydantic-AI (agent framework), Google Gemini (e.g. gemini-2.5-flash), Google GLA provider, Pydantic models for WebElementList / ListOfFillActions | Typed form understanding, element mapping, and fill actions; consistent structured outputs. |
| **Data & validation** | Pydantic (request/response, agent outputs), jsonschema, Avro, CloudEvents | Valid event envelopes and schemas; fewer runtime errors and clear contracts. |
| **Google Cloud** | Cloud Functions (HTTP, functions-framework), Cloud Run (scraper/applier workers), Cloud Tasks (queues), Pub/Sub (push), GCS (JSON, CSV), Secret Manager, Cloud Logging | Scalable, event-driven execution; secure secrets; structured logs. |
| **Backend & APIs** | Flask, REST (internal Zen API, external ATS endpoints) | Simple HTTP handling in serverless; integration with user/job data and ATS. |
| **DevOps** | gcloud CLI, Bash (deploy.sh, permissions, topics), .gcloudignore, dotenv / env vars | Lean Cloud Function deploys; scripted IAM and topic setup; clear local vs cloud config. |
| **Concurrency** | concurrent.futures (ThreadPoolExecutor), asyncio / nest_asyncio | Parallel Pub/Sub publish and batch work; async where needed (e.g. agent/form filling). |
| **Other** | Pillow (images), Slack webhooks (job-comparison, missing-job alerts), OpenTelemetry (tracing), CSV batch job lists | Notifications and observability; batch job ingestion. |

**CV one-liner (auto-apply):** Built an event-driven auto-apply system (Python, Selenium, Pydantic-AI + Gemini, GCP Cloud Functions/Run, Cloud Tasks, Pub/Sub, GCS, Secret Manager) for scraping and auto-filling ATS application forms across multiple vendors.

### Company Intelligence Agent

**Summary:** Provider-agnostic AI agent built with LangGraph that helps recruiters understand what a candidate's previous employer does. Given a company name from a candidate's CV, the agent autonomously runs custom web-search and scraping tools, iteratively retrieves live company data — business activity, funding rounds, tech stack, culture signals, recent news — and synthesises a structured summary surfaced in the recruiter UI alongside the candidate profile.

**Key components & techniques**
- **Agent framework:** LangGraph state-machine agent; provider-agnostic (swap any LLM backend); custom tool nodes for web search, page scraping, and structured extraction.
- **Tool use:** Modular custom tools — web search, HTML scraper, news aggregator — registered as LangGraph tool nodes; agent iterates until confidence threshold met.
- **Structured output:** Schema-enforced extraction (company activity, funding, tech stack, culture, news bullets); stored in GCS and served via internal API.
- **Pipeline:** Recruiter views candidate → trigger → LangGraph agent execution → GCS storage → internal Zen API update → UI enrichment.
- **Quality controls:** Fallback re-query on low-confidence fields; citation tracking so UI can link to source URLs.

**CV one-liner (company agent):** Built a LangGraph agent with custom web-search and scraping tools to autonomously retrieve and synthesise company intelligence (activity, funding, tech, news) — giving recruiters instant context on a candidate's previous employer.

---

### CV Processing & Candidate Ranking Pipeline

**Summary:** LLM-driven pipeline to parse uploaded candidate CVs, extract structured fields, calculate weighted match scores against job requirements, and rank candidates — reducing manual screening effort and improving shortlist quality.

**Key components & techniques**
- **CV parsing:** LLM (Gemini Flash) extracts structured fields from raw CV text: skills list, years of experience per domain, education level, seniority signal, location.
- **Scoring:** Weighted match scoring against job requirement vectors (required skills, min experience, education); configurable weights per job type.
- **Data flow:** CV upload → GCS → Cloud Function → LLM extraction → Pydantic validation → score calculation → ranked results stored in internal API.
- **Quality:** Schema-enforced Pydantic outputs prevent hallucinated fields; confidence flags on low-evidence extractions.

**CV one-liner (CV processing):** Built an LLM pipeline (Gemini, Pydantic-AI, GCP Cloud Functions) to parse CVs, extract structured candidate fields, calculate match scores against job requirements, and rank applicants automatically.

---

### Talent-seeker project (your accounts)

**Summary:** Full-stack app for LinkedIn-based talent outreach: manage accounts, relations, projects, and in-app messaging. Unipile API powers LinkedIn messaging, relations, and chat history; AWS AppSync delivers real-time updates (e.g. new messages) to the UI. Webhooks receive Unipile events (message, account, relation); backend validates and pushes to AppSync for live UI sync. Chat history stored in DynamoDB with cursor-based pagination; Stream Chat + custom WebSocket/AppSync for in-app chat and event-driven state.

**Architecture & flow**
- **Frontend:** React 19, Next.js 16 (Pages Router, API routes, server/client components), Material UI 7; React Context for LinkedIn relations, project, panel, messaging, and AppSync events.
- **Backend:** Next.js API routes (serverless-style), REST design and consumption (Unipile, internal), webhook handlers with signature/auth (Unipile-Auth).
- **Data & real-time:** DynamoDB (entity/repository layer, GSIs, chat history, cursor-based pagination); AppSync WebSocket subscriptions for publish/subscribe; flow: webhook → backend → AppSync → UI.
- **Integrations:** Unipile API (LinkedIn messaging, relations, accounts, chat history, invitations); LinkedIn Recruiter/Sales Navigator flows.

**Technologies & techniques**

| Area | Techniques / tech | Effect |
|------|-------------------|--------|
| **Languages & runtime** | TypeScript (primary; backend + frontend), JavaScript (Node.js) | Type-safe full stack; single language. |
| **Frontend** | React 19 (hooks, context, client components), Next.js 16 (Pages Router, API routes), MUI 7, React Context, useState/useEffect/useCallback/useMemo/useRef, Stream Chat (stream-chat, stream-chat-react), Lucide React, Day.js, Axios, UUID v7 | Consistent UI, theme, layout; in-app chat; shared state and reactive updates. |
| **Backend & APIs** | Next.js API routes, REST (Unipile, internal), webhooks (receive/validate Unipile message, account, relation; signature/auth) | Serverless-style handlers; secure webhook ingestion; Unipile/LinkedIn integration. |
| **Data & persistence** | AWS DynamoDB (@aws-sdk/client-dynamodb, lib-dynamodb), Get/Put/Query, GSIs, entity/repository layer, chat history storage, cursor-based pagination | Scalable persistence; clear data access; efficient “load more” for chat. |
| **Real-time & messaging** | AWS AppSync (WebSocket subscriptions, pub/sub), custom WebSocket helpers (channel format, subscription lifecycle), event-driven updates (webhook → backend → AppSync → UI) | Live LinkedIn message events and UI sync; deduplication to avoid double unread counts. |
| **AWS** | DynamoDB, AppSync, EventBridge, Lambda (event handlers) | Managed persistence, real-time, and event-driven processing. |
| **Dev & quality** | Git, Prettier, Biome (backend lint), Vitest, TypeScript strict + Zod | Formatting, lint, tests, type safety and validation. |
| **Infra & config** | Terraform (e.g. infrastructure/amplify.tf), env vars (API keys, endpoints) | IaC and env-based config. |
| **Practices** | Optimistic UI (show message then confirm via API), cursor-based pagination, Context + hooks, event deduplication, service layer (Unipile, chat history repo, user metadata repo), secure webhooks (header validation, idempotency) | Responsive UX; clear layering; fewer duplicate events and safer webhooks. |

**Technical skills block (CV):** Frontend: React 19, Next.js 16, TypeScript, Material UI, React Context & hooks, Stream Chat, Axios. Backend: Node.js, Next.js API routes, REST APIs, webhook handling, TypeScript. Data & real-time: AWS DynamoDB (GSI, repository pattern), AWS AppSync (real-time subscriptions), cursor-based pagination. Integrations: Unipile API (LinkedIn messaging, relations, accounts), LinkedIn Recruiter/Sales Navigator flows. Dev & infra: Git, Prettier, Biome, Vitest, Terraform, env-based config. Practices: Optimistic UI, event-driven updates, service/repository layering, type-safe APIs.

**CV one-liner (talent-seeker):** TypeScript · React · Next.js · Material UI · AWS (DynamoDB, AppSync, Lambda) · REST APIs & webhooks · Unipile/LinkedIn integration · real-time WebSocket/AppSync · Terraform.

---

## AI Engineer (Contractor)
**Comply Copilot** | May 2025 – Jun 2025

**Focus:** Backend and AI/LLM features for planning and consent: activity–standard linking, recommended activities, standard evaluation, and PDF extraction.

**1. Activity–standard linking**
- End-to-end pipeline to link council activities to compliance standards using LLMs.
- Batch processing by section (e.g. H1–H30, E1–E39) with section-specific standard documents.
- Structured LLM output (activity code, status, list of standard codes); async processing with semaphore (e.g. concurrency 5).
- Separate script to apply LLM responses to CSV (e.g. `compliance_standard_ids`) with normalised activity codes and composite keys (section, code, status).

**2. Recommended activities (auto-select from COCO)**
- Reduced candidate activities from ~1100 to ~200 via LLM-based relevance filtering (large token/cost reduction).
- Composite keys (section_id + activity_code), deduplicated activity text (~30% token savings).
- Integrated project plans and GIS; council-specific logic (e.g. Auckland, Christchurch).
- Async LLM calls and structured responses for recommended activities per section.

**3. Standard evaluation (assessment of rules)**
- LLM-based evaluation of project plans against council standards with detailed reports and page references.
- Refined prompts and moved to no-thinking models where appropriate for cost.
- Concurrent evaluation with asyncio semaphore and fallback/retry around LLM calls.

**4. PDF extraction with LLM**
- LLM-driven extraction: text-first with image fallback, lower-resolution images.
- Async page-level summarisation and plan detection.

**Techniques & technologies:** Python, asyncio, Semaphore; Google Gemini (Flash/Pro), Claude; structured outputs, prompt design; Pydantic (schemas, validation), JSON/CSV pipelines; SQLModel, SQL; token reduction, deduplication, batching; PDF parsing, text + image extraction.

**CV one-liner:** Designed and implemented LLM-based pipelines for activity–standard linking, recommended-activity filtering, and plan-vs-standard evaluation; used asyncio, Pydantic, and prompt/token optimisation to improve reliability and cost.

**Reference:** Joshua — joshua@complycopilot.com

---


## Artificial Intelligence Engineer
**Imagr** | May 2022 – April 2025

- Designed, trained, and deployed Computer Vision models for smart shopping carts: **Object Detection** (YOLO, SSD, Faster R-CNN), **Segmentation** (U-Net, Mask R-CNN, SAM), **Classification** (MobileNet, EfficientNet, Inception).
- Optimized models for Google EdgeTPU (quantization): ~75% model size reduction, 2–4× inference speedup with minimal accuracy loss.
- Used Google Coral Dev Board for edge deployment: developed object detection models in TensorFlow/PyTorch, quantized them, and ran inference on the Coral board with C++.
- Trained on Google Cloud TPUs; datasets in TFRecord format; used Vertex AI, AutoML, BigQuery ML.
- Self-hosted CVAT for annotation; auto-annotation with trained models (e.g. YOLOv5) to cut annotation cost ~90% and time ~50%.
- Multi-processing for batch image preprocessing (debayer, augmentation), ~80% preprocessing time reduction.
- Implemented SORT for real-time object tracking; web crawling for data collection.
- Post-deployment: identified performance gaps and retrained with additional data.

---

## Intern
**Davanti Consultant** | November 2021 – February 2022

- Developed a CRM for a non-profit using Salesforce as part of their system transformation.
- Client communication, requirements gathering, feature implementation, testing, documentation.
- Agile delivery, deployment best practices, conflict resolution.

---

## Graduate Teaching Assistant
**University of Auckland** | March 2021 – November 2021

- **CS719** Programming with Web Technologies (JavaScript, Node.js, HTML, CSS, SQLite, database design).
- **CS718** Programming for Industry (Java).
- Prepared and delivered online live code demos to explain complex concepts.
