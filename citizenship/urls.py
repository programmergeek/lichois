from django.urls import path, include
from django.urls.conf import path
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter
from .views import AdoptedChildRegistrationViewSet, DeclarationNaturalisationForeignSpouseViewSet
from .views import CertNaturalisationByForeignSpouseViewSet
from .admin_site import citizenship_admin

app_name = 'citizenship'

router = DefaultRouter()
router.register(r'adopted-child-registrations/', AdoptedChildRegistrationViewSet, basename='adopted-child-registrations')
router.register(r'declaration-intent-naturalisation-fs/',
                DeclarationNaturalisationForeignSpouseViewSet, basename='declaration-intent-naturalisation-fs')
router.register(r'cert-naturalisation-fs/',
                CertNaturalisationByForeignSpouseViewSet, basename='cert-naturalisation-fs')
router.register(r'foreign-spouse-naturalisation-certs/', AdoptedChildRegistrationViewSet, basename='foreign-spouse-naturalisation-certs')
router.register(r'settlement-citizenships/', AdoptedChildRegistrationViewSet, basename='settlement-citizenships')
router.register(r'citizenship-renunciation-declarations/', AdoptedChildRegistrationViewSet, basename='citizenship-renunciation-declarations')
router.register(r'citizenship-renunciations/', AdoptedChildRegistrationViewSet, basename='citizenship-renunciations')
router.register(r'citizenship-resumptions/', AdoptedChildRegistrationViewSet, basename='citizenship-resumptions')
router.register(r'late-citizenship-renunciationss/', AdoptedChildRegistrationViewSet, basename='late-citizenship-renunciations')
router.register(r'nationality-declarations/', AdoptedChildRegistrationViewSet, basename='nationality-declarations')
router.register(r'foreign-spouse-naturalisations/', AdoptedChildRegistrationViewSet, basename='foreign-spouse-naturalisations')
router.register(r'naturalisations/', AdoptedChildRegistrationViewSet, basename='naturalisations')
router.register(r'oath-of-allegiance/', AdoptedChildRegistrationViewSet, basename='oath-of-allegiance')
router.register(r'foreign-citizenship-renunciations/', AdoptedChildRegistrationViewSet, basename='foreign-citizenship-renunciations')
router.register(r'spouse-naturalisations/', AdoptedChildRegistrationViewSet, basename='spouse-naturalisations')
router.register(r'under-20-citizenships/', AdoptedChildRegistrationViewSet, basename='under-20-citizenships')


urlpatterns = [
    path('admin/', citizenship_admin.urls),
    path('', RedirectView.as_view(url='admin/'), name='home_url'),
    path('', include(router.urls)),

]

