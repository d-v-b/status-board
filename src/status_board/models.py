from pydantic import BaseModel
from typing import List, NamedTuple
from enum import Enum

class TaskType(str, Enum):
    SAMPLE_PREP = 'Preparing sample'
    CLEM = 'CLEM'
    STAINING = 'Staining and resin embedding'
    TEM = 'TEM quality check'
    FIBSEM_PREP = 'FIB-SEM prep'
    FIBSEM_IMAGING = 'FIB-SEM imaging'
    FIBSEM_RECON = 'Reconstruction'
    COSEM_IMPORT = 'Import'
    GROUND_TRUTH = 'Ground truth'
    ML_TRAINING = 'ML training'
    ML_INFERENCES = 'Inferences'
    ML_EVALUATION = 'Evaluation'
    CLEM_REGISTRATION = 'Registration'
    ML_REFINEMENTS = 'Refinements'
    ANALYSIS = 'Analysis'
    PUBLIC_RELEASE = 'Public release'
    OTHER = 'Other'

class ProgressType(str, Enum):
    NA = 'N/A'
    PLANNING = 'Planning'
    WAITING = 'Waiting'
    QUEUING = 'Queuing'
    PROGRESSING = 'Progressing'
    DONE = 'Done'


class Task(BaseModel):
    name: TaskType
    status: ProgressType
    duration_weeks: int

class TaskState(NamedTuple):
    status: ProgressType = 'N/A'
    duration_weeks: int = 0

class Tasks(BaseModel):
    sample_prep: TaskState
    clem_imaging: TaskState
    staining: TaskState
    tem_imaging: TaskState
    fibsem_prep: TaskState
    fibsem_imaging: TaskState
    fibsem_reconstruction: TaskState
    cosem_import: TaskState
    ground_truth: TaskState
    ml_training: TaskState
    ml_inference: TaskState
    ml_evaluation: TaskState
    clem_registration: TaskState
    ml_refinement: TaskState
    analysis: TaskState
    public_release: TaskState
    other: TaskState

class Project(BaseModel):
    name: str
    tasks: Tasks


class Board(BaseModel):
    projects: List[Project]


if __name__ == '__main__':
    print(Board.schema_json(indent=2))