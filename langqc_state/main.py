from typing import Dict

from fastapi import FastAPI

from langqc_state.models import (
    InboxResults,
    GetWellQcOutcomeResult,
    QcStatus,
    QcStatusEnum,
)

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


@app.get("/wells", response_model=InboxResults, tags=["Well inbox"])
def get_wells_filtered_by_status(qc_status: QcStatusEnum = None):
    pass


@app.get("/wells/qc_status/inbox", response_model=InboxResults, tags=["Well inbox"])
def get_inbox_wells():
    """Get inbox wells.

    Makes a call to the langqc data API, and returns a filtered list. Returns wells
    that are not yet assigned any QC status.
    """
    pass


@app.get(
    "/wells/qc_status/in_progress", response_model=InboxResults, tags=["Well inbox"]
)
def get_in_progress_wells():
    """Get in progress wells.

    Possibly empty list of wells that are "Claimed", not "On hold" or anything else that
    is preliminary.
    """
    pass


@app.get("/wells/qc_status/on_hold", response_model=InboxResults, tags=["Well inbox"])
def get_on_hold_wells():
    """Get on hold wells.

    Possibly empty list of wells that are "On hold".
    """
    pass


@app.get(
    "/wells/qc_status/qc_complete", response_model=InboxResults, tags=["Well inbox"]
)
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
def claim_well(user_claim: QcStatus, run_name: str, well_label: str):
    pass


@app.post(
    "/run/{run_name}/well/{well_label}/qc_steal", tags=["Well level QC operations"]
)
def steal_well(user_claim: QcStatus, run_name: str, well_label: str):
    pass


@app.post(
    "/run/{run_name}/well/{well_label}/qc_assign", tags=["Well level QC operations"]
)
def qc_assign_well(qc_state: QcStatus, run_name: str, well_label: str):
    pass


@app.get(
    "/run/{run_name}/well/{well_label}/qc_outcome",
    tags=["Well level QC operations"],
    response_model=GetWellQcOutcomeResult,
)
def get_well_qc_outcome(run_name: str, well_label: str):
    pass


# ID-level QC operations


@app.post(
    "/product/find_id_product", response_model=str, tags=["ID-based QC operations"]
)
def find_product_id(product: Dict):
    pass


@app.post("/product/{id_product}/qc_claim", tags=["ID-based QC operations"])
def claim_product(user_claim: Dict, id_product: str):
    pass


@app.post("/product/{id_product}/qc_steal", tags=["ID-based QC operations"])
def steal_product(user_claim: Dict, id_product: str):
    pass


@app.post("/product/{id_product}/qc_assign", tags=["ID-based QC operations"])
def qc_assign_product(qc_state: Dict, id_product: str):
    pass


@app.get("/product/{id_product}/qc_outcome", tags=["ID-based QC operations"])
def get_product_qc_outcome(id_product: str):
    pass
