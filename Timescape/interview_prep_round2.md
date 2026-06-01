# Timescapes Round 2 — Interview Prep (with Shehan Bala, VP Product)

## Who You're Talking To

**Shehan Bala** is VP of Product (listed as "CPO" in your notes but ZoomInfo shows VP Product). His background spans **Xero, Datacom NZ, See-Mode Technologies (medical AI), Digital Humans, and Meaningful Technology** — he's a product person with a tech lens, not an ML engineer. He will evaluate your **product thinking and communication**, not your model architecture knowledge.

**Round 2 purpose (from the JD):** "Provide context, understand career history, answer questions" — this is a two-way conversation. Your job is to tell a coherent story AND leave with real signal about the role.

---

## What Timescapes Actually Does (Crisp Summary)

From the website + webinar:

- **Core product:** Solar-powered, **Cellular data**， cableless cameras on construction sites → high-res timelapse + live feeds
- **AI layer:** Automatically extracts **worker volume/activity, heavy equipment utilisation, concrete delivery truck schedules** from images
- **Platform features:** BIM overlay (real vs. designed), weather data correlation, milestone comparison, automated daily logs, dispute resolution with visual evidence
- **Integrations:** Procore, Autodesk, IoT sensors
- **Scale:** 100+ companies, 400+ projects, AU/CA/NZ/US
- **Usage intensity (Capital Group webinar):** 300–400 platform sessions/day — this is a daily operational tool, not a reporting add-on
- **Recent focus (Dec 2025 UX article):** Simplified information architecture; next phase = richer data layers (schedules, progress metrics) — ML relevance here is high

---

## Points to Prepare — Your Story

### 1. Lead with the product outcome, not the model
Shehan cares about value delivered, not YOLO variants. For every project, prepare a one-liner:

| Project | What you'd say to a CPO |
|---|---|
| Imagr (CV) | "I built the detection and tracking pipeline that ran on every cart in production — I owned it from labelling through edge deployment and post-release monitoring. When performance dropped, I diagnosed it and retrained." |
| Comply Copilot | "I built LLM pipelines that let the product evaluate whether a construction plan met council standards — the kind of document-heavy compliance work that was previously manual and slow." |
| ZEIL auto-apply | "Event-driven pipeline that automated a labour-intensive process at scale — I designed the data contracts, the inference layer, and the error handling." |

### 2. Address the "second ML hire" framing directly
The JD says you're hire #2. Prepare to answer: *"What would you want to know about what the first hire built before joining?"* This signals you think in terms of foundations and handoffs, not just greenfield work.

### 3. Show you've used the product (conceptually)
From the webinar: Capital Group uses Timescapes 300–400x/day. The value is **shared visibility** — not just dashboards, but trust and dispute resolution. Connect this to your work: at Imagr you built systems that had to be reliable enough to be trusted in a live retail environment — similar stakes.

### 4. Construction domain gap — address it proactively
You don't have direct construction CV experience, but:
- Comply Copilot = construction planning and consent (LLM-driven, but construction-adjacent)
- Imagr = real-world retail CV with same core challenges: occlusion, lighting variation, moving objects, edge deployment
- Frame it: "The domain is new to me but the problems — tracking activity over time, handling visual ambiguity, connecting model output to business decisions — are ones I've solved in analogous contexts."

### 5. Gap to know about: .NET / C# / TensorRT
The JD lists these as preferred. You don't have them. Don't volunteer the gap, but if asked: "I haven't used TensorRT directly but I've done model quantization for EdgeTPU which shares the same tradeoffs — latency vs accuracy vs memory budget. TensorRT is on my list."

---

## Questions to Ask Shehan

### Product & ML Roadmap
- "The platform now tracks worker volume, equipment, and concrete deliveries — what's the next detection capability on the roadmap, and what's blocking it: data, model accuracy, or something else?"
- "The recent UX work focused on simplifying navigation and making newer tools more discoverable. How does ML fit into that next phase — are there analytical features that haven't landed yet because the model side wasn't ready?"
- "How do customers currently consume insights — do they come to the platform proactively, or is it more notification-driven? Where do you want that to go?"

### The "second hire" context
- "What did the first ML hire focus on, and where are the biggest gaps they left or weren't resourced to tackle?"
- "How do you split priorities between improving existing model accuracy vs. building new detection capabilities?"

### Ways of working
- "How does product define ML requirements here — do you come to engineering with a problem, a proposed solution, or something in between?"
- "What does an experiment-to-production cycle look like? Is there infrastructure in place for that, or is part of the role to build it?"

### Business & market
- "Capital Group mentioned initial 'big brother' skepticism that faded in six months — is managing that perception still a live challenge with new customers, and does that affect how you design ML features like activity tracking?"
- "You're expanding into the US — are there ML challenges that are market-specific? Different site types, weather, data availability?"

### Success signal
- "What does success in this role look like at 3 months and 6 months?"

---

## Things to Notice / Red Flags During the Interview

| Signal | What it means |
|---|---|
| Vague answer on what the first ML hire delivered | The ML function may be unclear or undervalued |
| Shehan can't describe a specific ML problem they're struggling with | ML is an afterthought, not a product priority |
| "You'd figure out the data side as you go" | No data infrastructure — you'd be starting from zero with no support |
| No answer on experiment-to-production timeline | No ML culture or process yet |
| Enthusiastic about BIM/schedule integration | This is where ML gets interesting — progress estimation, not just activity detection |
| Mentions camera hardware constraints | Edge ML on the camera itself may be a future direction — your EdgeTPU experience is directly relevant |

---

## Your Strongest CV-to-JD Matches (for Shehan)

| JD requirement | Your evidence |
|---|---|
| Production CV models | Imagr: YOLO, Mask R-CNN, SAM — full lifecycle |
| End-to-end ML ops | Data → CVAT → auto-annotation → training → EdgeTPU deployment → monitoring |
| LLMs + multimodality | Comply Copilot (Claude, Gemini, structured outputs), ZEIL (Pydantic-AI) |
| Off-the-shelf vs custom trade-offs | Active at every role — can speak to decision frameworks |
| High-throughput inference | ZEIL async pipelines; Imagr production edge inference |
| SDLC ownership | Consistently end-to-end across roles |
| Edge ML (preferred) | EdgeTPU + Coral Dev Board — this is a differentiator |

---

## One-paragraph opener to rehearse

> "I've spent the last four years building computer vision systems that have to work reliably in production — at Imagr that meant everything from labelling pipelines and model training through to running C++ inference on edge hardware in live retail environments. More recently I've been working with LLMs and multimodal models, including in the construction space at Comply Copilot. What draws me to Timescapes is that the problems — tracking real-world activity over time from camera feeds, connecting visual data to business decisions — are things I've worked on in adjacent contexts, and I think there's a genuine opportunity to build something meaningful here."
