from ninja.orm import create_schema

from app.internal.rest.camera.db.models import CameraImage

CameraImageSchema = create_schema(CameraImage)
