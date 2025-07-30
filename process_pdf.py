import torch  # Optional preload for DLLs
import os
import onnxruntime
capi_path = os.path.join(os.path.dirname(onnxruntime.__file__), 'capi')
os.environ['PATH'] = capi_path + os.pathsep + os.environ['PATH']
# Now import unstructured.partition.pdf
# import onnxruntime as ort  # For explicit provider setup if desired

from unstructured.partition.pdf import partition_pdf

# Common parameters as keywords
common_params = {
    "strategy": "hi_res",
    "hi_res_model_name": "yolox",
    "languages": ["heb"],
    "infer_table_structure": True,
    "extract_images_in_pdf": True,  # If books have diagrams
    "chunking_strategy": "by_title"  # Groups into sections for tutor dataset
}

# Process first book
elements1 = partition_pdf(
    filename="D:/path/to/your_first_hebrew_grammar_book.pdf",  # Replace with actual path, e.g., "D:\\AI\\Projects\\HEBREW TRAINING AI AGENT\\GRAMMAR\\Book1.pdf"
    **common_params
)

# Save as JSON
import json
with open("grammar_book1.json", "w", encoding="utf-8") as f:
    json.dump([el.to_dict() for el in elements1], f, ensure_ascii=False, indent=4)

# Process second book
elements2 = partition_pdf(
    filename="D:\\AI\\Projects\\HEBREW TRAINING AI AGENT\\GRAMMAR\\Gesenius-HebrewGrammar.pdf",
    **common_params
)

# Save as JSON
with open("grammar_book2.json", "w", encoding="utf-8") as f:
    json.dump([el.to_dict() for el in elements2], f, ensure_ascii=False, indent=4)