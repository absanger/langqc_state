from typing import Dict, List

from fastapi import FastAPI

tags_metadata = [
    {
        "name": "Well inbox",
        "description": "Get wells with different statuses. For now this only contains"
        " PacBio-specific wells.",
    },
    {
        "name": "Well level QC operations",
        "description": "Collection of endpoints to claim and assign QC statuses to"
        " specific PacBio wells.",
    },
    {
        "name": "ID-based QC operations",
        "description": "Collection of endpoints to clain and assign QC statuses, using"
        " product IDs.",
    },
]

app = FastAPI(title="LangQC State API", openapi_tags=tags_metadata)


# Get wells in different statuses


@app.get("/wells/qc_status/in_progress", response_model=List, tags=["Well inbox"])
def get_in_progress_wells():
    """Get in progress wells.

    Possibly empty list of wells that are "Claimed", not "On hold" or anything else that
    is preliminary.
    """
    pass


@app.get("/wells/qc_status/on_hold", response_model=List, tags=["Well inbox"])
def get_on_hold_wells():
    """Get on hold wells.

    Possibly empty list of wells that are "On hold".
    """
    pass


@app.get("/wells/qc_status/qc_complete", response_model=List, tags=["Well inbox"])
def get_qc_complete_wells():
    """Get qc_complete wells.

    Possibly empty list of wells with any status that is not preliminary, apart from
    "Claimed" and "On hold".
    """
    pass


# Well level QC operations


@app.post(
    "/run/{run_name}/well/{well_label}/qc_claim", tags=["Well level QC operations"]
)
def claim_well(user_claim: Dict, run_name: str, well_label: str):
    pass


@app.post(
    "/run/{run_name}/well/{well_label}/qc_steal", tags=["Well level QC operations"]
)
def steal_well(user_claim: Dict, run_name: str, well_label: str):
    pass


@app.post(
    "/run/{run_name}/well/{well_label}/qc_assign", tags=["Well level QC operations"]
)
def qc_assign_well(qc_state: Dict, run_name: str, well_label: str):
    pass


# ID-level QC operations


@app.post("/id_product", response_model=str, tags=["ID-based QC operations"])
def get_product_id(product: Dict):
    pass


@app.post("/qc_claim/{id_product}", tags=["ID-based QC operations"])
def claim_product(user_claim: Dict, id_product: str):
    pass


@app.post("/qc_steal/{id_product}", tags=["ID-based QC operations"])
def steal_product(user_claim: Dict, id_product: str):
    pass


@app.post("/qc_assign/{id_product}", tags=["ID-based QC operations"])
def qc_assign_product(qc_state: Dict, id_product: str):
    pass
