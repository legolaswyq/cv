"""Generate Walter Wang CV for Senior AI Specialist roles (Computer Vision / Agentic AI)."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY

PAGE_W, PAGE_H = A4
MARGIN = 18 * mm

# Colour palette
DARK = colors.HexColor("#1A1A2E")
ACCENT = colors.HexColor("#16213E")
MID = colors.HexColor("#0F3460")
LIGHT_LINE = colors.HexColor("#CCCCCC")
TAG_BG = colors.HexColor("#E8EEF7")
TAG_FG = colors.HexColor("#1A1A2E")
WHITE = colors.white

def build_styles():
    base = getSampleStyleSheet()
    def S(name, **kw):
        return ParagraphStyle(name, **kw)

    return {
        "name": S("name",
            fontName="Helvetica-Bold", fontSize=22, textColor=DARK,
            spaceAfter=1 * mm, leading=26),
        "title": S("title",
            fontName="Helvetica", fontSize=11, textColor=MID,
            spaceAfter=3 * mm, leading=15),
        "contact": S("contact",
            fontName="Helvetica", fontSize=8.5, textColor=colors.HexColor("#444444"),
            spaceAfter=0, leading=13),
        "section": S("section",
            fontName="Helvetica-Bold", fontSize=11, textColor=WHITE,
            spaceAfter=2 * mm, leading=14),
        "job_title": S("job_title",
            fontName="Helvetica-Bold", fontSize=10, textColor=DARK,
            spaceAfter=0.5 * mm, leading=13),
        "company": S("company",
            fontName="Helvetica-Oblique", fontSize=9, textColor=MID,
            spaceAfter=1 * mm, leading=12),
        "bullet": S("bullet",
            fontName="Helvetica", fontSize=8.8, textColor=colors.HexColor("#222222"),
            leftIndent=8, firstLineIndent=-8, spaceAfter=1.5 * mm,
            leading=12.5, bulletIndent=0),
        "body": S("body",
            fontName="Helvetica", fontSize=8.8, textColor=colors.HexColor("#222222"),
            spaceAfter=1.5 * mm, leading=12.5),
        "profile": S("profile",
            fontName="Helvetica", fontSize=9, textColor=colors.HexColor("#222222"),
            spaceAfter=2 * mm, leading=13.5, alignment=TA_JUSTIFY),
        "edu_title": S("edu_title",
            fontName="Helvetica-Bold", fontSize=9, textColor=DARK,
            spaceAfter=0.5 * mm, leading=12),
        "edu_body": S("edu_body",
            fontName="Helvetica", fontSize=8.8, textColor=colors.HexColor("#333333"),
            spaceAfter=0.5 * mm, leading=12),
        "tag": S("tag",
            fontName="Helvetica", fontSize=8, textColor=TAG_FG,
            spaceAfter=0, leading=11),
        "small": S("small",
            fontName="Helvetica", fontSize=8, textColor=colors.HexColor("#555555"),
            spaceAfter=0, leading=11),
    }


def section_header(title, styles, width):
    """Dark banner with white section title."""
    data = [[Paragraph(title.upper(), styles["section"])]]
    t = Table(data, colWidths=[width])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), ACCENT),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    return t


def tag_table(tags, styles, width):
    """Inline tag chips."""
    cells = [Paragraph(f"  {t}  ", styles["tag"]) for t in tags]
    per_row = 6
    rows = [cells[i:i+per_row] for i in range(0, len(cells), per_row)]
    col_w = width / per_row
    tables = []
    for row in rows:
        padded = row + [Paragraph("", styles["tag"])] * (per_row - len(row))
        t = Table([padded], colWidths=[col_w] * per_row)
        t.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), TAG_BG),
            ("ROUNDEDCORNERS", [3, 3, 3, 3]),
            ("LEFTPADDING", (0, 0), (-1, -1), 4),
            ("RIGHTPADDING", (0, 0), (-1, -1), 4),
            ("TOPPADDING", (0, 0), (-1, -1), 2),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
            ("GRID", (0, 0), (-1, -1), 0.3, colors.HexColor("#BBCCDD")),
        ]))
        tables.append(t)
        tables.append(Spacer(1, 1.5 * mm))
    return tables


def build_cv(out_path):
    doc = SimpleDocTemplate(
        out_path,
        pagesize=A4,
        leftMargin=MARGIN, rightMargin=MARGIN,
        topMargin=14 * mm, bottomMargin=14 * mm,
    )
    W = PAGE_W - 2 * MARGIN
    S = build_styles()
    story = []

    # ── HEADER ────────────────────────────────────────────────────────────────
    header_data = [[
        Paragraph("Walter Wang", S["name"]),
        Paragraph("Senior AI Engineer", S["title"]),
        Paragraph(
            "022-104-1307  ·  legolaswyq@gmail.com  ·  "
            "linkedin.com/in/yuqi-wang-74a84b218",
            S["contact"]),
    ]]
    header_t = Table(
        [[Paragraph("Walter Wang", S["name"])],
         [Paragraph("Senior AI Engineer — Computer Vision &amp; Agentic AI", S["title"])],
         [Paragraph("022-104-1307  ·  legolaswyq@gmail.com  ·  linkedin.com/in/yuqi-wang-74a84b218", S["contact"])]],
        colWidths=[W]
    )
    header_t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F4F7FC")),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (0, 0), 7),
        ("BOTTOMPADDING", (0, -1), (-1, -1), 7),
        ("TOPPADDING", (0, 1), (-1, -1), 1),
        ("BOTTOMPADDING", (0, 0), (-1, -2), 1),
        ("LINEBELOW", (0, -1), (-1, -1), 2, MID),
    ]))
    story.append(header_t)
    story.append(Spacer(1, 4 * mm))

    # ── PROFILE ───────────────────────────────────────────────────────────────
    story.append(section_header("Profile", S, W))
    story.append(Spacer(1, 2 * mm))
    story.append(Paragraph(
        "AI Engineer with 4+ years of commercial experience spanning Computer Vision, "
        "Agentic AI, and cloud-native backend engineering. At Imagr I designed, trained, "
        "and edge-deployed object-detection, segmentation, and classification models for "
        "real-time smart shopping-cart systems. More recently at ZEIL I architect and "
        "ship multi-agent, LLM-driven pipelines (Pydantic-AI, Gemini) on GCP that "
        "automate end-to-end workflows at scale, and built real-time full-stack products "
        "with React/Next.js and AWS. I take ideas from prototype to production and focus "
        "on outcomes and measurable value.",
        S["profile"]
    ))
    story.append(Spacer(1, 3 * mm))

    # ── EXPERIENCE ────────────────────────────────────────────────────────────
    story.append(section_header("Experience", S, W))
    story.append(Spacer(1, 2 * mm))

    def job(title, company, period, bullets):
        hdr = Table(
            [[Paragraph(title, S["job_title"]),
              Paragraph(period, S["small"])]],
            colWidths=[W * 0.72, W * 0.28]
        )
        hdr.setStyle(TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "BOTTOM"),
            ("RIGHTPADDING", (1, 0), (1, 0), 0),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("ALIGN", (1, 0), (1, 0), "RIGHT"),
        ]))
        story.append(hdr)
        story.append(Paragraph(company, S["company"]))
        for b in bullets:
            story.append(Paragraph(f"• {b}", S["bullet"]))
        story.append(Spacer(1, 2.5 * mm))

    # ZEIL — AI Engineer
    job(
        "AI Engineer",
        "ZEIL  |  Auckland, NZ",
        "Jul 2025 – Present",
        [
            "<b>Auto-apply pipeline:</b> Designed an event-driven, multi-tenant pipeline that scrapes "
            "ATS job-application forms with headless browser automation, maps fields using AI structured "
            "outputs, and auto-fills applications at scale across multiple ATS vendors.",
            "<b>Company Intelligence Agent:</b> Built a provider-agnostic AI agent with custom "
            "web-search and scraping tools that, given a company name from a candidate's CV, "
            "autonomously retrieves live data — business activity, funding, tech stack, and news — "
            "and synthesises a structured summary to give recruiters instant context on a candidate's "
            "previous employer.",
            "<b>CV Processing &amp; Candidate Ranking:</b> Developed an LLM pipeline that parses "
            "uploaded CVs, extracts structured fields, calculates weighted match scores against job "
            "requirements, and ranks candidates — reducing manual screening effort and improving "
            "shortlist quality.",
            "<b>Talent-seeker platform:</b> Full-stack LinkedIn outreach app with real-time messaging, "
            "relation management, and live event sync; cloud-native backend with managed database and "
            "real-time subscriptions.",
        ]
    )

    # Comply Copilot
    job(
        "AI Engineer (Contractor)",
        "Comply Copilot  |  Remote",
        "May 2025 – Jun 2025",
        [
            "Built LLM pipelines to link council activities to compliance standards, filter recommended "
            "activities (~1,100 → ~200 via relevance scoring), and evaluate project plans against "
            "regulatory rules — with structured outputs, async concurrency, and fallback/retry for "
            "reliability.",
            "Cut token costs ~30% through deduplication, batching, and selective model choices; "
            "improved output quality via iterative prompt design and schema-enforced responses.",
        ]
    )

    # Imagr
    job(
        "Artificial Intelligence Engineer",
        "Imagr  |  Auckland, NZ",
        "May 2022 – Apr 2025",
        [
            "Designed, trained, and deployed Computer Vision models for smart shopping carts: "
            "<b>Object Detection</b> (YOLO, SSD, Faster R-CNN), <b>Segmentation</b> (U-Net, Mask R-CNN, SAM), "
            "<b>Classification</b> (MobileNet, EfficientNet, Inception); customised architectures and "
            "loss functions to suit real-world retail constraints — varied lighting, partial occlusion, "
            "and high SKU count.",
            "Full model lifecycle — collect data, train, deploy, monitor production metrics, identify "
            "failure modes, then close the loop: targeted data collection in scenarios where the model "
            "performed worst, re-annotation, and iterative fine-tuning to continuously raise accuracy.",
            "Self-hosted CVAT for annotation; trained a large model on an initial labelled dataset and "
            "used it to auto-annotate new data at scale — human reviewers corrected predictions and "
            "refined labels were fed back to fine-tune the model, producing a high-quality dataset "
            "that drove sustained accuracy gains while cutting annotation cost ~90% and time ~50%.",
            "Implemented native Bayer RAW image processing in the inference pipeline — decoding RAW "
            "sensor frames directly rather than converting to RGB first — eliminating a preprocessing "
            "step and improving end-to-end inference speed.",
            "Optimised models for <b>Google EdgeTPU</b> via quantisation: ~75% model size reduction, "
            "2–4× inference speedup with minimal accuracy loss; deployed on Coral Dev Board with C++.",
            "Trained on Google Cloud TPUs with TFRecord datasets; implemented SORT for real-time "
            "multi-object tracking.",
        ]
    )

    # Davanti
    job(
        "Intern — Salesforce Developer",
        "Davanti Consulting  |  Auckland, NZ",
        "Nov 2021 – Feb 2022",
        [
            "Developed a CRM for a non-profit on Salesforce; gathered requirements, implemented features, "
            "tested, and delivered documentation in an Agile team.",
        ]
    )

    # Teaching Assistant
    job(
        "Graduate Teaching Assistant",
        "University of Auckland",
        "Mar 2021 – Nov 2021",
        [
            "Delivered live code demos for CS719 (Web Technologies: JS, Node.js, HTML, CSS, SQLite) "
            "and CS718 (Programming for Industry: Java).",
        ]
    )

    # ── EDUCATION ─────────────────────────────────────────────────────────────
    story.append(section_header("Education", S, W))
    story.append(Spacer(1, 2 * mm))

    edu = [
        ("University of Auckland",
         "Master of Information Technology — First Class Honours (GPA 8.0)"),
        ("University of Auckland",
         "Postgraduate Certificate in Information Technology — Best Student Award (2020)"),
        ("South China Agricultural University",
         "Bachelor of Industrial Engineering"),
    ]
    for inst, deg in edu:
        story.append(Paragraph(inst, S["edu_title"]))
        story.append(Paragraph(deg, S["edu_body"]))
        story.append(Spacer(1, 1.5 * mm))

    story.append(Spacer(1, 2 * mm))

    # ── CERTIFICATIONS ────────────────────────────────────────────────────────
    story.append(section_header("Certifications & Awards", S, W))
    story.append(Spacer(1, 2 * mm))
    certs = [
        "AWS Certified Solutions Architect — Associate",
        "Coursera Deep Learning Specialization (Andrew Ng)",
        "Google Prompting Essentials",
        "Prompt Engineering for ChatGPT — Vanderbilt University",
        "Certificates of Outstanding Achievement: Data Mining · Advanced AI",
    ]
    for c in certs:
        story.append(Paragraph(f"• {c}", S["bullet"]))

    story.append(Spacer(1, 3 * mm))

    # ── CORE SKILLS ───────────────────────────────────────────────────────────
    story.append(section_header("Core Skills", S, W))
    story.append(Spacer(1, 2 * mm))

    skill_rows = [
        ("Agentic AI / LLM",
         "Pydantic-AI · Google Gemini (Flash/Pro) · Claude · Prompt Engineering · "
         "Structured Outputs · Tool Use / Web Search · Multi-agent orchestration · "
         "RAG · Token optimisation · Async pipelines"),
        ("Computer Vision",
         "YOLO · SSD · Faster R-CNN · U-Net · Mask R-CNN · SAM · MobileNet · "
         "EfficientNet · OpenCV · TensorFlow · PyTorch · Google EdgeTPU / Coral · "
         "Vertex AI · AutoML · BigQuery ML"),
        ("Cloud & Infra",
         "GCP (Cloud Run, Cloud Functions, Cloud Tasks, Pub/Sub, GCS, Secret Manager) · "
         "AWS (DynamoDB, AppSync, Lambda, EventBridge) · Terraform · Docker"),
        ("Backend & Data",
         "Python · asyncio · Pydantic · Flask · FastAPI · REST APIs · Webhooks · "
         "SQLModel · Avro · CSV/JSON pipelines · Selenium · BeautifulSoup"),
        ("Frontend",
         "TypeScript · React 19 · Next.js 16 · Material UI · Real-time WebSocket / AppSync"),
        ("Practices",
         "Event-driven architecture · Edge quantisation · Concurrency "
         "(ThreadPoolExecutor, asyncio) · CI/CD · Agile"),
    ]
    col_w = [35 * mm, W - 35 * mm]
    for label, value in skill_rows:
        row = [[
            Paragraph(f"<b>{label}</b>", S["body"]),
            Paragraph(value, S["body"]),
        ]]
        t = Table(row, colWidths=col_w)
        t.setStyle(TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 4),
            ("RIGHTPADDING", (0, 0), (-1, -1), 4),
            ("TOPPADDING", (0, 0), (-1, -1), 2),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
        ]))
        story.append(t)
    story.append(Spacer(1, 3 * mm))

    # ── REFERENCES ────────────────────────────────────────────────────────────
    story.append(section_header("References", S, W))
    story.append(Spacer(1, 2 * mm))
    refs = [
        ("Konstantinos", "Chief AI Officer, Imagr", "konstantinos@imagr.co"),
        ("Joshua", "Comply Copilot", "joshua@complycopilot.com"),
        ("Alice Hopkinson", "Practice Lead, Davanti Consulting", "alice.hopkinson@davanti.co.nz"),
    ]
    ref_rows = [[
        Paragraph(f"<b>{n}</b><br/>{role}<br/><font color='#0F3460'>{email}</font>", S["body"])
        for n, role, email in refs
    ]]
    ref_t = Table(ref_rows, colWidths=[W / 3] * 3)
    ref_t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 2),
    ]))
    story.append(ref_t)

    doc.build(story)
    print(f"CV written to {out_path}")


if __name__ == "__main__":
    import os
    out = os.path.join(os.path.dirname(__file__), "Walter_Wang_Senior_AI_Specialist_CV.pdf")
    build_cv(out)
