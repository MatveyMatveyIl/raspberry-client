from django.contrib import admin

from app.internal.rest.indicators.presentation.admin import *
from app.internal.rest.light.presentation.admin import *
from app.internal.rest.microclimate.presentation.admin import *
from app.internal.rest.irrigation.presentation.admin import *
from app.internal.rest.camera.presentation.admin import *
from app.internal.rest.admin_user.presentation.admin import AdminUserAdmin

admin.site.site_title = "Agroaspect"
admin.site.site_header = "Agroaspect"
