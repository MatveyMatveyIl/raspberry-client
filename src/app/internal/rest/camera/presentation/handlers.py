from app.internal.rest.camera.db.models import CameraImage
from app.internal.rest.camera.domain.entities import CameraImageSchema


class CameraHandler:

    def get_image(self, request):
        img = CameraImage.objects.first()
        return 200, CameraImageSchema.from_orm(img)
