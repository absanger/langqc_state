from datetime import datetime
from enum import Enum
from typing import List

from pydantic import BaseModel, Field


class QcStatusEnum(Enum):
    INBOX = "inbox"
    IN_PROGRESS = "in_progress"
    ON_HOLD = "on_hold"
    QC_COMPLETE = "qc_complete"


# QC_outcome model


class QcStatus(BaseModel):

    user: str = Field(default=None, title="User owning the QC state.")
    date_created: datetime = Field(default=None, title="Date created")
    date_updated: datetime = Field(default=None, title="Date updated")
    qc_type: str = Field(default=None, title="QC type")
    qc_type_description: str = Field(default=None, title="QC type description")
    qc_outcome_type: str = Field(
        default=None, title="QC outcome type", description="Short outcome or outcome"
    )
    is_preliminary: bool = Field(default=None, title="Preliminarity of the ouctome")
    created_by: str = Field(default=None, title="QC State creator")


class GetWellQcOutcomeResult(BaseModel):

    label: str = Field(
        default=None, title="Well label", description="The well identifier."
    )
    start: datetime = Field(default=None, title="Timestamp of well started.")
    complete: datetime = Field(default=None, title="Timestamp of well complete.")
    qc_outcome: QcStatus


# Inbox models


class WellInfo(BaseModel):
    label: str = Field(
        default=None, title="Well label", description="The well identifier."
    )
    start: datetime = Field(default=None, title="Timestamp of well started")
    complete: datetime = Field(default=None, title="Timestamp of well complete")
    qc_status: QcStatus


class InboxResultEntry(BaseModel):

    run_name: str = Field(default=None, title="Run Name")
    time_start: datetime = Field(default=None, title="Run start time")
    time_complete: datetime = Field(default=None, title="Run complete time")
    wells: List[WellInfo]


class InboxResults(BaseModel):

    __root__: List[InboxResultEntry]
