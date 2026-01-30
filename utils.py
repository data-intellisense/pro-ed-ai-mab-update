"""Utility functions for the ProEd AI Demo app."""
from pathlib import Path
from docx import Document


def read_docx_content(file_path: str) -> list[dict]:
    """
    Read content from a Word document and return structured data.
    
    Returns a list of dictionaries with 'type' and 'content' keys.
    Types can be: 'heading', 'paragraph', 'list_item'
    """
    doc = Document(file_path)
    content = []
    
    for para in doc.paragraphs:
        text = para.text.strip()
        if not text:
            continue
            
        # Determine content type based on style
        style_name = para.style.name.lower() if para.style else ""
        
        if "heading" in style_name:
            content.append({
                "type": "heading",
                "level": int(style_name[-1]) if style_name[-1].isdigit() else 1,
                "content": text
            })
        elif para.style.name == "List Paragraph" or text.startswith(("•", "-", "●")):
            content.append({
                "type": "list_item",
                "content": text.lstrip("•-● ")
            })
        else:
            content.append({
                "type": "paragraph",
                "content": text
            })
    
    return content


def get_data_path() -> Path:
    """Get the path to the data directory."""
    return Path(__file__).parent / "data"


# ProEd Focus Areas
FOCUS_AREAS = [
    "Energy - future looking (traditional sources, nuclear, geothermal)",
    "AI use in industry",
    "Executive education in STEM fields",
    "Mining & Minerals",
    "Aerospace",
    "Construction Engineering"
]

# Financial Model Data
FINANCIAL_MODEL = {
    "self_paced": {
        "title": "Self-Paced (On-Demand) Courses",
        "options": [
            {
                "name": "Option A: Revenue Share",
                "compensation": "$250 per learning hour created",
                "revenue_share": "20% of net revenue"
            },
            {
                "name": "Option B: Flat Rate",
                "compensation": "$750 per learning hour created",
                "revenue_share": "None"
            }
        ]
    },
    "facilitated": {
        "title": "Online Facilitated Courses",
        "note": "Facilitated delivery requires active participation from the instructor throughout the course each time it is taught.",
        "compensation": "$2,500 per teaching day",
        "preparation_fee": "$1,250 per teaching day",
        "revenue_share": "20% of net revenue",
        "example": "A two-day course would be $5,000 + $2,500 preparation"
    }
}

# SME Application Link
SME_APPLICATION_LINK = "https://webforms.pipedrive.com/f/clTeQxDh43DxZluuQxlgduRDzDnztn2vjizguzjcyzcHtmzZhocEMbCATC0qF1KMzV"
